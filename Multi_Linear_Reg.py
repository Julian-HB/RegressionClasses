import numpy as np
from statistics import mean

class Multi_Linear_Reg:
    def __init__(self, matrix: list, y_arr: list):
        """
        Initialisiert eine Instanz der Multi_Linear_Reg Klasse.

        Args:
        matrix (list): Eine Liste von Listen, die die unabhängigen Variablen darstellt.
        y_arr (list): Eine Liste, die die abhängige Variable darstellt.
        determination_coeficient: float
        Der zu berechnende Determinationskoeffizient
        function_string: String
        Die auszugebende Funktion

        Returns:
        None
        """
        self.y_arr = y_arr
        self.vector_arr = []
        self.matrix = matrix
        self.matrix_Ex = []
        self.parameter_arr = []
        self.solv_vector = []
        self.reg_arr = []
        self.determination_coeficient = 0.0;
        self.function_string = "";
        self.regression_name = "Multi-Lineare Regression"

    def create_matrix(self):
        """
        Erstellt eine Matrix der unabhängigen Variablen.

        Returns:
        None
        """
        ones_array = self.create_one_array()
        self.matrix.insert(0, ones_array)
        self.matrix = np.transpose(self.matrix)
        #print(self.matrix)

    def calculate_solv_solution(self):
        """
        Berechnet die Lösung des linearen Gleichungssystems.

        Returns:
        None
        """
        self.matrix_Ex = np.matmul(np.transpose(self.matrix) , self.matrix)
        self.vector_arr = np.matmul(np.linalg.inv(self.matrix_Ex), np.matmul(np.transpose(self.matrix), np.transpose(self.y_arr)))

    def create_one_array(self):
        """
        Erstellt ein Array von Einsen mit der gleichen Länge wie des Arrays y_arr.

        Returns:
        arr (list): Ein Array von Einsen.
        """
        arr = []
        for i in range(len(self.y_arr)):
            arr.append(1)
        return arr
    
    def print_Funktion(self):
        '''
        Gibt die berechneten Parameter als mathematische multiple lineare Funktion aus.

        Returns
        -------
        None
        '''
        equation = "y = "
        for i, param in enumerate(self.vector_arr):
            if i == 0:
                equation += str(param)
            else:
                equation += " + " + str(param) + "*x_" + str(i)
        print("Die Funktion lautet:", equation)
    
    def calc_reg_arr(self):
        """
        Berechnet den Array mit den Ergebnissen der Multiplen Linearen Regression.
        Returns:
        reg_arr (list): Array mit den Ergebnissen der Multiplen Linearen Regression.
        """
        for row in self.matrix:
            result = 0
            for i, param in enumerate(self.vector_arr):
                result += param * row[i]
            self.reg_arr.append(result)
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
    
    def save_Funktion(self):
        '''
        Speichert die Funktion in function_string.

        Returns
        -------
        None
        '''
        equation = "y = "
        for i, param in enumerate(self.vector_arr):
            if i == 0:
                equation += str(param)
            else:
                equation += " + " + str(param) + "*x_" + str(i)
        self.function_string = equation

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
        self.create_matrix
        self.calculate_solv_solution()
        self.calc_reg_arr()
        self.caluculate_determination_coefficitient
        self.save_Funktion
        self.save_Regression_items
    
