import numpy as np
from statistics import mean
from Regression_Model import Regression_Model

class Polynomial_Reg(Regression_Model):
    """
    x_arr: Array
        Die Werte der unabhängigen Parameter.
    y_arr: Array
        Die Werte der abhängigen Parameter.
    reg_arr: Array
        Ein Array mit den berechneten Werten des Regressionsgraphen.
    matrix: Array
        Eine Matrix zur Speicherung der Koeffizienten.
    parameter_arr: Array
        Ein Array zur Speicherung der berechneten Parameter.
    solv_vector: Array
        Ein Array zur Speicherung des Lösungsvektors.
    determination_coeficient: float
        Der zu berechnende Determinationskoeffizient
    function_string: String
        Die auszugebende Funktion
    """
    def __init__(self, x_arr: list, y_arr: list):
        self.x_arr = x_arr
        self.y_arr = y_arr
        self.y_avarrage = mean(y_arr);
        self.reg_arr = []
        self.matrix = []
        self.parameter_arr = []
        self.solv_vector = []
        self.reg_arr = []
        self.determination_coeficient = 0.0;
        self.function_string = "";
        self.regression_name = "Polynomiale Regression"
        self.container_arr = []

    def calculate_exponential_sum(self, arr, j, i):
        '''
        Berechnet die Summe der Exponentialfunktion für die Matrixerstellung.

        Parameters
        ----------
        arr: Array
            Das Array der unabhängigen Parameter.
        j: int
            Der Spaltenindex.
        i: int
            Der Zeilenindex.

        Returns
        -------
        float
        Die berechnete Summe.
        '''
        num = i+j
        return np.sum(np.power(arr, num))

    def create_matrix(self, j, i):
        '''
        Erstellt die Koeffizientenmatrix für die Polynomische Regression.

        Parameters
        ----------
        j: int
            Die Anzahl der Zeilen in der Matrix.
        i: int
            Die Anzahl der Spalten in der Matrix.

        Returns
        -------
        None
        '''
        for rows in range(j):
            row = []
            for columns in range(i):
                sum_x = self.calculate_exponential_sum(self.x_arr, columns, rows)
                row.append(sum_x)
                #print(sum_x)
            self.matrix.append(row)
        self.matrix[0][0] = len(self.x_arr)
        #print(self.matrix)
    
    def calculate_solv_vector(self, j):
        '''
        Berechnet den Lösungsvektor für die polynomiale Regression.

        Parameters
        ----------
        j: int
        Die Anzahl der Elemente im Lösungsvektor.

        Returns
        -------
        None
        '''
        for n in range(j):
            arr = np.multiply(np.power(self.x_arr, n), self.y_arr)
            self.solv_vector.append(np.sum(arr))
            
        #print(self.solv_vector)

    def jordan_gauß_alg(self):
        '''
        Löst das Gleichungssystem mit dem Gauss-Jordan-Verfahren.

         Returns
        -------
        parameter_arr: Array
        Das Array der berechneten Parameter.
        '''       
        self.parameter_arr = np.linalg.solve(self.matrix, self.solv_vector)
        return self.parameter_arr
        #print(self.parameter_arr):

    def print_Funktion(self):
        '''
        Gibt die berechneten Parameter als mathematische polynomiale Funktion aus.

        Returns
        -------
        None
        '''
        equation = "y = "
        for i, param in enumerate(self.parameter_arr):
            if i == 0:
                equation += str(param)
            else:
                equation += " + " + str(param) + "*x^" + str(i)
        #print("Die Funktion lautet:", equation)
    
    def calc_reg_arr(self):
        '''
        Berechnet die Regressionslinie für die polynomische Regression.

        Returns
        -------
        reg_line: Array
            Ein Array mit den berechneten Werten dem Regressionsgraphen.
        '''
        for x in self.x_arr:
            y = 0
            for i, param in enumerate(self.parameter_arr):
                y += param * (x ** i)
            self.reg_arr.append(y)
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
        for i, param in enumerate(self.parameter_arr):
            if i == 0:
                equation += str(param)
            else:
                equation += " + " + str(param) + "*x^" + str(i)
        self.function_string = equation
        #print("Die Funktion lautet:", equation)

    def save_Regression_items(self):
        '''
        Speichert und gibt  die Eigenschaften der Regressionsfunktion in self.container_arr zurück.

        Returns
        -------
        None
        '''
        self.container_arr = [self.regression_name, self.function_string, self.reg_arr, self.determination_coeficient]
        return self.container_arr
    
    def reset_attributes(self):
        """
        Setzt alle Objektattribute auf ihre Ausgangswerte zurück.
        """
        self.reg_arr = []
        self.matrix = []
        self.parameter_arr = []
        self.solv_vector = []
        self.determination_coeficient = 0.0
        self.function_string = ""
        self.container_arr = []
    
    def execute_Regression(self):
        '''
        Führt alle Methoden aus, welche zur durchführung der Regression notwendig sind.

        Returns
        -------
        None
        '''
        polynom_arr = []
        for n in range(2,8):
            self.create_matrix(n, n)
            self.calculate_solv_vector(n)
            self.jordan_gauß_alg()
            self.calc_reg_arr()
            coefficient = self.caluculate_determination_coefficitient()
            polynom_arr.append([n, coefficient])
            self.reset_attributes()
        
        sorted_arr = sorted(polynom_arr, key=lambda x: x[-1])
        
        polynom = sorted_arr[0][0]
        self.create_matrix(polynom, polynom)
        self.calculate_solv_vector(polynom)
        self.jordan_gauß_alg()
        self.calc_reg_arr()
        self.caluculate_determination_coefficitient()
        self.save_Funktion()
        self.save_Regression_items()