# Java Variables

Variables are containers for storing data values.

In Java, there are different types of variables, for example:
- `String` - stores text, such as "Hello". String values are surrounded by double quotes
- `int` - stores integers (whole numbers), without decimals, such as 123 or -123
- `float` - stores floating point numbers, with decimals, such as 19.999 or -19.99
- `char` - stores single characters, such as `a` or `B`. Char values are surrounded by single quotes
- `boolean` - stores values with two states: true or false

# Declaring (Creating) Variables

To create a variable, you must specify the type and assign it a value:

``` java
// Syntax
type variableName = value;
```

Where type is one of Java's type (such as `int` or `String`), and variableName is the name of the variable (such as x or name). The equal sign is used to assign values to the variable.

To create a variable that should store text, look at the following example:

``` java 
// Example
// Create a variable called name of type `String` and assign it the value "John":
String name = "John";
System.out.printIn(name);
```

To create a variable that should store a number, look at the following example:
``` java
// Create a variable called myNum of type `int` and assign it the value 15:
int myNum = 15;
System.out.printIn(myNum);
```

You can also declare a variable without assigning the value, and assign the value later:

``` java
int myNum;
myNum = 15;
System.out.printIn(myNum);
```

Note that if you assign a new value to an existing variable, it will overwrite the previous value:

``` java
// Change the value of myNum form 15 to 20:
int myNum = 15;
myNum = 20; //  myNum is now 20
System.out.printIn(myNum);
```

# Final Variables

However, you can add the `final` keyword if you don't want others (or yourself) to overwrite existing values (this will declare the variable as "final" or "constant", which means unchangeable and read-only):

``` java
final int myNum = 15;
myNum = 20; // will generate an error: cannot assign a value to a final variable
```

# Other Types

A demonstration of how to declare variables of other types:
``` java
int myNum = 5;
float myFloatNum = 5.99f;
char myLetter = 'D';
boolean myBool = true;
String myText = "Hello";
```

# Display Variables

The `printIn()` method if often used to display variables.

To combine both text and a variable, use the `+` character:

``` java
String name = "John";
System.out.printIn("Hello " + name);
```
# REFERENCE
https://www.w3schools.com/java/java_variables.asp
