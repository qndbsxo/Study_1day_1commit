# JavaScript Objects Defines

In Javascript, objects are king. If you understand objects. you understand JavaScript

In JavaScript, almost "everything" is an object.

- Booleans can be objects (If defined with the `new` keyword)
- Numbers can be objects (If defined with the `new` keyword)
- String can be objects (If defined with the `new` keyword)
- Dates are always objects
- Maths are always objects
- Regular expressions are always objects
- Arrays are always objects
- Functions are always objects
- Objects are always objects

All JavaScript values, except primitives, are objects

# JavaScript Primitives

A primitive values is value that has no properties or methods.

A primitive date type is data that has a primitive value.

JavaScript defines 5 types of primitive data types:
- `string`
- `number`
- `boolean`
- `null`
- `undefined`

Primitive values are immutable ( they are hardcoded and therefore cannot be changed.)

if x = 3.14, you can changed the value of x. But you cannot change the value of 3.14.

# Objects are Variables

JavaScript variables can contain single values:

``` javascript 
let person = "John Doe";
```

JavaScript variables can also contain many values.

Objects are variables too. But objects can contain many values.

Object values are written as name : value pairs (name and value separated by a colon).

``` javascript 
let person = {firstName:"John", lastName:"Doe", age:50, eyeColor:"blue"};
```

a JavaScript object is a collection of named values

It is a common practice to declare objects with `const` keyword

``` javascript
const person = {firName:"John", lastName:"Doe", age:50, eyeColor:"blue"};
```

# Object Properties

THe named values, In JavaScript objects, are called properties

| Property | Value
---|---
firstName | John
lastName | Doe
age | 50
eyeColor | blue

Objects written as name value pairs are similar to:
- Associative arrays in PHP
- Dictionaries In Python
- Hash tables in C
- Hash maps in Java
- Hashed in Ruby ans Perl


# Object Methods

Methods are actions that can be performed on objects.

Object properties can be both primitive values, other objects, and functions.

An object method is an object property containing a function definition.

Property | Value
--- | ---
firstName | John
lastName | Doe
age | 50
eyeColor | blue
fullName | function() {return this.firstName + ""+this.lastName;}

JavaScript objects are containers for named values, called properties and methods.

# Creating a JavaScript Object

With JavaScript, you can define and create your own objects.

There are different ways to create new objects:
- Create a single object, using an object literal.
- Create a single object, with the keyword `new`.
- Define an object constructor, and the create objects of the constructed type.
- Create an object using `Object.create()`






# REFERENCE
https://www.w3schools.com/js/js_object_definition.asp