import tempfile
from typing import List
from langchain_core.documents import Document
from langchain_community.document_loaders import TextLoader
from .base import BaseDataParser


class TextDataParser(BaseDataParser):

    def parse(self, file) -> List[Document]:
        with tempfile.NamedTemporaryFile(delete=False, suffix=".txt") as tmp:
            tmp.write(file.read())
            tmp_path = tmp.name

        loader = TextLoader(tmp_path, encoding="utf-8")
        return loader.load()
