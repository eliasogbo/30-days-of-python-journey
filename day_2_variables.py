
# 'Day 2: 30 Days of python programming'
first_name = 'Elias'
last_name = 'Ogbo'
full_name = (first_name + ' ' + last_name) # decided to do it this way hehe
country = 'Nigeria'
city = 'Port-Harcourt'
age = 18
year = 2026
is_married = False
is_true = True
is_light_on = False # It's really dark in here
first_name, last_name, country, city, age, year = 'Elias', 'Ogbo', 'Nigeria', 'Port-Harcourt', 18, 2026

# Checking the variable types
print(type(first_name))
print(type(last_name))
print(type(full_name))
print(type(country))
print(type(city))
print(type(age))
print(type(year))
print(type(is_married))
print(type(is_true))
print(type(is_light_on))

print(len(first_name))
print(len(first_name) > len(last_name)) # This is what I thought of when the exercise said to compare the length

num_one = 5
num_two = 4
total = num_one + num_two
print(total)
diff = num_one - num_two
print(diff)
product = num_one * num_two
print(product)
division = num_one / num_two
print(division)
remainder = num_one % num_two
print(remainder)
exp = num_one ** num_two
print(exp)
floor_division = num_one // num_two
print(floor_division)

radius = 30
pi = 3.14
area_of_circle = pi * (radius ** 2)
print(area_of_circle)

circum_of_circle = 2 * pi * radius
print(circum_of_circle)

first_name = input('What is your first name: ')
last_name = input('What is your last name: ')
country = input('What is your country: ')
age = input('What is your age: ')

print('First Name:', first_name)
print('Last Name:', last_name)
print('Country:', country)
print('age:', age)

help('keywords')