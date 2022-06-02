
```MANDATORY```

# 0-add.py

> Write a program that imports the function def add(a, b): from the file add_0.py and prints the result of the addition 1 + 2 = 3

- You have to use print function with string format to display integers
- You have to assign:
  - the value 1 to a variable called a
  - the value 2 to a variable called b
- You should use those two variables as arguments when calling the functions add and print
  a and b must be defined in 2 different lines: a = 1 and another b = 2
- Your program should print: <a value> + <b value> = <add(a, b) value> followed with a new line
- You can only use the word add_0 once in your code
- You are not allowed to use * for importing or __import__
- Your code should not be executed when imported - by using __import__, like the example below

  
# 1-calculation.py

> Write a program that imports functions from the file calculator_1.py, does some Maths, and prints the result.

- Do not use the function print (with string format to display integers) more than 4 times
- You have to define:
  - the value 10 to a variable a
  - the value 5 to a variable b
- You should use those two variables only, as arguments when calling functions (including print)
a and b must be defined in 2 different lines: a = 10 and another b = 5
- Your program should call each of the imported functions. See example below for format
  the word calculator_1 should be used only once in your file
- You are not allowed to use * for importing or __import__
- Your code should not be executed when imported

  
# 2-args.py

> Write a program that prints the number of and the list of its arguments.

- The output should be:
  - Number of argument(s) followed by argument (if number is one) or arguments (otherwise), followed by
    : (or . if no arguments were passed) followed by
    a new line, followed by (if at least one argument),
    one line per argument:
      - the position of the argument (starting at 1) followed by :, followed by the argument value and a new line
- Your code should not be executed when imported
- The number of elements of argv can be retrieved by using: len(argv)
- You do not have to fully understand lists yet, but imagine that argv can be used just like a C array: you can use an index to walk through it. There are other ways (which will be preferred for future project tasks), if you know them you can use them.

  
# 3-infinite_add.py

> Write a program that prints the result of the addition of all arguments

- The output should be the result of the addition of all arguments, followed by a new line
- You can cast arguments into integers by using int() (you can assume that all arguments can be casted into integers)
- Your code should not be executed when imported
- Last but not least, your program should also handle big numbers.

  
# 4-hidden_discovery.py

> Write a program that prints all the names defined by the compiled module hidden_4.pyc (please download it locally).

- You should print one name per line, in alpha order
- You should print only names that do not start with __
- Your code should not be executed when imported
- Make sure you are running your code in Python3.8.x (hidden_4.pyc has been compiled with this version)

  
# 5-variable_load.py

> Write a program that imports the variable a from the file variable_load_5.py and prints its value.

- You are not allowed to use * for importing or __import__
- Your code should not be executed when imported

  ```ADVANCED```

# 100-my_calculator.py

> Write a program that imports all functions from the file calculator_1.py and handles basic operations.

- Usage: ./100-my_calculator.py a operator b
- If the number of arguments is not 3, your program has to:
- print Usage: ./100-my_calculator.py <a> <operator> <b> followed with a new line
exit with the value 1
- operator can be:
  - + for addition
  - - for subtraction
  - * for multiplication
  - / for division
- If the operator is not one of the above:
  - print Unknown operator. Available operators: +, -, * and / followed with a new line exit with the value 1
- You can cast a and b into integers by using int() (you can assume that all arguments will be castable into integers)
- The result should be printed like this: <a> <operator> <b> = <result>, followed by a new line
- You are not allowed to use * for importing or __import__
- Your code should not be executed when imported

  
# 101-easy_print.py

> Write a program that prints #pythoniscool, followed by a new line, in the standard output.

- Your program should be maximum 2 lines long
- You are not allowed to use print or eval or open or import sys in your file 101-easy_print.py

  
# 102-magic_calculation.py

> Write the Python function def magic_calculation(a, b): that does exactly the same as the following Python bytecode:

```

  3           0 LOAD_CONST               1 (0)
              3 LOAD_CONST               2 (('add', 'sub'))
              6 IMPORT_NAME              0 (magic_calculation_102)
              9 IMPORT_FROM              1 (add)
             12 STORE_FAST               2 (add)
             15 IMPORT_FROM              2 (sub)
             18 STORE_FAST               3 (sub)
             21 POP_TOP

  4          22 LOAD_FAST                0 (a)
             25 LOAD_FAST                1 (b)
             28 COMPARE_OP               0 (<)
             31 POP_JUMP_IF_FALSE       94

  5          34 LOAD_FAST                2 (add)
             37 LOAD_FAST                0 (a)
             40 LOAD_FAST                1 (b)
             43 CALL_FUNCTION            2 (2 positional, 0 keyword pair)
             46 STORE_FAST               4 (c)

  6          49 SETUP_LOOP              38 (to 90)
             52 LOAD_GLOBAL              3 (range)
             55 LOAD_CONST               3 (4)
             58 LOAD_CONST               4 (6)
             61 CALL_FUNCTION            2 (2 positional, 0 keyword pair)
             64 GET_ITER
        >>   65 FOR_ITER                21 (to 89)
             68 STORE_FAST               5 (i)

  7          71 LOAD_FAST                2 (add)
             74 LOAD_FAST                4 (c)
             77 LOAD_FAST                5 (i)
             80 CALL_FUNCTION            2 (2 positional, 0 keyword pair)
             83 STORE_FAST               4 (c)
             86 JUMP_ABSOLUTE           65
        >>   89 POP_BLOCK

  8     >>   90 LOAD_FAST                4 (c)
             93 RETURN_VALUE

 10     >>   94 LOAD_FAST                3 (sub)
             97 LOAD_FAST                0 (a)
            100 LOAD_FAST                1 (b)
            103 CALL_FUNCTION            2 (2 positional, 0 keyword pair)
            106 RETURN_VALUE
            107 LOAD_CONST               0 (None)
            110 RETURN_VALUE
```

  
#  103-fast_alphabet.py
> Write a program that prints the alphabet in uppercase, followed by a new line.

- Your program should be maximum 3 lines long
- You are not allowed to use:
  - any loops
  - any conditional statements
  - str.join()
  - any string literal
  - any system calls