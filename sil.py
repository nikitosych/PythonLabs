from functools import reduce

silnia = lambda n: 1 if n == 0 else reduce(lambda x, y: x * y, range(1, n + 1))
