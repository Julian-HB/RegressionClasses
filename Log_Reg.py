
from statistics import mean
import numpy as np
import math
from Regression_Model import Regression_Model

class Log_Reg(Regression_Model):
    """
    x_arr: Array
        Die Werte der unabhängigen Parameter.
    y_arr: Array
        Die Werte der abhängigen Parameter.
    y_arr_log: Array
        Die logarithmierten Werte von y_arr.
    x_avarrage: float
        Der Durchschnittswert von x_arr.
        Berechnet unter Einsatz des arithmetischen Mittels.
    y_avarrage: float
        Der Durchschnittswert von y_arr_log.
        Berechnet unter Einsatz des arithmetischen Mittels.
    m_value: float
        Die Steigung der Regressionskurve.
    b_value: float
        Der Achsenabschnitt der Ordinate.
    reg_arr: Array
        Ein Array zur Speicherung der Regressionswerte.
    determination_coeficient: float
        Der zu berechnende Determinationskoeffizient
    function_string: String
        Die auszugebende Funktion
    """
    def __init__(self, x_arr: list, y_arr: list):
        self.x_arr = x_arr;
        self.y_arr = y_arr;
        self.y_arr_log = [0] * len(y_arr)
        self.x_avarrage = mean(x_arr);
        self.y_avarrage = 0;
        self.m_value = 0;
        self.b_value = 0;
        self.reg_arr = [];
        self.determination_coeficient = 0.0;
        self.function_string = "";
        self.regression_name = "Logistische Regression"
        self.container_arr = []
    
    def logarithmize_y_arr(self):
        '''
        Berechnet den Logarithmus der Werte in y_arr.

        Returns
        -------
        None
        '''
        for i, x in enumerate(self.y_arr):
            self.y_arr_log[i] = math.log((30 / self.y_arr[i]) - 1)

        self.y_avarrage = mean(self.y_arr_log)

    def calculate_m_value(self):
        '''
        Berechnet die Steigung der Regressionskurve.

        Returns
        -------
        None
        '''
        k_one = 0
        k_two = 0

        for i,j in enumerate(self.y_arr_log):
            k_one += (self.x_arr[i] - self.x_avarrage)*(self.y_arr_log[i] - self.y_avarrage)
            k_two += (self.x_arr[i] - self.x_avarrage)*(self.x_arr[i] - self.x_avarrage)

        self.m_value = k_one / k_two

    def calculate_b_value(self):
        '''
        Berechnet den Achsenabschnitt der Ordinate.

        Returns
        -------
        None
        '''
        self.b_value = self.y_avarrage - self.m_value*self.x_avarrage

    def exp_calculate_m_value(self):
        '''
        Berechnet den Exponentialwert der Steigung.

        Returns
        -------
        None
        '''
        self.m_value = np.exp(self.m_value)

    def exp_calculate_b_value(self):
        '''
        Berechnet den Exponentialwert des Achsenabschnitts.

        Returns
        -------
        None
        '''
        self.b_value = np.exp(self.b_value)    
    
    def calc_reg_arr(self):
        '''
        Berechnet die Regressionswerte und speichert sie in reg_arr.

        Returns
        -------
        self.reg_arr
        '''
        for i, x in enumerate(self.x_arr):
            y_pred = 30 / (np.exp(self.b_value + self.m_value * x) + 1)
            self.reg_arr.append(y_pred)

        return self.reg_arr

    def caluculate_determination_coefficitient(self):
        '''
        Berechnet den Determinationskoeffizient und speichert diesen in detcof.

        Returns
        -------
        self.detCof
        '''
        regression_variance = 0
        total_variance = 0

        for i, x in enumerate(self.x_arr):
            regression_variance += (self.reg_arr[i] - self.y_avarrage)**2
            total_variance += (self.y_arr[i] - self.y_avarrage)**2

        self.determination_coeficient = regression_variance / total_variance
        return self.determination_coeficient
    
    def print_Funktion(self):
        '''
        Gibt die Funktion der logistischen Regression aus.

        Returns
        -------
        None
        '''
        print("Die Funktion lautet: y =", str(30) + " / (1 + exp(-(" + str(self.b_value) + " + " + str(self.m_value) + " * x)))")
    
    def save_Funktion(self):
        '''
        Speichert die Funktion in function_string..

        Returns
        -------
        None
        '''
        self.function_string=("y =", str(30) + " / (1 + exp(-(" + str(self.b_value) + " + " + str(self.m_value) + " * x)))") 
    
    def save_Regression_items(self):
        '''
        Speichert und gibt  die Eigenschaften der Regressionsfunktion in self.container_arr zurück.

        Returns
        -------
        None
        '''
        self.container_arr = [self.regression_name, self.function_string, self.reg_arr, self.determination_coeficient]
        return self.container_arr
    
    def execute_Regression(self):
        '''
        Führt alle Methoden aus, welche zur durchführung der Regression notwendig sind.

        Returns
        -------
        None
        '''
        self.logarithmize_y_arr()
        self.calculate_m_value()
        self.calculate_b_value()
        #self.exp_calculate_m_value
        #self.exp_calculate_b_value
        self.calc_reg_arr()
        self.caluculate_determination_coefficitient()
        self.save_Funktion()
        self.save_Regression_items()