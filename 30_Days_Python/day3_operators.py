# theory day 3 (12.03.2023)

print(True)
print('Floating Point Number, gravity', 9.81)
print('Complex number: ', 1 + 1j)
print(3 != 2)
print('a' != 'a')
a = 'Switzerland'
b = 'Germany'
print( 'a != a: ', a != a)
print( 'a != b: ', a != b)
print('3 == 3: ', 3 == 3)

print(len('Nadine') > len('Robin'))

print( 'a is a: ', a is a)

print('Black in Black Swan: ', 'Black' in 'Black Swan')
print('B' in 'Robin')
print('b' in 'Robin')

print(3 > 1 and 2 < 5)
print('not: ', not(3 > 1 and 2 < 5))

# exercises

print(type(int(30)))         # my age
print(type(float(1.87)))    # my height
complex_number = 1 + 1j
print(complex_number)
# base = input('enter base of triangle: ')
# height = input('height base of triangle: ')
# area = 0.5 * int(base) * int(height)
#print('The area of the triangle is: ', int(area))

# 5
# side_a = input('Whats the lenght of the side a? ')
# side_b = input('Whats the lenght of the side b? ')
# side_c = input('Whats the lenght of the side c? ')
# perimeter = side_a + side_b + side_c
# print('The perimeter of the triangle', int(perimeter))

# 6
# length = input('Whats the lenght? ')
# width = input('Whats the width? ')
# perimeter = 2 * int(length) * int(width)
# print('perimeter of the rectangle is: ', perimeter)

#7
# radius = input('radius: ')
# area = float(3.14) * float(radius) ** 2
# print(float(area))

#12
print('12: ', len('python') != len('dragon'))

#13
print('13: ', 'on' in 'python' and 'on' in 'dragon')

#14
print('14: ', 'jargon' in 'I hope this course is not full of jargon')

#15
print('15: ', not('on' in 'python' and 'on' in 'dragon'))

#16
print('16 float: ', float(len('python')))
print('16 int: ', int(len('python')))

#17
#lets check if 10 is an even number via remainder %. If % == 0, then even nr
print('17: ', int(10 % 2) == int(0))

#18
print('18: ', int(7 // 3) == int(2.7))

#19
print('19: ', type('10') == type(10))

#20
print('20: ',int(9.8) == int(10))

# hours = input('How many hours? ')
# rate = input('How much is rate? ')
# earning = int(hours) * int(rate)
# print('Your weekly earning is', earning)

#22
# age = input('How old are you? ')
# time_left = (int(100) - float(age)) * 60 * 60
# print('Congrats - You can live for another', int(time_left), 'seconds')

#23
a = 1
b = 2
c = 3
d = 4
e = 5
print(a, int(1), a, a ** 2, a ** 3)
print(b, int(1), b, b ** 2, b ** 3)
print(c, int(1), c, c ** 2, c ** 3)
print(d, int(1), d, d ** 2, d ** 3)
print(e, int(1), e, e ** 2, e ** 3)