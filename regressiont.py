import numpy as np
from sklearn.linear_model import LinearRegression

x = [
  [0, 1], [5, 1], [15, 2], [25, 5], [35, 11], [45, 15], [55, 34], [60, 35]
]
y = [4, 5, 20, 14, 32, 22, 38, 43]

x, y = np.array(x), np.array(y)

model = LinearRegression().fit(x, y)
r_sq = model.score(x, y)
print(f"coefficient of determination: {r_sq}")
print(f"slope: {model.coef_}")
print(f"intercept: {model.intercept_}")
y_pred = model.predict(x)
print(f"predicted response:\n{y_pred}")

