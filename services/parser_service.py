from typing import List, Dict
from langchain_core.documents import Document

from data_parsers import DataParserFactory
from exceptions import FileParsingError


class ParserService:

    @classmethod
    def parse_files(cls, uploaded_files: List) -> Dict[str, List[Document]]:
        documents: Dict[str, List[Document]] = {}
        errors: Dict[str, str] = {}

        for file in uploaded_files:
            try:
                parser = DataParserFactory.get_parser(file.name)
                docs = parser.parse(file)

                for doc in docs:
                    doc.metadata.setdefault("source", file.name)

                documents[file.name] = docs

            except Exception as exc:
                # DO NOT crash the app
                errors[file.name] = str(exc)

        return documents, errors
