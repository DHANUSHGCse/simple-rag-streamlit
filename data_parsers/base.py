from abc import ABC, abstractmethod
from typing import List
from langchain_core.documents import Document


class BaseDataParser(ABC):
    """
    Abstract base class for all document parsers.
    Ensures consistent interface across file types.
    """

    @abstractmethod
    def parse(self, file) -> List[Document]:
        """
        Parse an uploaded file into LangChain Documents.
        """
        pass
