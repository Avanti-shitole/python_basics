Variables & Data Types
1. Variables

A variable stores a value.

name = "Avanti"
age = 22
2. Basic Data Types
Type	Example
int	10
float	10.5
str	"Hello"
bool	True / False
3. Check Data Type

Use type():

age = 22
print(type(age))

Output:

<class 'int'>
4. Type Casting

Changing one data type into another.

age = "22"
age = int(age)

Common functions: int(), float(), str(), bool().

5. Multiple Assignment
name, age = "Avanti", 22
6. Important Rules
Variable names cannot start with a number.
Don't use spaces; use _.
Python is case-sensitive.
Python uses dynamic typing, so you don't need to declare the data type.

Important Interview Questions
Q1. What is a variable?

A variable is a name that refers to a value stored in memory.

Q2. Is Python statically typed or dynamically typed?

Python is dynamically typed. We don't need to declare the variable's data type explicitly.

Example:

x = 10
x = "Python"

The same variable can refer to values of different types.

Q3. What are the basic Python data types?

Some common data types are:

int
float
str
bool

Python also provides collection types such as:

list
tuple
set
dict

We will study these later.

Q4. How do you check the type of a variable?

Using:

type(variable)
Q5. What is type casting?

Type casting is converting a value from one data type to another.

Example:

age = "22"
age = int(age)
Q6. What is the difference between int and float?

int stores whole numbers:

10

float stores decimal numbers:

10.5
Q7. Is Python case-sensitive?

Yes.

name = "Avanti"
Name = "ABC"

name and Name are two different variables.