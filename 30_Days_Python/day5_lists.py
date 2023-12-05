# 05.12.2023; 3:30h

fruits = ['banana', 'orange', 'mango', 'lemon']                     # list of fruits
vegetables = ['Tomato', 'Potato', 'Cabbage','Onion', 'Carrot']      # list of vegetables
animal_products = ['milk', 'meat', 'butter', 'yoghurt']             # list of animal products
web_techs = ['HTML', 'CSS', 'JS', 'React','Redux', 'Node', 'MongDB'] # list of web technologies
countries = ['Finland', 'Estonia', 'Denmark', 'Sweden', 'Norway']

# Print the lists and its length
print('Fruits:', fruits)
print('Number of fruits:', len(fruits))
print('Vegetables:', vegetables)
print('Number of vegetables:', len(vegetables))
print('Animal products:',animal_products)
print('Number of animal products:', len(animal_products))
print('Web technologies:', web_techs)
print('Number of web technologies:', len(web_techs))
print('Countries:', countries)
print('Number of countries:', len(countries))

# ok so len means how any items in that list
# not like a word

fruits = ['banana', 'orange', 'mango', 'lemon']
first_fruit = fruits[0] # we are accessing the first item using its index
print(first_fruit)      # banana

second_fruit = fruits[1]
print(second_fruit)     # orange

last_fruit = fruits[3]
print(last_fruit) # lemon

# Last index
last_index = len(fruits) - 1
last_fruit = fruits[last_index]


fruits = ['banana', 'orange', 'mango', 'lemon']
first_fruit = fruits[-4]
last_fruit = fruits[-1]
second_last = fruits[-2]

print(first_fruit)      # banana
print(last_fruit)       # lemon
print(second_last)      # mango

print(list(('Apple', 'Samsung')))   # thats with a tuple inside; a bit confusing
print(['Apple', 'Samsung'])         # lists are with []

# so just use [] for lists for now

List = ['item1','item2','item3', 'item4', 'item5']
# List = first_item, second_item, third_item, *rest   # needs to be first the variable
first_item, second_item, third_item, *rest = List
print(first_item)

countries = ['Germany', 'France','Belgium','Sweden','Denmark','Finland','Norway','Iceland','Estonia']

DE, F, Be, *rest = countries
print(DE)
print(countries)

first, second, third,*rest, tenth = [1,2,3,4,5,6,7,8,9,10]

# OR
numbers = [1,2,3,4,5,6,7,8,9,10]
first, second, third, *rest, tenth = numbers
print(first)
print(numbers)
print(tenth)
print(*rest)

Names = ['Julian', 'Mike', 'Leo', 'Muller']
Be, *rest, DE, He = Names
print(Be)
print(DE)
print(He)
print(*rest)

fruits = ['banana', 'orange', 'mango', 'lemon']
print('all', fruits[0::])
print('only 1st: ', fruits[0:2])

print(fruits[-3:-1])
print(fruits[0])                                        # banana
fruits[0] = 'avocado'
print(fruits)                                           # changed to avocado ^^

print('banana' in fruits)
print('avocado' in fruits)

fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.append('apple')
print(fruits)                                           # cool :)!

fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.insert(0, 'apple')
print(fruits)

fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.insert(1, 'apple')
print(fruits)

fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.remove('banana')
print(fruits)

fruits = ['banana', 'orange', 'mango', 'lemon']
# fruits.remove('banana', 'orange', 'mango')            # only delets one at a time
print(fruits)

fruits = ['banana', 'orange', 'mango', 'lemon']
# fruits_to_remove = ['banana', 'orange', 'mango']
# print(fruits.remove(fruits_to_remove))                # doesnt work, too complex for now, move on

print('/')

fruits = ['banana', 'orange', 'mango', 'lemon']
print(fruits.pop())                                     # lemon

fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.pop()
print(fruits)                                           # ['banana', 'orange', 'mango']

# why this different outcome?
# When you call print(fruits.pop()), you're doing two things: removing the last item from the list fruits and printing that item. Since pop() removes the last item, 'lemon' is printed and removed from the list.


fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.pop(1)
print(fruits)                                           # orange is out

fruits = ['banana', 'orange', 'mango', 'lemon']
# del fruits
# print(fruits)                                         # deletes lists at all

fruits = ['banana', 'orange', 'mango', 'lemon']
del fruits[0]                                           # banana is gone
print(fruits)

fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.clear()
print(fruits)                                           # cleares whole list

fruits = ['banana', 'orange', 'mango', 'lemon']
fruits_copy = fruits.copy()
print(fruits_copy)                                      # make copies

fruits_total = fruits + fruits_copy
print(fruits_total)                                     # merge that stuff :)

print('/')

num1 = [0, 1, 2, 3]
print('before', num1)
num2= [4, 5, 6]
num1.extend(num2)
print('after', num1)                                    # add to existing list another list

fruits = ['banana', 'orange', 'mango', 'lemon']
print('before', fruits)
vegetables = ['Tomato', 'Potato', 'Cabbage', 'Onion', 'Carrot']
fruits.extend(vegetables)
print('after', fruits)

print(fruits.count('banana'))                           # counts, cant be empty

print(fruits.index('banana'))                           # index which position

fruits = ['banana', 'orange', 'mango', 'lemon']
print('before', fruits)
fruits.reverse()
print('after', fruits)                                  # reverse the order


fruits = ['banana', 'orange', 'mango', 'lemon']
print('before', fruits)
fruits.sort(reverse=True)
print('after', fruits)      

fruits = ['1', '2', '4', '3']
print('before', fruits)
fruits.sort(reverse=True)
print('after', fruits)                              # so sort is not same as reverse! Its sorts but also changes

# Exercises: Day 5

#1: Declare an empty list
empty_list = list()
print(empty_list)

#2: Declare a list with more than 5 items
list_5_items = [1,2,3,4,5,6]

#3: Find the length of your list
print(list_5_items)
# print(list_5_items.count())                       # use len() instead of conunt()
print(len(list_5_items))                            # count is for specific words

#4: Get the first item, the middle item and the last item of the list
print(list_5_items[0], list_5_items[3], list_5_items[-1])   # my answer

# from gpt
list_5_items = [1,2,3,4,5,6]
fist_item = list_5_items[0]
middle_index = len(list_5_items) // 2               # Use floor division to get an integer index (so in this case 6 / 2 = 3 aka '4')
middle_item = list_5_items[middle_index]
last_item = list_5_items[-1]
print(fist_item, middle_item, last_item)            # smart solution, not hard coded! Finally // in action :D

#5: Declare a list called mixed_data_types, put your(name, age, height, marital status, address)
mixed_data_types = ['Robin Kunz', int(30), int(187)]
print(mixed_data_types)

#6/7: Declare a list variable named it_companies and assign initial values Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon. / Print the list using print()
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple']
print(it_companies)

# This is a single string, where each company name is separated by a comma and a space
company_names = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"

# Using the split() method to split the string into a list at each comma and space
it_companies = company_names.split(", ")

# Now it_companies is a list where each element is one of the company names
print(it_companies)  # This will print the list of company names

# (1) ok so again on my own
names = "Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon"
it_companies = names.split(', ')
print(it_companies)

# (2) lets play a bit
names = "Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon"
it_companies = names.split()        # seperator is different
print(it_companies)             

                                            # compare 1 and 2

                                            # 1 - This correctly splits the string into individual company names
                                            # because the original string has exactly that:
                                            # each company name is followed by a comma and then a space.

                                            # 2 - you're using just a comma as the separator.
                                            # This will split the string at every comma,
                                            # but because there are spaces after the commas in the original string,
                                            # the resulting list will have those spaces
                                            # included in the company names (except for the first one).

                                            # remember: if you want to split use the correct seperator as its in the list

#8: Print the number of companies in the list
print(len(it_companies))

#9: Print the first, middle and last company
it_companies_middle_index = len(it_companies) // 2
print(it_companies[0] + it_companies[it_companies_middle_index] + it_companies[-1])

# nicer with whitespace?
print(it_companies[0], it_companies[it_companies_middle_index], it_companies[-1])

#10: Print the list after modifying one of the companies
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple']
print('before', it_companies)
it_companies[0] = 'Meta'
print('after', it_companies)

#11: Add an IT company to it_companies
# multiple different ways possible w/ insert()
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple']
print('before', it_companies)
it_companies.insert(0, 'Netflix')
print('after', it_companies)

# multiple different ways possible w/ insert()
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple']
print('before', it_companies)
it_companies.insert(0, 'Netflix')
print('after', it_companies)

# multiple different ways possible w/ append()
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple']
print('before', it_companies)
it_companies.append('Netflix')
print('after', it_companies)

#12: Insert an IT company in the middle of the companies list
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple']
print('before', it_companies)
it_companies.insert(2, 'Netflix')
print('after', it_companies)

#13: Change one of the it_companies names to uppercase (IBM excluded!)
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple']
print('before', it_companies)
it_companies[0] = it_companies[0].upper()       
print('after', it_companies)

                                                    # ok I wanted to upper first whole list,
                                                    # but I need to first select one value [0]
                                                    # also I need to tell it_companies[0] that it got updated
                                                    # from Facebook to FACEBOOK


 #14: Join the it_companies with a string '#;  '
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple']
print('before', it_companies)
joined_companies = '# '.join(it_companies)  
print('after', joined_companies)

                                                # not really understanding that... now # is after the word, can it also be before?
                                                # ok, I think I dont get join function

#15: Check if a certain company exists in the it_companies list. '
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple']
print('Facebook' in it_companies)

#16: Sort the list using sort() method
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple']
sorted_companies = it_companies.sort()
print(sorted_companies)                           # doesnt help a lot; I want a list as output
                                                  # The sort() method sorts the list in place, meaning it modifies the original list and returns None. That's why when you try to print the result of it_companies.sort(), you see None.

it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple']
it_companies.sort()                               # first sort, afterwards print
print(it_companies)

#17: Reverse the list in descending order using reverse() method
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple']
it_companies.sort(reverse=True)
print(it_companies)

# OR
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple']
it_companies.reverse()
print(it_companies)

#18: Slice out the first 3 companies from the list
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple']
print(it_companies[0:3])                        # first, check if its only 3 and not 2 or 4 ^^
del it_companies[0:3]
print(it_companies)

#19: Slice out the last 3 companies from the list
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple']
del it_companies[-3:]
print(it_companies)

#20: Slice out the middle IT company or companies from the list
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple']
del it_companies[1:3]
print(it_companies)

#21: Remove the first IT company from the list
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple']
del it_companies[0]
print(it_companies)

# Just saw I mixed up with Slicing out and removing
# Its not the same.
# slicing: does not change the original list; it simply creates a new list based on the specified range
# removing: deleting an element (or elements) from the original list, which changes the original list

#18: Slice out the first 3 companies from the list
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple']
print(it_companies[3:])
#19: Slice out the last 3 companies from the list
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple']
print(it_companies[0:1])
#20: Slice out the middle IT company or companies from the list
print(it_companies[1:3])

#22: Remove the middle IT company or companies from the list
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple']
del it_companies[1:3]
print(it_companies)

#23: Remove the last IT company from the list
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple']
del it_companies[-1:]
print(it_companies)

#24: Remove all IT companies from the list
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple']
it_companies.clear()                    # first clean list, after print. You cant to in same thing?
print(it_companies)

#25: Destroy the IT companies list
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple']
del it_companies

try:                                    # gpt
    print(it_companies)
except NameError:
    print("it_companies does not exist.")

#26: Join the following lists:
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']

joined_list = front_end + back_end
print(joined_list)                  # imo the better alternatives rn

front_end.extend(back_end)
print(front_end)                    # this way Backend List gets added to frontend list; not sure if one wants that

#27: After joining the lists in question 26. Copy the joined list
#    and assign it to a variable full_stack. Then insert Python and SQL after Redux.
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
full_stack = front_end + back_end
print(full_stack)

# Exercises: Level 2
#1: The following is a list of 10 students ages:
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

ages.sort()
print(ages)
print(ages[0], ages[-1])        # Sort the list and find the min and max age. Or even better..

ages_lowest = ages[0]
ages_highest = ages[-1]
print([ages_lowest, ages_highest])

ages.append(ages_lowest)
ages.append(ages_highest)
print(ages)                     # Add the min age and the max age again to the list

ages_middle_index = len(ages) // 2
print(ages_middle_index)
ages_median = ages[ages_middle_index] // 2
print(ages_median)              # Find the median age (one middle item or two middle items divided by two)

ages_average = (sum(ages)) // len(ages)
print(ages_average)             # Find the average age (sum of all items divided by their number )

ages_rages = ages_highest - ages_lowest
print(ages_rages)               # Find the range of the ages (max minus min)

LA = abs(ages_lowest - ages_average)
HA = abs(ages_highest - ages_average)
print([LA, HA])                 # Compare the value of (min - average) and (max - average), use abs() method
                                # min / max would have been better ^^


# Find the middle country(ies) in the countries list
countries = ['Afghanistan', 'Albania', 'Algeria', 'Andorra', 'Angola', 'Antigua and Barbuda', 'Argentina', 'Armenia', 'Australia', 'Austria', 'Azerbaijan', 'Bahamas', 'Bahrain', 'Bangladesh', 'Barbados', 'Belarus', 'Belgium', 'Belize', 'Benin', 'Bhutan', 'Bolivia', 'Bosnia and Herzegovina', 'Botswana', 'Brazil', 'Brunei', 'Bulgaria', 'Burkina Faso', 'Burundi', 'Cambodia', 'Cameroon', 'Canada', 'Cape Verde', 'Central African Republic', 'Chad', 'Chile', 'China', 'Colombi', 'Comoros', 'Congo (Brazzaville)', 'Congo', 'Costa Rica', "Cote d'Ivoire", 'Croatia', 'Cuba', 'Cyprus', 'Czech Republic', 'Denmark', 'Djibouti', 'Dominica', 'Dominican Republic', 'East Timor (Timor Timur)', 'Ecuador', 'Egypt', 'El Salvador', 'Equatorial Guinea', 'Eritrea', 'Estonia', 'Ethiopia', 'Fiji', 'Finland', 'France', 'Gabon', 'Gambia, The', 'Georgia', 'Germany', 'Ghana', 'Greece', 'Grenada', 'Guatemala', 'Guinea', 'Guinea-Bissau', 'Guyana', 'Haiti', 'Honduras', 'Hungary', 'Iceland', 'India', 'Indonesia', 'Iran', 'Iraq', 'Ireland', 'Israel', 'Italy', 'Jamaica', 'Japan', 'Jordan', 'Kazakhstan', 'Kenya', 'Kiribati', 'Korea, North', 'Korea, South', 'Kuwait', 'Kyrgyzstan', 'Laos', 'Latvia', 'Lebanon', 'Lesotho', 'Liberia', 'Libya', 'Liechtenstein', 'Lithuania', 'Luxembourg', 'Macedonia', 'Madagascar', 'Malawi', 'Malaysia', 'Maldives', 'Mali', 'Malta', 'Marshall Islands', 'Mauritania', 'Mauritius', 'Mexico', 'Micronesia', 'Moldova', 'Monaco', 'Mongolia', 'Morocco', 'Mozambique', 'Myanmar', 'Namibia', 'Nauru', 'Nepal', 'Netherlands', 'New Zealand', 'Nicaragua', 'Niger', 'Nigeria', 'Norway', 'Oman', 'Pakistan', 'Palau', 'Panama', 'Papua New Guinea', 'Paraguay', 'Peru', 'Philippines', 'Poland', 'Portugal', 'Qatar', 'Romania', 'Russia', 'Rwanda', 'Saint Kitts and Nevis', 'Saint Lucia', 'Saint Vincent', 'Samoa', 'San Marino', 'Sao Tome and Principe', 'Saudi Arabia', 'Senegal', 'Serbia and Montenegro', 'Seychelles', 'Sierra Leone', 'Singapore', 'Slovakia', 'Slovenia', 'Solomon Islands', 'Somalia', 'South Africa', 'Spain', 'Sri Lanka', 'Sudan', 'Suriname', 'Swaziland', 'Sweden', 'Switzerland', 'Syria', 'Taiwan', 'Tajikistan', 'Tanzania', 'Thailand', 'Togo', 'Tonga', 'Trinidad and Tobago', 'Tunisia', 'Turkey', 'Turkmenistan', 'Tuvalu', 'Uganda', 'Ukraine', 'United Arab Emirates', 'United Kingdom', 'United States', 'Uruguay', 'Uzbekistan', 'Vanuatu', 'Vatican City', 'Venezuela', 'Vietnam', 'Yemen', 'Zambia', 'Zimbabwe']
print(len(countries))
countries_middle_index = len(countries) // 2
print(countries_middle_index)
print(countries[countries_middle_index])

# Divide the countries list into two equal lists if it is even if not one more country for the first half.
countries_left = countries[:countries_middle_index]
countries_right = countries[-countries_middle_index:]
print(countries_left)
print(countries_right)

# ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']. Unpack the first three countries and the rest as scandic countries.
countries = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
c1, c2, c3, *rest = countries
print([c1, c2, c3])

countries_scandic = rest            # learning! Here its just 'rest' without *
print(countries_scandic)

# Wow!!! Finally - that was a though session. Better late then never :D Tomorrow next one