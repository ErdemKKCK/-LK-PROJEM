In [1]: def calculate_product(*args):
 ...: product = 1
 ...: for value in args:
 ...: product *= value
 ...: return product
 ...:
In [2]: calculate_product(10, 20, 30)
Out[2]: 6000
In [3]: calculate_product(*range(1, 6, 2))
Out[3]: 15