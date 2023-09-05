# How to solve a problem:
    # Figure out what the input and its type are
    # Set up a function
    # Figure out what the output and its type are
    # Gather Your Knowledge
    # Gathers Your Constraints (Not always necessary) 
    # Determine a Logical way to solve the problem
        #Write each step out English
        #Write each step out in Python-esse (sudo-code)
    # Invoke and Test Your Function

# DESCRIPTION:
# Write a function that takes a string of parentheses, and determines if the order of the parentheses is valid. The function should return true if the string is valid, and false if it's invalid.

# Examples
# "()"              =>  true
# ")(()))"          =>  false
# "("               =>  false
# "(())((()())())"  =>  true
# Constraints
# 0 <= length of input <= 100

# All inputs will be strings, consisting only of characters ( and ).
# Empty strings are considered balanced (and therefore valid), and will be tested.
# For languages with mutable strings, the inputs should not be mutated.

# Protip: If you are trying to figure out why a string of parentheses is invalid, paste the parentheses into the code editor, and let the code highlighting show you!


# inputs: parentheses, string
# determine if the string is True or False so I must return True or False
# True if parentheses end up closing properly (or are in order) or if string is empty
# False if the parentheses end up closing improperly (or not in order)
# constraints: length of input = 0 - 100, characters are only ( and ), inputs should not be mutated



def parentheses_valid(parentheses):
    
    parentheses_counter = 0
    for x in parentheses:
        if x == "(":
            parentheses_counter += 1
        elif x == ")":
            parentheses_counter -= 1
            if parentheses_counter < 0:
                return False
    if parentheses_counter == 0:
        return True
    else:
        return False

print(parentheses_valid(")()("))