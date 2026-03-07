## 1. Data Types

Data types represent the type of value stored in a variable.

Examples:
str → String (text)
int → Integer (whole numbers)
float → Decimal numbers
bool → Boolean (True / False)
NoneType → None (no value)
complex → Complex numbers

## 2. Data Structures

Data structures store collections of data.
## List
Mutable (can change)
my_list = [1, 2, 3]

## Tuple
Immutable (cannot change)
my_tuple = (1, 2, 3)

## Set
Unique values only
my_set = {1, 2, 3}

## Dictionary
Key-value pairs
my_dict = {
"name": "Giorgi",
"age": 25
}

## 3. Comprehensions

List Comprehension
numbers = [x for x in range(5)]

Dictionary Comprehension
squares = {x: x\*x for x in range(5)}

## 4. Assignment Operator
   Used to assign value to variable

x = 10
name = "Giorgi"

## 5. Comparison Operators

Used to compare values.
== equal
!= not equal

> greater
> < smaller
> = greater or equal
> <= smaller or equal

## 6. Built-in Functions

Common Python built-in functions:
int()
float()
str()
type()
print()
list()
round()
len()

## 7. Casting

Casting means converting one data type to another.
Example:
age = "25"
age_int = int(age)
str(10)
float(5)
int("3")

## 8. List Slicing

Used to get part of a list.
numbers = [1,2,3,4,5]

numbers[1:3]

## 9. Modifying Lists

## append()
Adds item to end.
my_list.append(5)

## insert()
Adds item at specific position.
my_list.insert(0, "hello")

## remove()
Removes value.
my_list.remove(2)

## pop()
Removes by index.
my_list.pop()

## Common Errors
| Error | Meaning |
| ------------------ | -------------------------- |
| `SyntaxError` | Python syntax is incorrect |
| `IndentationError` | Wrong indentation |
| `TypeError` | Wrong data type used |

Unlike syntax errors, exceptions can be handled.
x = 10 / 0
ZeroDivisionError
try:
x = 10 / 0
except ZeroDivisionError:
print("You cannot divide by zero")


## Common Exceptions
| Exception | Meaning |
| ------------------- | --------------------------- |
| `ValueError` | Wrong value type |
| `KeyError` | Key not found in dictionary |
| `IndexError` | List index out of range |
| `AttributeError` | Object has no attribute |
| `ZeroDivisionError` | Division by zero |

✔ In simple words

## Error → problem in code structure (program can't run)
## Exception → problem during program execution (can be handled)

💡 Important for Django/backend developers
You will often handle exceptions like:
try:
user = User.objects.get(id=1)
except User.DoesNotExist:
print("User not found")

## Function Parameters

## Positional Arguments
def add(a, b):
return a + b

add(1, 2)

## Keyword Arguments
def greet(message="Hello"):
print(message)

greet(message="Hi")

Rule:

Keyword arguments must come after positional arguments
Example:
my_function(1, 2, name="giorgi")

*args and \*\*kwargs
*args
Allows multiple positional arguments.
def my_function(\*args):
print(args)

my_function(1,2,3,4)

\*\*kwargs
Allows multiple keyword arguments.
def my_function(\*\*kwargs):
print(kwargs)

my_function(name="Giorgi", age=25)

Very Important Python Rule
## Everything in Python is an object.

## Object-Oriented Programming (OOP) in Python

Object-Oriented Programming (OOP) is a programming paradigm where code is organized around objects instead of just functions and logic.
An object represents something with:

Data → attributes (variables)

Behavior → methods (functions)
