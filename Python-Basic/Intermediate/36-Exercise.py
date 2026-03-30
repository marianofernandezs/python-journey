from functools import reduce

numbers = [1,2,3,4,5,6,6,1,10]

r = reduce(lambda x,y: x+y, numbers)

print(r)
