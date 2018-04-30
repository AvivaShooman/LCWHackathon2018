from fractions import Fraction
import math

n = str(math.sqrt(2018))
f = Fraction(n)
number = f.limit_denominator(20180)
print(number)