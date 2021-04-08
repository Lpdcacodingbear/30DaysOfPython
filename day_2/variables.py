# Variables in Python

first_name = 'Goku'
last_name = 'Sun'
country = 'Wakusei'
city = 'bejīta'
age = 250
is_married = True
skills = ['HTML', 'CSS', 'JS', 'React', 'Python']
person_info = {
    'firstname':'Goku', 
    'lastname':'Sun', 
    'country':'Wakusei',
    'city':'bejīta'
    }

# Printing the values stored in the variables

print('First name:', first_name)
print('First name length:', len(first_name))
print('Last name: ', last_name)
print('Last name length: ', len(last_name))
print('Country: ', country)
print('City: ', city)
print('Age: ', age)
print('Married: ', is_married)
print('Skills: ', skills)
print('Person information: ', person_info)

# Printing the type of the values stored in the variables

print(type(first_name))
print(type(last_name))
print(type(country))
print(type(city))
print(type(age))
print(type(is_married))
print(type(skills))
print(type(person_info))

# Compare the length of your first name and your last name
print(max(len(first_name), len(last_name)))

'''
Declare 5 as num_one and 4 as num_two

Add num_one and num_two and assign the value to a variable _total
Subtract num_two from num_one and assign the value to a variable _diff
Multiply num_two and num_one and assign the value to a variable _product
Divide num_one by num_two and assign the value to a variable _division
Use modulus division to find num_two divided by num_one and assign the value to a variable _remainder
Calculate num_one to the power of num_two and assign the value to a variable _exp
Find floor division of num_one by num_two and assign the value to a variable _floor_division
'''

num_one = 5
num_two = 4
_total = num_one + num_two
_diff = num_one +-num_two
_product = num_one * num_two
_division = num_one / num_two
_remainder = num_one % num_two
_exp = num_one ** num_two
_floor_division = num_one // num_two

'''
The radius of a circle is 30 meters.

Calculate the area of a circle and assign the value to a variable area_of_circle
Calculate the circumference of a circle and assign the value to a variable circum_of_circle
Take radius as user input and calculate the area.
'''

pi = 3.14
radius = 30
area_of_circle = pi * (radius ** 2)
print(area_of_circle)
circum_of_circle = 2 * pi * radius
print(circum_of_circle)
radius_as_user_input = input('How long about radius?')
area_of_circle_as_user_input = pi * (int(radius_as_user_input) ** 2)
print(area_of_circle_as_user_input)

# Use the built-in input function to get first name, last name, country and age from a user and store the value to their corresponding variable names

first_name_as_user_input = input('What is your first name?')
last_name_as_user_input = input('What is your last name?')
country_as_user_input = input('Where are you from?')
age_as_user_input = input('How old are you?')
