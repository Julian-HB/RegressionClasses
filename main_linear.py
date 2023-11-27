from Polynomial_Reg import Polynomial_Reg
import numpy as np
import matplotlib.pyplot as plt

# Deine gegebenen Daten
x = np.array([1, 2, 3, 4, 5, 6, 7])
y = np.array([1, 6, 10, 17, 28, 38, 61])

# Instanziierung der Klasse mit den gegebenen Daten
poly_reg = Polynomial_Reg(x, y)

# Erstellen der Matrix
poly_reg.create_matrix(5, 5)  # Beispiel: Polynomgrad 2 (3 Koeffizienten)

# Berechnen des Lösungsvektors
poly_reg.calculate_solv_vector(5)  # Beispiel: Polynomgrad 2 (3 Koeffizienten)

# Anwenden der Jordan-Gauß-Elimination und Berechnen der Koeffizienten
poly_reg.jordan_gauß_alg()

poly_reg.print_Funktion()

y_pred = poly_reg.calc_reg_arr()

cof = poly_reg.caluculate_determination_coefficitient()
print(cof)