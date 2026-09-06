# Python Loops

A **loop** is used to repeat a block of code multiple times.

## Types of Loops

### 1. For Loop

A `for` loop is used to iterate over a sequence or repeat code a specific number of times.

```python
for i in range(1, 6):
    print(i)

Output:
1
2
3
4
5

2. While Loop

A while loop runs as long as a condition is True.

i = 1

while i <= 5:
    print(i)
    i += 1

range()

range(start, stop) generates numbers from start to stop - 1.

range(1, 6)    # 1 to 5
range(1, 11)   # 1 to 10

Important Loop Keywords
break

Stops the loop immediately.

for i in range(1, 6):
    if i == 3:
        break
    print(i)

continue
Skips the current iteration and continues with the next one.

for i in range(1, 6):
    if i == 3:
        continue
    print(i)

pass
Does nothing. It is used as a placeholder.

for i in range(5):
    pass

Infinite Loop
A loop that never becomes False is called an infinite loop.

Example:

while True:
    print("Hello")

Interview Questions

1. What is a loop?
A loop is used to execute a block of code repeatedly.

2. What are the types of loops in Python?
for loop and while loop.

3. What is the difference between for and while?
for is generally used when iterating over a sequence or known range, while while is used when repetition depends on a condition.

4. What is range()?
range() generates a sequence of numbers.

5. What does break do?
break immediately stops the loop.

6. What does continue do?
continue skips the current iteration and moves to the next iteration.

7. What is an infinite loop?
A loop that continues running because its condition never becomes False.

8. What is the difference between break and continue?
break stops the entire loop, while continue skips only the current iteration.