import tempfile
from typing import List

from langchain_core.documents import Document
from langchain_community.document_loaders import UnstructuredCSVLoader

from .base import BaseDataParser


class CSVDataParser(BaseDataParser):
    """
    Robust CSV parser with encoding fallback.
    Handles UTF-8, Windows-1252, Latin-1 safely.
    """

    def parse(self, file) -> List[Document]:
        raw_bytes = file.read()

        # Try common encodings
        for encoding in ("utf-8", "utf-8-sig", "cp1252", "latin-1"):
            try:
                text = raw_bytes.decode(encoding)
                break
            except UnicodeDecodeError:
                text = None

        if text is None:
            # Absolute fallback (never crash ingestion)
            text = raw_bytes.decode("latin-1", errors="replace")

        with tempfile.NamedTemporaryFile(
            delete=False, suffix=".csv", mode="w", encoding="utf-8"
        ) as tmp:
            tmp.write(text)
            tmp_path = tmp.name

        loader = UnstructuredCSVLoader(tmp_path)
        return loader.load()
