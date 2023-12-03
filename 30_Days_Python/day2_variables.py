# theory day 1

# Variables in Python
first_name = 'Robin'
last_name = 'Kunz'
country = 'Switzerland'
city = 'Zurich'
age = 30
is_married = False
skills = ['Python']

#another way to structure the data. Using a directory instead of multiple own variables. 
person_info = {
   'firstname':'Asabeneh',
   'lastname':'Yetayeh',
   'country':'Finland',
   'city':'Helsinki'
   }

print(first_name)
print(last_name)
print(city)
print(country)

#print is a developer tool. Not used for showcasing on website LOL

print(len('Hello World!'))

#pasted to see logic
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

#me

print('First Name of the Participant:', first_name)
print('Age:', age, 'years')

#paste

# fav_game = input('Whats your favorite game? ') // ansonsten zweimal drücken bei Run
# print(fav_game)

# ok, I can communicate with the terminal down below lol ^^
# script also doesnt keep the memory

# paste

first_name = 'Asabeneh'     # str
last_name = 'Yetayeh'       # str
country = 'Finland'         # str
city= 'Helsinki'            # str
age = 250                   # int, it is not my real age, don't worry about it

# Printing out types
print(type('Asabeneh'))     # str
print(type(first_name))     # str
print(type(10))             # int
print(type(3.14))           # float
print(type(1 + 1j))         # complex
print(type(True))           # bool
print(type([1, 2, 3, 4]))     # list
print(type({'name':'Asabeneh','age':250, 'is_married':250}))    # dict
print(type((1,2)))                                              # tuple
print(type(zip([1,2],[3,4]))) 

# own

float_number = 4.31

print(type(first_name)) #str
print(type(float_number)) #float

# paste

# int to float
num_int = 12
print('num_int', num_int)         # 10
num_float = float(num_int)
print('num_float:', num_float)   # 10.0

# int to float
num_int = 14
print('num_int:', num_int) # 14
num_float = float(num_int)
print('num_float', num_float)

# float to int
num_float = 12.3
print('num_float', num_float)
num_int = int(num_float)
print('num_int', num_int)

# float to int
gravity = 9.81
print(int(gravity))

# int to str
num_int = 10
print(num_int)
num_str = str(num_int)
print(str(num_int))

# exercises day 2

# 1; done
# 2; Day 2: 30 Days of python programming

first_name = 'Robin'                            # als Variable
last_name = 'Kunz' 
full_name = 'Robin Kunz'
country = 'Switzerland'
city = 'Zurich'
age = int(30)
year = int(2023)
is_married = False
is_true = False
is_light_on = True
person_info = first_name, last_name, country       # als Tuple
person_info = {                                    # als Dictionary / dic
    'first_name': "Robin",
}

print(type(first_name))
print(type(last_name))
print(type(full_name))
print(type(age))
print(type(person_info))

print(len(first_name))
print(len(last_name))

num_one = int(5)
num_two = int(4)

total = num_one + num_two
print('total:', total)

diff = num_one - num_two            # nicht abgerundet, float() wert
print('diff:', diff)

product = num_one * num_two
print(product)

division = num_one / num_two
print(division)

remainder = num_one % num_two
print(remainder)

exp = num_one ** num_two
print(exp)

floor_division = num_one // num_two    # entspricht abgerundetem int() wert
print(floor_division)

area_of_circle = 3.14 * 30
print(area_of_circle)

circum_of_circle = 2 * 3.14159 * 30 
print(circum_of_circle)

first_name = input('Enter your first name: ')
print(first_name)

last_name = input('your last name? ')
print(last_name)