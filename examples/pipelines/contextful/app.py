import os

import pathway as pw
from pathway.stdlib.ml.index import KNNIndex

from llm_app.model_wrappers import OpenAIChatGPTModel, OpenAIEmbeddingModel


class DocumentInputSchema(pw.Schema):
    doc: str


class QueryInputSchema(pw.Schema):
    query: str
    user: str


def run(
    *,
    data_dir1: str = os.environ.get("PATHWAY_DATA_DIR1", "./examples/data/pathway-docs/"),
    data_dir2: str = os.environ.get("PATHWAY_DATA_DIR2", "./examples/data/pathway-docs1/"),
    api_key: str = os.environ.get("OPENAI_API_TOKEN", ""),
    host: str = "0.0.0.0",
    port: int = 8080,
    embedder_locator: str = "text-embedding-ada-002",
    embedding_dimension: int = 1536,
    model_locator: str = "gpt-3.5-turbo",
    max_tokens: int = 60,
    temperature: float = 0.0,
    **kwargs,
):
    embedder = OpenAIEmbeddingModel(api_key=api_key)

    # Load and process the first dataset
    documents1 = pw.io.jsonlines.read(
        data_dir1,
        schema=DocumentInputSchema,
        mode="streaming",
        autocommit_duration_ms=50,
    )

    enriched_documents1 = documents1 + documents1.select(
        vector=embedder.apply(text=pw.this.doc, locator=embedder_locator)
    )

    # Load and process the second dataset
    documents2 = pw.io.jsonlines.read(
        data_dir2,
        schema=DocumentInputSchema,
        mode="streaming",
        autocommit_duration_ms=50,
    )

    enriched_documents2 = documents2 + documents2.select(
        vector=embedder.apply(text=pw.this.doc, locator=embedder_locator)
    )

    # Combine the two datasets (enriched_documents1 and enriched_documents2) if needed.

    index1 = KNNIndex(
        enriched_documents1.vector, enriched_documents1, n_dimensions=embedding_dimension
    )

    index2 = KNNIndex(
        enriched_documents2.vector, enriched_documents2, n_dimensions=embedding_dimension
    )

    query, response_writer = pw.io.http.rest_connector(
        host=host,
        port=port,
        schema=QueryInputSchema,
        autocommit_duration_ms=50,
    )

    query += query.select(
        vector=embedder.apply(text=pw.this.query, locator=embedder_locator),
    )

    query_context = query + index1.get_nearest_items(
        query.vector, k=3, collapse_rows=True
    ).select(documents_list=pw.this.doc)

    @pw.udf
    def build_prompt(documents, query):
        docs_str = "\n".join(documents)
        prompt = f"Given the following documents : \n {docs_str} \nanswer this query: {query}"
        return prompt

    prompt = query_context.select(
        prompt=build_prompt(pw.this.documents_list, pw.this.query)
    )

    model = OpenAIChatGPTModel(api_key=api_key)

    responses = prompt.select(
        query_id=pw.this.id,
        result=model.apply(
            pw.this.prompt,
            locator=model_locator,
            temperature=temperature,
            max_tokens=max_tokens,
        ),
    )

    response_writer(responses)

    pw.run()


if __name__ == "__main__":
    run()
