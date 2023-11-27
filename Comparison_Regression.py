from Linear_Reg import Linear_Reg
from Expo_Reg import Expo_Reg
from Log_Reg import Log_Reg
from Polynomial_Reg import Polynomial_Reg
from Regression_Model import Regression_Model
from Regression_Context import Regression_Context




x = [1, 2, 3, 4, 5, 6, 7]
y = [2.5, 3.8, 4.2, 5.5, 7.0, 8.2, 10.0]

reg_models = [Linear_Reg, Expo_Reg, Log_Reg, Polynomial_Reg]

regression_context = Regression_Context(Linear_Reg(x,y))
comparison_arr = []

for model in reg_models:
    regression_context.set_strategy(model(x,y))
    regression_context.perform_Regression()
    container_arr = regression_context.get_container_arr()
    comparison_arr.append(container_arr)
 
sorted_data = sorted(comparison_arr, key=lambda x: x[-1])


print(sorted_data)


