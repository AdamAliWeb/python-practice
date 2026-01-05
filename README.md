# Python Practice

## ToDo

- Check the lists and tuples methods

## Tips

> / - Float Division; // - Int Division

> int(3.99) -> 3, not 4

> r"" - raw string, will not interpret \n or others

> Python provides a built-in module called re, you have to import re to use it.

> B = A[:] - to clone a list without referencing the original one while modifying the copy one.

> help(list/tuple) - to output the methods you can use on lists/tuples

> del(A[index]) - to delete an element from a list

> element in DICT returns a boolean if the element is on the dict

| Special Sequence | Meaning                                                                | Example                                                                   |
| ---------------- | ---------------------------------------------------------------------- | ------------------------------------------------------------------------- |
| \d               | Matches any digit character (0-9)                                      | "123" matches "\d\d\d"                                                    |
| \D               | Matches any non-digit character                                        | "hello" matches "\D\D\D\D\D"                                              |
| \w               | Matches any word character (a-z, A-Z, 0-9, and \_)                     | "hello_world" matches "\w\w\w\w\w\w\w\w\w\w\w"                            |
| \W               | Matches any non-word character                                         | "@#$%" matches "\W\W\W\W"                                                 |
| \s               | Matches any whitespace character (space, tab, newline, etc.)           | "hello world" matches "\w\w\w\w\w\s\w\w\w\w\w"                            |
| \S               | Matches any non-whitespace character                                   | "hello_world" matches "\S\S\S\S\S\S\S\S\S\S\S"                            |
| \b               | Matches the boundary between a word character and a non-word character | "cat" matches "\bcat\b" in "The cat sat on the mat"                       |
| \B               | Matches any position that is not a word boundary                       | "cat" matches "\Bcat\B" in "category" but not in "The cat sat on the mat" |

|

- Python can distinguish among data types such as integers, floats, strings, and Booleans.

- Integers are whole numbers that can be positive or negative.

- Floats are numbers that have decimal points; they can represent whole or fractional values.

- You can convert integers to floats using typecasting and vice-versa.

- You can convert integers and floats to strings.

- You can convert an integer or float to a Boolean: 0 becomes False, non-zero becomes True.

- Expressions in Python are a combination of values and operations used to produce a single result.

- Expressions perform mathematical operations such as addition, subtraction, multiplication, and so on.

- We can use // to perform integer division, which results in an integer value by discarding the fractional part.

- Python follows the order of operations (BODMAS) to perform operations with multiple expressions.

- Variables store and manipulate data, allowing you to access and modify values throughout your code.

- The assignment operator "=" assigns a value to a variable.

- Assigning another value to the same variable overrides the previous value of that variable.

- You can perform mathematical operations on variables using the same or different variables.

- Modifying the value of one variable will affect other variables only if they reference the same mutable object.

- Python string operations involve manipulating text data using tasks such as indexing, concatenation, slicing, and formatting.

- A string is usually written within double quotes or single quotes, including letters, white space, digits, or special characters.

- A string can be assigned to a variable and is an ordered sequence of characters.

- Characters in a string identify their index numbers, which can be positive or negative.

- Strings are sequences that support operations like indexing and slicing.

- You can input a stride value to perform slicing while operating on a string.

- Operations like concatenation and replication produce new strings, while finding the length of a string returns a number.

- You cannot modify an existing string; they are immutable.

- You can use escape sequences with a backslash (\) to change the layout of a string. (For example, \n for a new line, \t for a tab, and \\ for a backslash, etc.)

- In Python, you perform tasks such as searching, modifying, and formatting text data with its pre-built string methods.

- You apply a method to a string to change its value, resulting in another string.

- You can perform actions such as changing the case of characters in a string, replacing items in a string, finding items in a string, and so on using pre-built string methods.
