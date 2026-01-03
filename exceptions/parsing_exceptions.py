class ParsingError(Exception):
    """Base exception for all parsing errors."""
    pass


class UnsupportedFileTypeError(ParsingError):
    pass


class FileParsingError(ParsingError):
    pass
