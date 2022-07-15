import numpy as np
import statsmodels.api as sm

x = [
  [0, 1], [5, 1], [15, 2], [25, 5], [35, 11], [45, 15], [55, 34], [60, 35]
]
y = [4, 5, 20, 14, 32, 22, 38, 43]
x, y = np.array(x), np.array(y)

x = sm.add_constant(x)
model = sm.OLS(y, x)
results = model.fit()
print(results.summary())