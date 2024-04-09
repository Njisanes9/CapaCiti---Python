# Python-Week-1
Introduction

Python is a programming language widely used for developing web applications, mobile applications, artificial intelligence and games. Python is known for being easiest to use compared to other programming languages. Python code can be writen on IDEs(Intergrated Development Environment) like Pycharm, Visual Studio Code and Sublime. It can be installed on a machine using the Python.org website.


# Variables and Types

Variables are basic unit of program, they are assigned a value which can store a piece of information temporarily. A variable beginning with a number can not be used, but mostly variables can begin with a lower case letter and have upper case letters or underscores. Unlike other programming languages, in Python a user does not have to specify a variable type, a variable can be declared an then assigned a value, the value assigned can be the one determining the variable type, to learn of the variable type in Python one can use the type(variableName) function and then run the code, after the code has been executed the terminal will return then variable type where there it is an int, char,float or string based on the value you assigned when declaring it.

# Data Structures

Data structures allow the storage of list values in a single variable. Types of data structures are Lists, Tuples, Sets and Dictionaries.

# Operators

Operators are instructions that perform operations on variables and values in Python. They are used to manapulate actions on data, there are Mathematical, Logical and Membership operators. Arithmetic operator is the operator that is used for mathematical calculations, these operators include addition(+), division(/), subtraction(-), and multiplication(*).

Comparison operator evaluate two variables or values and produce a boolean result either true or false.

Logical operators include "and", "or" and "not" can be used on boolean values. The "and" operator returns true only if both operands are true, "or" operator return true if at least one operand is true, "not" operator negates the boolean value it operates on.

Membership operators arenused to check if a number or string exists in a given list or string, "in" and "not in" are examples of logical operators.

# Lists

Lists are data structures that can store multiple values whether strings, intergers or floats. To access values in a list, indexes are used. There is a method called slicing that helps filter values according to index numbers. If one does not want to display other values in the list, they just use slicing to show only the values from a certain index. Lists can be modified using various, this modification includes removing, inserting and appending values in the list. Lists can be declare using a variable that used square brackets [] and have values in inside of it.

# Tuples and Sets

Tuples and sets on not so much different from lists, the only difference is that when defining a tuple, values are defined inside of round brackets, tuples are immutable which means they cannot be modified in any form. When defining a set values are defined inside of curly braces.


# Dictionaries
Like, lists,tuples and sets, dictionaries are data structures for storing a series of values. To define a dictionary we use curly brackets, but the difference between defining a set and a dictionary is that a dictionary has a key and a value. A key a value are separated by  the a colon(:), a key will be on the left side and a value will be on the right.

# List Comprehensions

A list comprehension is an easy way to iterate through a list using a for loop, while also returning a copy of th list you iterating over. It also enables you to filter or apply functions to every item in a list.

# Dictionaries and Comprehension

Comprehension in dictionaries is used the same way it is used in lists, the minor difference is that in dictionaries you specify a key and a value.


# Control Flow

Control flow is a way of making decisions in programming. This can be done by testing using an if stament, if the if the condition is true then the code inside the if statement can be executed but a different decision is made if the condition is false in the if statement, this can be achieved by using an else statement below the if stament. 
There are different types of loops, namely while, do while,for and foreach loop, a for and a while are the most commonly used loops. 


# WEEK 2

# FUNCTIONS

* A function is a basic unit of a program.
* Functions are made of a name and parameters, which are denoted by the def statement.
* A function can be called along with it's parameters to execute it's results.

# *Args

args only works on positional arguments, should there be a key wordm we will get an error that say "unexpected key word argument".

# **Kwargs (Key Word arguments)

These type of arguments when included in a function they print results as a dictionary.

# CLASSES & OBJECTS

A class is an extensible program template for creating objects, providing initial values for state and implementations of behavior.
An object is an instance of class.

# ERROR HANDLING FUNDAMENTALS

Errors are thing we always experience in programming. So an error handling method it used in order to handle errors.
To handle errors we use the try, exception statement to catch the errors that may arrise while coding. There are different error types and python can handle them all either with the "except" key word and return the error encountered. In errror handling, the finally part will always execute regardless of the exception caught on the code.

There 3 types of errors, namely 
* TypeError
* ZeroDivisionError
* Exception error.

# WEEK 3

# USER STORIES
These are usualy scenarios from a user's perspective, emphasizing the user's goal and motivation rather than the application itself.They may be driven by a goal to achieve something specific. User stories focus on who, what and why of achieving a goal.

# USE CASES
A use case is a project planning tool depicting how the user can interact with the system to perform certain tasks and how the system can respond to the user.Use cases focus on the who, what and how of achieving a goal.

# PROJECT REQUIREMENTS

Functional requirements describe what the application shoud or should not do and are written as sentences starting with "the application must" or "the application shall".

Non-functional requirements describe how the application should accomplish its task. They focus qualities like maintainability, reliability and usability.

# ARCHITECTURE

This focuses on how the project will be structured based on the project requirements gathered along with user stories. Classes are created and the databases to store user information.




# DATA ---ANALYTICS

# WEEK 1
# Day 1

# Forces Creating Golden Age of Analytics

* Data
* Storage
* Computing

The role of data analytics is to transform data into actionable insights guiding decision making processes within the organization.

This is involves the following key responsibilities:

* Data Collection and Preparation
* Data Analysis
* Data Visualization and Storytelling
* Decision Support
* Collaboration and Communication
* Continuous Learning and Adaptation

# The Analytics Process

This process involves: 

* Data Acquisition
* Cleaning and Manipulation
* Analysis
* Visualization
* Reporting and Communication
* 
The analytics process is iterative meaning that it is a series of sequential actions, making it more accurate to think of them as a set of interrelated actions that may be revisted frequently while working with a dataset.

# Analytics Techniques

* Descriptive Analytics
* Predictive Analytics
* Prescriptive Analytics

# Machine Learning, Artificial Intelligence, and Deep Learning

Machine learning uses algorithms to discover knowledge in datasets can be applied to make informed decisions about the future.

Machine learning commonly adds value on these cases: 

* Segmentning customers and determining the marketing messages that will appeal to different customer groups.
* Discovering anomalies in system and application logs that may be indicative of a cybersecurity incident.
* Forecasting product sales based on market and environmental conditions.
* Recommending the next movie that a customer might wish to watch based on their past activity and the preferences of similar customers.
* Setting prices for hotel rooms far in advance based on forecasted demand.

# Artificial Intelligence

Includes any type of technique when one is attempting to get a computer system to imitate a human behavior. Though it may not be possible for a modern computer to function at the complex reasoning found in the human mind, one can try mimic some small portions of human behavior and judgement.

# Machine Learning

This is a subset of AI techniques. ML techniques attempt to apply statistics to data problems in an effort to discover new knowledge. In short ML techniques are AI techniques designed to learn.

# Deep Learning

This is a further subdivision of machine learning that uses quite complex techniques, known as neural networks, to discover knowledge in a particular way. It is a highly specialized subfield of ML most commonly used for imae, video and sound analysis.


# Data Governance

Data governance programs ensure that the organization has high-quality data and is able to effectively control that data.



# UNDERSTANDING DATA
# DATA TYPES

To understand data types, it is best first to understad data elements. A data element is an attribute about a person, or thing containing data within a range of values. Data elements also describe characteristics of activities, including orders, transactions and events.

# Tabular Data

It is a data organized into a table, made up of columns and rows. A table represents information about a single topic. The contents of each column contain values for the data element. Each row represents a record of a single instance of the table's topic.

# Structured Data Types

This data is tabular in nature and organized into rows and columns. A spreadsheet is an example of structured data type. Clearly defined column headings make spreadsheets easy to work with and understand. A cell is in s spreadsheed is where a column and a row intersect.

# Character 

The character data type limits data entry to only valid characters.Characters can include alphabets on the keyboard, as well as numbers. Depending on ones needs, multiple data types are available that can enforce character limits.

# Alphanumeric

It is most widely used data type for storing character-nased data. As the name implies, alphanumeric is appropriate when a data element consists of both numbers and letters. This data type is ideal for storing product stock-keeping units (SKUs).It is common in the retail clothing space to have a unique SKU for each item available for sale.

# Strong And Weak Typing

Strong typing is when technology rigidly enforces data types.A database column defined as numeric only accepts numerical values. You will get an error if you attemot to enter characters into a numeric column.

Weak typing loosely enforces data types. Spreadsheets use week typing to help make it easier for people to accompilish their work. Spreadsheets default to an automatic data type and accommodate practically any value. When a person specifies a data type, it is loosely enforced compared to a database. For example, with a numeric spreadsheet cell, the softwae does not stop you from entering and storing characters.


# Unstructured Data Types

Unstructured data is any type of data that does not fit neatly into the tabular model.
Examples of unstructured data include digital images, audio recordings, video recordings and open-ended survey responses. Analyzing unstructured data creates a wealth of information and insight.

# CATEGORIES OF DATA

# Quantitative vs Qualitative Data

Quantitative data consists of numeric values. Data elements whose values come from counting or measuring are quantitative. Quantitative data answers questions like "How many?" and "How much?"

Qualitative consists of frequent text values. Data elements whose values describe characteristics, traits, and attitudes are all qualitative. Qualitative data answers questions like "Why?" and "What?".

# Discrete vs Continuous Data

Numeric data comes in two different froms: discrete and continuous. 

A helpful way to think about discrete data is that it represents masurements that can't be subdivided.
Whole numbers represent descrete data, continuous data typically need a decimal pont.

Qualitative data is discrete, but quantitative data can be either discrete or continuous.

# Categorical Data

Text data with a known, finite number of categories is categorical. When considering an individual data element, it is possible to determine whether or not it is categorical.

# Dimensional Data

Dimensional modeling is an approach to arranging data to facilitate analysis. Dimensional modeling organizes data into fact tables and dimension tables. Fact tables store measurement data that is of interest to a business. Dimensions are tables that contain data about the fact.

# COMMON DATA STRUCTURES





























































































































