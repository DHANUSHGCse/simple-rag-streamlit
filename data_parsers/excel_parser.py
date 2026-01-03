import tempfile
from typing import List
from langchain_core.documents import Document
from langchain_community.document_loaders import UnstructuredExcelLoader
from .base import BaseDataParser


class ExcelDataParser(BaseDataParser):

    def parse(self, file) -> List[Document]:
        with tempfile.NamedTemporaryFile(delete=False, suffix=".xlsx") as tmp:
            tmp.write(file.read())
            tmp_path = tmp.name

        loader = UnstructuredExcelLoader(tmp_path)
        return loader.load()
