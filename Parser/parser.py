from abc import ABC, abstractmethod
from ConcreteSerializer.serializer import Serializer
"""Abstract class Parser"""


class Parser(ABC):
    def __init__(self):
        self.serializer = Serializer()

    @abstractmethod
    def dump(self, obj, file):
        pass

    @abstractmethod
    def dumps(self, obj):
        pass

    @abstractmethod
    def load(self, file):
        pass

    @abstractmethod
    def loads(self, string):
        pass
