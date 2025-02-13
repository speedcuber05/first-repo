import numpy as np
from io import StringIO
data = "1, 2, 3\n4, 5, 6"
print(np.genfromtxt(StringIO(data), delimiter=","))

data1 = "  1  2  3\n  4  5 67\n890123  4"
print(np.genfromtxt(StringIO(data1), delimiter=3))
data2 = "123456789\n   4  7 9\n   4567 9"
print(np.genfromtxt(StringIO(data2), delimiter=(4, 3, 2)))

data3= "1, abc , 2\n 3, xxx, 4"
# Without autostrip
print(np.genfromtxt(StringIO(data3), delimiter=",", dtype="|U5"))
# With autostrip
print(np.genfromtxt(StringIO(data3), delimiter=",", dtype="|U5", autostrip=True))

data4 = """#
# Skip me !
# Skip me too !
1, 2
3, 4
5, 6 #This is the third line of the data
7, 8
# And here comes the last line
9, 0
"""
print(np.genfromtxt(StringIO(data4), comments="#", delimiter=","))

data5 = "\n".join(str(i) for i in range(10))
print(np.genfromtxt(StringIO(data5)),
np.genfromtxt(StringIO(data5),
              skip_header=3, skip_footer=5))