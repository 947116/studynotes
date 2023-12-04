# Todays topic: Strings, Concatenation, Escape Sequences, Formatting, Methods

# Monday, 04.12.2023 with 3:30h

sentence = "I hope you are enjoying 30 days of Python Challenge"
print(sentence)
print(len(sentence))

sentence_long = '''I am a super super long sentence
please use me for a long long
long long time'''
print(sentence_long)

''' dont get it fully why we need multiline strings.
for docstrings - they way I am using that right now -
'''

full_text = sentence + sentence_long
print(full_text)

sentence_n = 'I am linebreak now\nnow on another page'
print(sentence_n)

print('left\tright')

print('Backlash: \\')

print('\'This text has doppelzeichen\'')        #works w/ both ' & ""


name = 'Robin'
print('Hello, %s!' % name)

benutzernamen = 'Robin'
logins = 5
bericht = 'Der Benutzer %s hat sich heute %d mal eingelogt.'
print(bericht % (benutzernamen, logins))

Price = 49.99
Article = '\'Rote Schuhe\''                     # \' for 'X'
Rechnung = 'Der Artikel %s kostet CHF %.2f.'    # .2 for decimals
print(Rechnung % (Article, Price))

# f-string once most popular / powerfull

a = 4
b = 3

print(f'{a} + {b} = {a + b}')       # f-string

a = 4
b = 3
result = a + b
print(a, '+', b, '=', result)       # without any formatting
                                    #looks way better with f-strings


# Python Strings as Sequences of Characters / hard to understand rn
# for practical examples its rather with lists etc. Theory example a bit stupid
# more real:

coordinates = (39, 42, 81)
x, y, z = coordinates
print(f'Coordinates: x: {x}, y: {y}, z: {z}')

user_data = ['robinkunz', 'sdfjkjWZuoas!923lkdsad']
username, password = user_data
print(f'Your credentials:, u: {username}, pw: {password}')

user_data = ['robinkunz', 'sdfjkjWZuoas!923lkdsad']
user_data = username, password                                  # possible on both sides? yes!
print(f'Your credentials:, u: {username}, pw: {password}')

some_random_variable = 'Robin'[0]
print(some_random_variable)
print('Robin'[0])

print('Robin'[-1])
print('Robin'[-5])

print('Robin'[0:3])
print('Robin'[-5:])     # no 0, just leave it empthy

print('Haha nice, well how is that?!'[::-1])

print('robin'.capitalize())     # dont need an argument, confusing
print('robin'.count('n'))       # needs argument

print('Robin'.isdecimal())
print('Robin32'.isdigit())
print('32'.isdigit())

web_tech = ['HTML', 'CSS', 'JavaScript', 'React']
result = ' '.join(web_tech)
print(result) # 'HTML CSS JavaScript React'

username = 'Robin Skywalker'
print(username.replace('Robin', 'Luke'))

print('Robin'.swapcase())

# exercises

web_tech = ['HTML', 'CSS', 'JavaScript', 'React']
result = ' '.join(web_tech)
print(result) # 'HTML CSS JavaScript React'

class_name = ['Thirty', 'Days', 'Of', 'Python']
print(' '.join(class_name))                     # version 1
print('Thirty' + 'Days' + 'Of' + 'Python')      # version 2 (add some ' ')
print('Thirty', 'Days', 'Of', 'Python')         # version 3

# take version 2&3 for easier stuff, for bigger use join function
# or depending on team styling guides

moto = ['Coding', 'For' , 'All']
print('Coding', 'For' , 'All')
print(' '.join(moto))
print('Coding' + 'For' + 'All')                 # again, add space manually

company = 'Coding For All'

print(company)

print('Lenght of', company, 'is:', len(company))
print(f'Lenght of "{company}" is: {len(company)}')  # for ' ' around company

print('Hello "very strange" person')        # there're " and ' to use both!

print(company.upper())

print(company.lower())

print(company.capitalize())
print(company.title())
print(company.swapcase())

print('Coding For All'[7::])

print('Coding For All'.find('Coding'))      # my first draft, but could be better

if 'Coding For All'.find('Coding') != -1:   # wow, awesome! Remember "!= -1"
    print(True)
else:
    print(False)


if 'Coding' in 'Coding For All':            # Version 1; Like that a lot!
    print(True)
else:
    print(False)

print(company.replace('Coding', 'Python'))

print(company.split())

print('Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon'.split()) # doesnt look nice; commas need to be gone
print('Facebook Google Microsoft Apple IBM Oracle Amazon'.split())          # no commas, but not auto
print('Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon'.split(', '))    # ouh nice!

data = "Name:Max;Alter:22;Stadt:Berlin"
attributes = data.split(';')
print(attributes)

s = "abc--def--ghi"
parts = s.split('--')
print(parts)  # ['abc', 'def', 'ghi']

s = "apple-orange-banana-tomato"            # Maximale Anzahl an Trennungen
limited = s.split('-', 2)
print(limited)

company = 'Coding For All'
print(company[-1])

#17

print(company[9])

print('Python For Everyone'[0:7:11])        # my 1st trial; only P gets shown

# Erstellen eines Akronyms in Python        # chatgpt, very smart!!
phrase = "Python For Everyone"
acronym = ''.join(word[0] for word in phrase.split()).upper()
print(acronym)

phrase = 'Python For Everyone'
print(phrase.split())

print(''.join(word[0] for word in phrase.split()).upper())

#20
print(company.index('C'))

print('Coding For All People'.rfind('l'))

phrase = 'You cannot end a sentence with because because because is a conjunction'
print(phrase.index('because'))
print(phrase.rindex('because'))
print(phrase[0:31:47])

# I've problems with slicing; lets recap

s = "Python"
pto = s[0:6:2]          # 'Pto', überspringt jeden zweiten Buchstaben
print(pto)

# ok so max 2 are possible; the 3rd one is 2nd etc.

print(phrase[0:31] + phrase[47:])       # nice!!

# 28



if print('Coding For All'.find('Coding')) != 0:
    print('True, the word is there :)')
else:
    print(False)


if print('Coding For All'.rfind('Coding')) != 0:    #rfind for last one
    print('True, the word is on the end :)')
else:
    print('Nope :(')

phrase = '   Coding For All      '
phrase_left = phrase.find('Coding')
print(phrase_left)
phrase_right = phrase.rfind('Coding')
print(phrase_right)
print(phrase[phrase_left:phrase_right])

print(phrase.strip())           # super easy once strip is exactly the function to delete white space ^^


phrase = ' Coding For All '
phrase_left = phrase.find('Coding')  # Findet den Startindex von 'Coding'
print(phrase_left)
print(phrase_right)
phrase_right = phrase.rfind('Coding') - len('Coding')  # Findet das Ende von 'Coding'
print(phrase[phrase_left:phrase_right])  # Sollte 'Coding' ausgeben

# ok now I got it, what's rfind really is!


# Gegeben ist ein String mit zusätzlichen Leerzeichen
phrase = ' Coding For All '

# Findet den Startindex des ersten Vorkommens von 'Coding'
phrase_left = phrase.find('Coding')

# Findet den Startindex des letzten Vorkommens von 'Coding' und addiert die Länge von 'Coding',
# um den Endindex zu erhalten
phrase_right = phrase.rfind('Coding') + len('Coding')

# Extrahiert den Substring von phrase_left bis phrase_right
# Da phrase_right das Ende von 'Coding' ist, müssen wir noch den Rest des Strings hinzufügen.
# Dazu addieren wir den Teil des Strings nach phrase_right
extracted_phrase = phrase[phrase_left:phrase_right] + phrase[phrase_right:]

print(extracted_phrase)
print(phrase_right)

# 31
print('30DaysOfPython'.isidentifier())
print('thirty_days_of_python'.isidentifier())

# 32
list = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
joined_list = ' # '.join(list)
print(joined_list)

    # why to do that? Reports, URL, Compatibilitly etc.

# 33
print('I am enjoying this challenge.\nI just wonder what is next.')

# 34
print('Name\tAge\tCountry\tCity\nAsabeneh\t250\tFinland\tHelsinki')

# 35
radius = 10
area = 3.14 * radius ** 2
    # The area of a circle with radius 10 is 314 meters square.
print(f' The area of a circle with radius {radius} is {int(area)} meters square')

# 36
a = 8
b = 6
print(f'{a} + {b} = {a + b}')
print(f'{a} - {b} = {a - b}')
print(f'{a} * {b} = {a * b}')
print(f'{a} / {b} = {a / b}')
print(f'{a} % {b} = {a % b}')
print(f'{a} // {b} = {a // b}')
print(f'{a} ** {b} = {a ** b}')

# finally :))! That was a though one! But intersting!