import tempfile
from typing import List
from langchain_core.documents import Document
from langchain_community.document_loaders import JSONLoader
from .base import BaseDataParser


class JSONDataParser(BaseDataParser):

    def parse(self, file) -> List[Document]:
        with tempfile.NamedTemporaryFile(delete=False, suffix=".json") as tmp:
            tmp.write(file.read())
            tmp_path = tmp.name

        loader = JSONLoader(
            file_path=tmp_path,
            jq_schema=".",
            text_content=False
        )
        return loader.load()
