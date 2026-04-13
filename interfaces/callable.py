from abc import ABC, abstractmethod

class Nameable(ABC):
    @abstractmethod
    def get_name(self) -> str:
        ...
