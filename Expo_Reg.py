from statistics import mean
import numpy as np
from Regression_Model import Regression_Model

class Expo_Reg(Regression_Model):
    """
    x_arr: Array
        Die Werte der unabhängigen Parameter.
    y_arr: Array
        Die Werte der abhängigen Parameter (logarithmiert).
    x_average: float
        Der Durchschnittswert von x_arr.
        Berechnet unter Einsatz des arithmetischen Mittels.
    y_average: float
        Der Durchschnittswert von y_arr.
        Berechnet unter Einsatz des arithmetischen Mittels.
    m_value: float
        Die Steigung der logarithmisierten exponentiellen Regressionskurve.
    b_value: float
        Der Achsenabschnitt der Ordinate.
    m_value_exp: float
        Der Exponentialwert der Steigung.
    b_value_exp: float
        Der Exponentialwert des Achsenabschnitts.
    reg_arr: Array
        Ein Array zur Speicherung der Regressionswerte.
    determination_coeficient: float
        Der zu berechnende Determinationskoeffizient
    function_string: String
        Die auszugebende Funktion
    """
    def __init__(self, x_arr: list, y_arr: list):
        self.x_arr = x_arr
        self.y_arr = np.log10(y_arr)
        self.x_average = mean(x_arr)
        self.y_average = mean(self.y_arr)
        self.m_value = 0
        self.b_value = 0
        self.m_value_exp = 0
        self.b_value_exp = 0
        self.reg_arr = []
        self.determination_coeficient = 0.0
        self.function_string = ""
        self.container_arr = []
        self.regression_name = "Exponentielle Regression"

    def calculate_m_value(self):
        '''
        Berechnet die Steigung der logarithmisierten exponentiellen Regressionskurve.

        Returns
        -------
        None
        '''
        k_one = 0
        k_two = 0

        for i,j in enumerate(self.y_arr):
            k_one += (self.x_arr[i] - self.x_average)*(self.y_arr[i] - self.y_average)
            k_two += (self.x_arr[i] - self.x_average)*(self.x_arr[i] - self.x_average)

        self.m_value = k_one / k_two

    def calculate_b_value(self):
        '''
        Berechnet den Achsenabschnitt der logarithmisierten exponentiellen Regressionskurve.

        Returns
        -------
        None
        '''
        self.b_value = self.y_average - self.m_value * self.x_average

    def exp_calculate_m_value(self):
        '''
        Berechnet den Exponentialwert der Steigung.

        Returns
        -------
        None
        '''
        self.m_value_exp = np.power(10, self.m_value)

    def exp_calculate_b_value(self):
        '''
        Berechnet den Exponentialwert des Achsenabschnitts.

        Returns
        -------
        None
        '''
        self.b_value_exp = np.power(10, self.b_value)

    def calc_reg_arr(self):
        '''
        Berechnet die prognostizierten Werte und speichert sie in reg_arr.

        Returns
        -------
        self.reg_arr
        '''
        for x in self.x_arr:
            y_pred = self.b_value_exp * np.power(self.m_value_exp, x)
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
            regression_variance += (self.reg_arr[i] - self.y_average)**2
            total_variance += (self.y_arr[i] - self.y_average)**2

        self.determination_coeficient = regression_variance / total_variance
        return self.determination_coeficient

    def print_Funktion(self):
        '''
        Gibt die Funktion der exponentiellen Regression aus.

        Returns
        -------
        None
        '''
        print("Die Funktion lautet: y =", str(self.b_value_exp), "*", str(self.m_value_exp), "^x")

    def save_Funktion(self):
        '''
        Speichert die Funktion in function_string.

        Returns
        -------
        None
        '''
        self.function_string=("y =", str(self.b_value_exp), "*", str(self.m_value_exp), "^x")
    
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
        self.calculate_m_value()
        self.calculate_b_value()
        self.exp_calculate_m_value()
        self.exp_calculate_b_value()
        self.calc_reg_arr()
        self.caluculate_determination_coefficitient()
        self.save_Funktion()
        self.save_Regression_items()