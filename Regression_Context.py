from Regression_Model import Regression_Model

class Regression_Context:
    def __init__(self, strategy):
        self.strategy = strategy

    def set_strategy(self, strategy):
        self.strategy = strategy
    
    def perform_Regression(self):
        self.strategy.execute_Regression()
    
    def get_container_arr(self):
        return self.strategy.container_arr