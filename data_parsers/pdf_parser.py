import tempfile
from typing import List
from langchain_core.documents import Document
from langchain_community.document_loaders import PyMuPDFLoader
from .base import BaseDataParser


class PDFDataParser(BaseDataParser):

    def parse(self, file) -> List[Document]:
        with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
            tmp.write(file.read())
            tmp_path = tmp.name

        loader = PyMuPDFLoader(tmp_path)
        return loader.load()
