house1_actual = 1000000
house1_pred = 1100000

house2_actual = 2000000
house2_pred = 2010000

mse = (
    (house2_actual - house2_pred)**2 + 
    (house1_actual-house1_pred)**2
    )/2

print(mse)

normalized_house2 = ((house2_actual - house2_pred)/house2_actual)
normalized_house1 = ((house1_actual - house1_pred)/house1_actual)

mse = (normalized_house1**2 + normalized_house2**2)/2

print(mse)