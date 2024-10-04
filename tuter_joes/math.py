# math
import math

#Returns the smallest integer greater than or equal to x
print(math.ceil(4.1))  # Output: 5

#Returns the largest integer less than or equal to x.
print(math.floor(4.9))  # Output: 4

#Returns the integer part of x (equivalent to int(x)).
print(math.trunc(4.9))  # Output: 4

#Returns the absolute value of x as a float.
print(math.fabs(-5))  # Output: 5.0

#Returns the factorial of x (x!).
print(math.factorial(5))  # Output: 120

#Returns the greatest common divisor of x and y.
print(math.gcd(24, 36))  # Output: 12

#Returns the remainder of dividing x by y (as a float).
print(math.fmod(7, 3))  # Output: 1.0

#Returns the IEEE remainder of x divided by y.
print(math.remainder(9, 4))  # Output: 1.0

#Returns e raised to the power of x (e^x).
print(math.exp(2))  # Output: 7.38905609893065

#Returns the logarithm of x to the given base. If no base is provided, returns the natural logarithm (base e).
print(math.log(100, 10))  # Output: 2.0

#Returns the base-2/3/4/5 logarithm of x.
print(math.log2(8))  # Output: 3.0
print(math.log10(1000))  # Output: 3.0

#Returns x raised to the power of y.
print(math.pow(2, 3))  # Output: 8.0

#Returns the square root of x.
print(math.sqrt(25))  # Output: 5.0

#Returns the integer square root of x.
print(math.isqrt(17))  # Output: 4


#3. Trigonometric Functions

#math.sin(x)
#Returns the sine of x (in radians).
print(math.sin(math.pi / 2))  # Output: 1.0

#math.cos(x)
#Returns the cosine of x (in radians).
print(math.cos(math.pi))  # Output: -1.0

#math.tan(x)
#Returns the tangent of x (in radians).
print(math.tan(math.pi / 4))  # Output: 1.0

#math.asin(x)
#Returns the arc sine of x, in radians.
print(math.asin(1))  # Output: 1.5707963267948966

#math.acos(x)
#Returns the arc cosine of x, in radians.
print(math.acos(-1))  # Output: 3.141592653589793

#math.atan(x)
#Returns the arc tangent of x, in radians.
print(math.atan(1))  # Output: 0.7853981633974483

#math.atan2(y, x)
#Returns the arc tangent of y/x in radians. This function accounts for the signs of both x and y and returns the angle between the positive x-axis and the point (x, y).
print(math.atan2(1, 1))  # Output: 0.7853981633974483

#math.degrees(x)
#Converts angle x from radians to degrees.
print(math.degrees(math.pi))  # Output: 180.0

#math.radians(x)
#Converts angle x from degrees to radians.
print(math.radians(180))  # Output: 3

#math.pi
#The mathematical constant π (pi).
print(math.pi)  # Output: 3.141592653589793

#math.e
#The mathematical constant e.
print(math.e)  # Output: 2.718281828459045