# 1. Concatenate the string 'Thirty', 'Days', 'Of', 'Python' to a single string, 'Thirty Days Of Python'.
print('Thirty' + 'Days' + 'Of' + 'Python')

# 2. Concatenate the string 'Coding', 'For' , 'All' to a single string, 'Coding For All'.
print('Coding' + 'For' + 'All')

# 3. Declare a variable named company and assign it to an initial value "Coding For All".
company = "Coding For All"

# 4. Print the variable company using _print()_.
print(company)

# 5. Print the length of the company string using _len()_ method and _print()_.
print(len(company))

# 6. Change all the characters to uppercase letters using _upper()_ method.
print(company.upper())

# 7. Change all the characters to lowercase letters using _lower()_ method.
print(company.lower())

# 8. Use capitalize(), title(), swapcase() methods to format the value of the string _Coding For All_.
print(company.capitalize())
print(company.title())
print(company.swapcase())

# 9. Cut(slice) out the first word of _Coding For All_ string.
print(company[7:])

# 10. Check if _Coding For All_ string contains a word Coding using the method index, find or other methods.
print(company.find('or'))

# 11. Replace the word coding in the string 'Coding For All' to Python.
replace_str = company.replace('Coding', 'Python')
print(replace_str)

# 12. Change Python for Everyone to Python for All using the replace method or other methods.
print(replace_str.replace('Python', 'Everyone to Python'))

# 13. Split the string 'Coding For All' using space as the separator (split()) .
print(company.split())

# 14. "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" split the string at the comma.
companys = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print(companys.split(','))

# 15. What is the character at index 0 in the string _Coding For All_.
print(company[0])

# 16. What is the last index of the string _Coding For All_.
print(company[-1])

# 17. What character is at index 10 in "Coding For All" string.
print(company[10])

# 18. Create an acronym or an abbreviation for the name 'Python For Everyone'.
python_str = 'Python For Everyone'
python_str = python_str.split()
print(python_str[0][0] + python_str[1][0] + python_str[2][0])

# 19. Create an acronym or an abbreviation for the name 'Coding For All'.
code_str = 'Coding For All'
codes = code_str.split()
print(codes[0][0] + codes[1][0] + codes[2][0])

# 20. Use index to determine the position of the first occurrence of C in Coding For All.
print(company.index('C'))

# 21. Use index to determine the position of the first occurrence of F in Coding For All.
print(company.index('F'))

# 22. Use rfind to determine the position of the last occurrence of l in Coding For All People.
print(company.rindex('l'))

# 23. Use index or find to find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
sentence = 'You cannot end a sentence with because because because is a conjunction'
print(sentence.index('because'))
print(sentence.find('because'))

# 24. Use rindex to find the position of the last occurrence of the word because in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
print(sentence.rindex('because'))
print(sentence.rfind('because'))

# 25. Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
first = sentence.index('because because because')
last = sentence.rfind('e')
print(sentence[first:last+1])

# 26. Find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
# Ditto

# 27. Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
# Ditto

# 28. Does '\'Coding For All' start with a substring _Coding_?
print(code_str.startswith('Coding'))

# 29. Does 'Coding For All' end with a substring _coding_?
print(code_str.endswith('coding'))

# 30. '&nbsp;&nbsp; Coding For All &nbsp;&nbsp;&nbsp; &nbsp;' &nbsp;, remove the left and right trailing spaces in the given string.
trailing_space_string = '&nbsp;&nbsp; Coding For All &nbsp;&nbsp;&nbsp; &nbsp;'
string = trailing_space_string.replace('&nbsp;', '')
print(string[1:-2])

# 31. Which one of the following variables return True when we use the method isidentifier():
#     - 30DaysOfPython
#     - thirty_days_of_python
print('30DaysOfPython'.isidentifier())
print('thirty_days_of_python'.isidentifier())

# 32. The following list contains the names of some of python libraries: ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']. Join the list with a hash with space string.
python_libraries = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
print(' '.join(['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']))

# 33. Use the new line escape sequence to separate the following sentences.
#     ```py
#     I am enjoying this challenge.
#     I just wonder what is next.
#     ```
print('I am enjoying this challenge.\nI just wonder what is next.')

# 34. Use a tab escape sequence to write the following lines.
#     ```py
#     Name      Age     Country   City
#     Asabeneh  250     Finland   Helsinki
#     ```
print('Name\tAge\tCountry\tCity')
print('Asabeneh\t250\tFinland\tHelsinki')

# 35. Use the string formatting method to display the following:

# ```sh
# radius = 10
# area = 3.14 * radius ** 2
# The area of a circle with radius 10 is 314 meters square.
# ```
radius = 10
area = 3.14 * radius ** 2
print('The area of a circle with radius %d is %.2f meters square.' %(radius, area))

# 36. Make the following using string formatting methods:

# ```sh
# 8 + 6 = 14
# 8 - 6 = 2
# 8 * 6 = 48
# 8 / 6 = 1.33
# 8 % 6 = 2
# 8 // 6 = 1
# 8 ** 6 = 262144
# ```
a = 8
b = 6
print('{} + {} = {}'.format(a, b, a + b))
print('{} - {} = {}'.format(a, b, a - b))
print('{} * {} = {}'.format(a, b, a * b))
print('{} / {} = {:.2f}'.format(a, b, a / b))
print('{} % {} = {}'.format(a, b, a % b))
print('{} // {} = {}'.format(a, b, a // b))
print('{} ** {} = {}'.format(a, b, a ** b))