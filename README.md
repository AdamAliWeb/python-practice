# Python Practice

## ToDo

- Check the lists and tuples methods

- Check a proper pandas documentation or cheat sheet

## Tips

> / - Float Division; // - Int Division

> int(3.99) -> 3, not 4

> r"" - raw string, will not interpret \n or others

> Python provides a built-in module called re for regular expressions, you have to import re to use it.

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

## Python Basics

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

## File Reading

Python uses the open() function and allows you to read and write files, providing access to the content within the file for reading. It also allows overwriting it for writing and specifies the file mode (for example, r for reading, w for writing, a for appending).

- To read a file, Python uses an open function along with r.

- Python uses the open with function to read and process a file attribute, that is, from open to close.

- In Python, you use the open method to edit or overwrite a file.

- To write a file, Python uses the open function along with w.

- In Python, "a" indicates that the program has appended to the file.

- In Python, “\n” signifies that the code should start on a new line.

- Python uses various methods to print lines from attributes.

## APIs and Data Collection

Simple APIs in Python are application programming interfaces that provide straightforward and easy-to-use methods for interacting with services, libraries, or data, often with minimal configuration or complexity.

- An API lets two pieces of software talk to each other.

- Using an API library in Python entails importing the library, calling its functions or methods to make HTTP requests, and parsing the responses to access data or services provided by the API.

- Pandas API processes the data by communicating with the other software components.

- An Instance forms when you create a dictionary and then use the DataFrames constructor to create a Pandas object.

- Method “head()” will display the mentioned number of rows from the top (default 5) of DataFrames, while method “mean()” will calculate the mean and return the values

Rest APIs allow you to communicate through the internet, taking advantage of resources like storage, access more data, AI algorithms, and so on.

- HTTP methods transmit data over the internet.

- An HTTP message typically includes a JSON file with instructions for operations.

- HTTP messages containing JSON files are returned to the client as a response from web services.

- Dealing with time series data involves using the Pandas time series function.

- You can get data for daily candlesticks and plot the chart using Plotly with the candlestick plot.

The HTTP (HyperText Transfer Protocol) transfers data, including web pages and resources, between a client (a web browser) and a server on the World Wide Web.

- The HTTP protocol is commonly used for implementing various types of REST APIs.

- An HTTP response includes information like the type of resource, length of resource, and so on

- Uniform resource locator (URL) is the most popular way to find resources on the web.

- URL is divided into three parts: scheme, internet address or base URL, and route

- The GET method is one of the popular methods of requesting information. Some other methods may also include the body.

- Response method contains the version and body of the response.

- POST submits data to the server, PUT updates data already on the server, DELETE deletes data from the server

Requests is a Python library that allows you to send HTTP/1.1 requests easily

- You can modify the results of your query with the GET method.

- You can obtain multiple requests from a URL like name, ID, and so on with a Query string.

Web scraping in Python involves extracting and parsing data from websites to gather information for various applications, using libraries like Beautiful Soup and requests.

- HTML comprises text surrounded by blue text elements enclosed in angular brackets called tags.

- You can select an HTML element on a web page to inspect the webpage.

- Web pages may also contain CSS and JavaScript along with HTML elements.

- Each HTML document is like an HTML Tree, which may contain strings and other tags.

- Each HTML table is comprised of table tags and is structured with elements such as rows, headers, body and so on.

Tabular data can also be extracted from web pages using the `read_html` method in Pandas.

Beautiful Soup in Python is a library for parsing and navigating HTML and XML documents, making extracting, and manipulating data from web pages more accessible.

To parse a document, pass it through the Beautiful Soup constructor to get a beautiful soup object representing the document as a nested data structure.

Beautiful soup represents HTML as a set of tree-like objects with methods to parse the HTML.

Navigable string is like a Python string that supports beautiful soup functionality.

find_all is a method used to extract content based on the tag’s name, its attributes, the text of a string, or some combination of these.

The find_all method looks through a tag’s descendants and retrieves all descendants that match your filters.

The result is a Python iterable like a list.

File formats refer to the specific structure and encoding rules used to store and represent data in files, such as .txt for plain text or .csv for comma-separated values.

Python works with different file formats such as CSV, XML, JSON, xlsx, and so on

The extension of a file name will let you know what type of file it is and what it needs to open with.

To access data from CSV files, we can use Python libraries such as Pandas.

Similarly, different methods help parse JSON, XML, and other files.
