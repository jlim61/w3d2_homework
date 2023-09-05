import re

with open('./user_records.txt') as f:
    data = f.readlines()
    print(data)

# to make user friendly
for line in data:
    print(line)

# brainstorm
# expected output:
# Age: 25, Country: United States
# Age: 30, Country: Canada
# Invalid record
# Invalid record
# Invalid record

# looks like will need 2 groups, age and country.
# age would be [0-9] and country [A-z]
# for not formated, print Invalid record
# need a function that takes in the file name and regex pattern as arguments and prints out result
# that means 2 arguments. also notes that I have to start by making a pattern
# also wants a count added for the number of valid and invalid records so will need to increment a counter

# patterns
# for age, each age is just 2 digits so: [0-9]{2} should cover that. It's any number from 0-9 and says there
# should be 2 numbers minimum.

# for country, it has a capital letter for sure [A-Z] followed by lowercase letters [a-z]+. The plus is added so
# that any string length of lowercase letters are included. however, there are some cases where the country has
# another capital letter and lowercase string (United States). so maybe \s could be added to connect those and
# make everything after the initial pattern optional since not everything will have it.
# country initial draft: [A-Z][a-z]+\s?[A-Z]*[a-z]*
# the * helps make it optional but still grab everything if needed. ? helps that it's 0-1 bceause there should
# not be more than 1 space between the country name

# Groups
# There should be 2 groups, age and country
# re.compile( () () ) - should have 2 parentheses inside the parentheses

# based on the file data and what outputs are valid (based on initial expected outcomes), there is an expected
# structure: first name last name, age, country
# first name = [A-Z][a-z]+ last name = [A-Z][a-z]+, age=[0-9]{2}, country = [A-Z][a-z]+\s?[A-Z]*[a-z]*

# meaning = first name   1 space last name     1 comma    1 space    age    comma  1 space         country
# my guess = [A-Z][a-z]+   \s{1}  [A-Z][a-z]+    ,{1}       \s{1}  [0-9]{2}  ,{1}     \s{1}     [A-Z][a-z]+\s?[A-Z]*[a-z]*
# wrap age and country in () because they are groups


# given data:
# John Doe, 25, United States - expect to see
# Jane Smith, 30, Canada - expect to see
# Invalid data
# John Adams; 45; United Kingdom
# , 20, 
# Megan Brown, 35, Australia - expect to see
# Data not available
# Mike Wilson, , United States
# Sarah Johnson, 40, 
# Paul Clark 50 Germany
# Emily Davis:32:France
# 45, United States
# Invalid Record
# Alex White, 25, 
# , , Germany
# Julia Robinson, 37, South Africa - expect to see
# Fred Thompson; ; United Kingdom
# 24, India
# John Adams : 45 : United Kingdom
# Sarah Johnson,40
# Sarah Johnson 40 

# I expect to see 4 valid results and 18 invalid results


user_record_pattern = re.compile('[A-Z][a-z]+\s{1}[A-Z][a-z]+,{1}\s{1}([0-9]{2}),{1}\s{1}([A-Z][a-z]+\s?[A-Z]*[a-z]*)')

def user_record_func(data_set, pattern):
    valid_counter = 0
    invalid_counter = 1
    for line in data_set:
        result = pattern.match(line)
        if result:
            valid_counter += 1
            print(f'Age: {result.group(1)}, Country: {result.group(2)}')
        else:
            invalid_counter += 1
            print('Invalid record')
    return f'Valid Counter = {valid_counter} : Valid Counter = {invalid_counter}'

print(user_record_func(data, user_record_pattern))