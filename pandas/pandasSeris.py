import numpy as np
import pandas as pd

# a = np.array([1, 2, 4]) #1*3+2*1+4*5 = 25  vector multiply vector = scalar
# b = np.array([3, 1, 5])

# print(np.dot(a, b))


# x = np.array([[1, 2], [3, 4]])
# print(x.T)


# a = np.array([[1, 1, 2], [1, -1, 3], [2, 3, 1]])
# b = np.array([[2, 3, 1],
#               [-1, 2, 1],
#               [0, 3, 1]])

# print(np.dot(a, b))

# products = ["A", "B", "C", "D"]

# product_categories = pd.Series(products)
# print(type(product_categories))

# daily_rates_dollars = pd.Series([40, 45, 50, 60])
# print(type(daily_rates_dollars))

# array_a = np.array([10, 20, 30, 40, 50])

# series_a = pd.Series(array_a)
# print(type(series_a))


# series_a = pd.Series([10, 20, 30, 40, 50])

# print(series_a.dtype) #int64
# print(series_a.size) #5


# product_categories = pd.Series(["A", "B", "C", "D"])
# print(type(product_categories.dtype))
# print(type(product_categories.size))
# product_categories.name = "Product Categories"
# print(product_categories)
# print(product_categories.name)

prices_per_category = {
    "A": 100,
    "B": 200,
    "C": 300
}

# print(type(prices_per_category)) #dict

prices_per_category = pd.Series(prices_per_category)
# print(type(prices_per_category))
# print(prices_per_category.index)
print(type(prices_per_category.index))
