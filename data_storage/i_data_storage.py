# data_storage/i_data_storage.py

from abc import ABC, abstractmethod
from typing import List

class IDataStorage(ABC):
    @abstractmethod
    def save_data(self, data):
        pass

    @abstractmethod
    def read_data(self)-> List[str]:
        pass
