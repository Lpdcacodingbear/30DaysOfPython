'''
***
* 1. Declare your age as integer variable
* 2. Declare your height as a float variable
* 3. Declare a complex number variable
***
'''
age = 18
height = 182.1
complex_number = 18-2j
print('My age is ', age)
print('My height is ', height)
print('I have a complex number is ', complex_number)


# ***
# 4. Write a script that prompts the user to enter base and height of
#    the triangle and calculate an area of this triangle (area = 0.5 x b x h).
# ***
base = input('Enter base: ')
_height = input('Enter height: ')
area = 0.5 * base * _height
print('The area of the triangle is ', area)


# ***
# 5. Write a script that prompts the user to enter side a, side b, and
#    side c of the triangle. Calculate the perimeter of the triangle (perimeter = a + b + c).
# ***
side_a = input('Enter side a: ')
side_b = input('Enter side b: ')
side_c = input('Enter side c: ')
perimeter = side_a + side_b + side_c
print('The perimeter of the triangle is ', perimeter)


'''
***
* 6. Get length and width of a rectangle using prompt. Calculate its area (area = length x width) and perimeter (perimeter = 2 x (length + width))
* 7. Get radius of a circle using prompt. Calculate the area (area = pi x r x r) and circumference (c = 2 x pi x r) where pi = 3.14.
* 8. Calculate the slope, x-intercept and y-intercept of y = 2x -2
* 9. Slope is (m = y2-y1/x2-x1). Find the slope between point (2, 2) and point (6,10)
* 10. Compare the slopes in tasks 8 and 9.
* 11. Calculate the value of y (y = x^2 + 6x + 9). Try to use different x values and figure out at what x value y is 0.
* 12. Find the length of 'python' and 'jargon' and make a falsy comparison statement.
* 13. Use and operator to check if 'on' is found in both 'python' and 'jargon'
* 14. I hope this course is not full of jargon. Use in operator to check if jargon is in the sentence.
* 15. There is no 'on' in both dragon and python
* 16. Find the length of the text python and convert the value to float and convert it to string
* 17. Even numbers are divisible by 2 and the remainder is zero. How do you check if a number is even or not using python?
* 18. The floor division of 7 by 3 is equal to the int converted value of 2.7.
* 19. Check if type of '10' is equal to 10
* 20. Check if int('9.8') is equal to 10
***
'''
rectangle_length = 28
rectangle_width = 15
rectangle_area = rectangle_length * rectangle_width
rectangle_perimeter = 2 * (rectangle_length + rectangle_width)
print('rectangle\'s area is ', rectangle_area)
print('rectangle\'s perimeter is ', rectangle_perimeter)

radius = 10
pi = 3.14
circle_area =  pi * (radius ** 2)
circle_circumference = 2 * pi * radius
print('circle\'s area is ', circle_area)
print('circle\'s circumference is ', circle_circumference)

# x-intercept and y-intercept of y = 2x -2
x1 = 2
x2 = 6
y1 = 2
y2 = 10
m = (y2-y1)/(x2-x1)
print('Slope is ', m)
print(len('python') == len('jargon'))
check_contain_item = 'on' in 'dragon' and 'on' in 'python'
print("Check if 'on' is found in both 'python' and 'jargon': ", check_contain_item)
print('Check if jargon is in the sentence: ', 'jargon' in 'I hope this course is not full of jargon')
print('no \'on\' in both dragon and python', check_contain_item)

length = '10'
print(str(float(length)))
number = input('Give me a number: ')
print('Check number is even or not: ', number %2 == 0)
print(7//3 == 2.7)
print('10' == 10)
print(int('9.8') == 10)


# ***
# 21. Writ a script that prompts the user to enter hours and rate per hour. Calculate pay of the person?
# ***
hours = input('Enter hours: ')
hourly_rate = input('Enter rate per hour: ')
print('Your weekly earning is ', hours*hourly_rate)


# ***
# 22. Write a script that prompts the user to enter number of years. 
#     Calculate the number of seconds a person can live. Assume someone lives up to hundred years
# ***
live_in_an_age = input('Enter number of years you have lived: ')
lived_for_seconds = live_in_an_age * 365 * 24 * 60 * 60
print(f'You have lived for {lived_for_seconds} seconds.')


# ***
# 23. Write a python script that displays the following table
# ***
a11 = 1
a12 = 2
a13 = 3
a14 = 4
a15 = 5
print(a11, a11, a11, a11, a11)
print(a12, a11, a12, a12**2, a12**3)
print(a13, a11, a13, a13**2, a13**3)
print(a14, a11, a14, a14**2, a14**3)
print(a15, a11, a15, a15**2, a15**3)
