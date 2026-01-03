import tempfile
from typing import List

from langchain_core.documents import Document
from langchain_community.document_loaders import Docx2txtLoader

from .base import BaseDataParser


class DocxDataParser(BaseDataParser):
    """
    DOCX file parser using Docx2txtLoader.
    Converts Word documents into LangChain Documents.
    """

    def parse(self, file) -> List[Document]:
        # Write Streamlit file object to temp file
        with tempfile.NamedTemporaryFile(delete=False, suffix=".docx") as tmp:
            tmp.write(file.read())
            tmp_path = tmp.name

        loader = Docx2txtLoader(tmp_path)
        return loader.load()
