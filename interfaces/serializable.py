from abc import ABC, abstractmethod

class Serializable(ABC):
    @abstractmethod
    def get_dict(self) -> dict:
        ...