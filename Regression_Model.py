from abc import ABC, abstractmethod

class Regression_Model(ABC):
    @abstractmethod
    def execute_Regression(self, x, y):
        pass