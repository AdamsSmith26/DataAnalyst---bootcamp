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

# prices_per_category = {
#     "A": 100,
#     "B": 200,
#     "C": 300
# }

# print(type(prices_per_category)) #dict

# prices_per_category = pd.Series(prices_per_category)
# print(type(prices_per_category))
# print(prices_per_category.index)
# print(type(prices_per_category.index))


# serias_a = pd.Series([10, 20, 30, 40, 50])
# print(list(serias_a.index))
# prices_per_category = pd.Series({"A": 100, "B": 101, "C":102})
# print(prices_per_category[0])

# series_b = pd.Series([10, 20, 30, 40, 50], index=[1, 2, 3, 4, 5])
# print(series_b[0]) #key_error
# series_c = pd.Series([10, 20, 30, 40, 50], index=['1', '2', '3', '4', '5'])
# print(series_c[3])

# start_date_depozits = pd.Series({
#     "7/4/2014" : 2000,
#     "8/4/2014" : 1000,
#     "9/4/2014" : 2000,
#     "1/4/2014" : 4000,
#     "2/4/2014" : 2500,
#     "3/4/2014" : 2000,
#     "4/4/2014" : 2300,
#     "5/4/2014" : 3000,
#     "6/4/2014" : 2800,
#     "7/1/2014" : 1500,
#     "7/2/2014" : 1000,
#     "7/3/2014" : 2000,
# })

# print(start_date_depozits)

# print(start_date_depozits.sum) #return nothing

# print(start_date_depozits.sum())
# print(start_date_depozits.min())
# print(start_date_depozits.max())
# print(start_date_depozits.idxmin()) #idx=index
# print(start_date_depozits.idxmax())


# print(start_date_depozits.head(3)) #first n elements  default = 5
# print(start_date_depozits.tail(3)) #last n elements


data = {"productName": ["Product A", "Product B", "Product C"], "productPrice": [200, 100, 300]}
# df = pd.DataFrame(data)
df = pd.DataFrame(data, index=["A", "B", "C"])
print(df)