from data_parsers.docx_parser import DocxDataParser
from .text_parser import TextDataParser
from .pdf_parser import PDFDataParser
from .csv_parser import CSVDataParser
from .excel_parser import ExcelDataParser
from .json_parser import JSONDataParser
from .exceptions import UnsupportedFileTypeError


class DataParserFactory:
    """
    Factory class to return correct parser
    based on uploaded file extension.
    """

    _PARSERS = {
        ".txt": TextDataParser(),
        ".pdf": PDFDataParser(),
        ".csv": CSVDataParser(),
        ".xlsx": ExcelDataParser(),
        ".xls": ExcelDataParser(),
        ".json": JSONDataParser(),
        ".docx": DocxDataParser(),
    }

    @classmethod
    def get_parser(cls, filename: str):
        ext = "." + filename.split(".")[-1].lower()

        if ext not in cls._PARSERS:
            raise UnsupportedFileTypeError(
                f"Unsupported file type: {ext}"
            )

        return cls._PARSERS[ext]
