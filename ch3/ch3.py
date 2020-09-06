# 3.1 Function calls
# int(), float() and str() are some example of functions

# 3.2 Math functions
# first import the math module
import math
degrees = 45
radians = degrees / 180.0 * math.pi
result = math.sin(radians)
print(result)

# 3.3 Composition
x = math.exp(math.log(2+1))
print(x)

# 3.4 Adding new functions
# empty parenthese means no arguments


def print_lyrics():

    print("i'm a lumberjack, and i'm ok.")
    print("i sleep all night and i work all day.")


print_lyrics()

# 3.5 Definitions and uses
# Statements inside a function do not run until the function is called
# Execution of function definitons create only function objects

# 3.6 Flow of Execution
# Understanding the order the statements

# 3.7 Parameters and arguments


def print_twice(bruce):

    print(bruce)
    print(bruce)


print_twice('hi')
print_twice(math.cos(math.pi))
print_twice('Spam ' * 3)
michael = 'eric, the half a bee'
print_twice(michael)

# 3.8 Variables and parameters are local
# variables defined inside a function is local
# parameters defined within the function is also local


def cat_twice(part1, part2):
    cat = part1 + part2
    print_twice(cat)


line1 = 'Bing tiddle '
line2 = 'tiddle bang.'
print(cat_twice(line1, line2))

# 3.9 Stack Diagrams
# can be used to track the value of each variable
# - each function is represented by a frame

# 3.10 Fruitful functions and void functions
# fruitful functions - functions that return results
# void functions - perform an action but doesn't return a value

# Exercises
# Ex 1.


def right_justify(s):
    len_s = len(s)
    num_white_spaces = 70 - len_s
    print(' ' * num_white_spaces + s)


right_justify('monty')

# Ex 2.


def do_twice(f, value):
    f(value)
    f(value)


do_twice(print_twice, 'spam')


def do_four(f, value):
    do_twice(f, value)
    do_twice(f, value)

# Ex 3.

def do_twice(f):
    f()
    f()

def do_four(f):
    do_twice(f)
    do_twice(f)

def print_beam():
    print('+ - - - -', end=' ')

def print_post():
    print('|        ', end=' ')

def print_beams():
    do_twice(print_beam)
    print('+')

def print_posts():
    do_twice(print_post)
    print('|')

def print_row():
    print_beams()
    do_four(print_posts)

def print_grid():
    do_twice(print_row)
    print_beams()

print_grid()
