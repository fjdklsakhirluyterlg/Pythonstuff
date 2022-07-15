import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

x = np.array([5, 15, 25, 35, 45, 55]).reshape((-1, 1))
y = np.array([15, 11, 2, 8, 25, 32])

transformer = PolynomialFeatures(degree=2, include_bias=False)
transformer.fit(x)
x_ = transformer.transform(x)

model = LinearRegression().fit(x_, y)

r_sq = model.score(x_, y)
print(f"coefficient of determination: {r_sq}")


print(f"intercept: {model.intercept_}")


print(f"coefficients: {model.coef_}")

y_pred = model.predict(x_)
print(f"predicted response:\n{y_pred}")