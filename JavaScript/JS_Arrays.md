# JavaScript Arrays

An array is special variable, which can hold more than one value:

``` javascript 
const cars = ["Saab", "Volvo", "BMW"];
```

# Why Using an Array?

If you have a list of items ( a list of car names, for example), storing the cars in single variables could look like this:

``` javascript
let car1 = "Saab";
let car2 = "Volvo";
let car3 = "BMW";
```

However, what if you want to loop through the car and find a specific one? And 
what if you had not 3 cars, but 300?

The solution is an array!

An array can hold many values under a single name, and you can access the values by referring to an index number.

# Creating an Array 

Using an array literal is the easiest way to create a JavaScript Array.

Syntax:

``` javascript 
const array_name = [item1, item2, ...];
```

It is a common practice to declare arrays with the `const` keyword.

``` html
<!DOCTYPE html>
<html>
	<body>

		<h2>JavaScript Arrays</h2>

		<p id="demo"></p>

		<script>
			const cars = ["Saab", "Volvo", "BMW"];
			document.getElementById("demo").innerHTML = cars;
		</script>
	</body>
</html>
```

Spaces and line breaks are note important. A declaration can span multiple lines:

``` javascript
const cars = [
  "Saab",
  "Volvo",
  "BMW"
]
```

you can also create an array, and then provide the elements:

``` javascript
const cars = []
cars[0] = "Saab";
cars[1] = "Volvo";
cars[2] = "BMW"
```

# Using the JavaScript Keyword new

the following example also creates an Array, and assign values to ti:

``` javascript
const cars = new Array("Saab", "Volvo", "BMW");
```

The two examples above do exactly the same.
There is no need to use `new Array()`.
For simplicity, readability and execution speed, use the array literal method.

# Accessing Array Elements

you access an array elements by referring to the index number:

``` javascript
const cars = ["Saab", "Volvo", "BMW"];
let car = cars[0];
```

Array indexes start with 0.
[0] is the first element. [1] is the second element.

# Changing an Array Element

This statement changes the value of the first element in `cars`:

``` javascript
cars[0] = "Opel";

```

``` javascript
const cars = ["Saab", "Volvo", "BMW"];
cars[0] = "Opel";
```

# Access the Full Array

With JavaScript, the full array can be accessed by referring to the array name:

``` javascript
const cars = ["Saab", "Volvo", "BMW"];
document.getElementById("demo").innerHTML = cars;
```

# Arrays are Objects

Arrays are a special type of objects. The typeof operator in JavaScript returns "object" for arrays.

But, JavaScript arrays are best described as arrays.

Arrays use numbers to access its  "element". In this example. `person[0]` return John:

``` javascript
// Array:
const person = ["John", "Doe", 46];
```

Object use names to access its "members". In this example, `person.firstName` return John:

``` javascript
// Object
const person = {firstName:"John", lastName:"Doe", age:46};
```

# Array Elements Can Be Objects

JavaScript variables can be objects. Arrays are special kinds of objects.
Because of this, you can have variables of different types in the same Array.
You can have objects in an Array. You can have functions in an Array. You can have arrays in an Array:

``` javascript
myArray[0] = Date.now();
myArray[1] = myFunction;
myArray[2] = myCars;
```

# Array Properties and MEthods 

The real strength of JavaScript array are the build-in array properties and methods:

``` javascript 
cars.length // Return the number of elements
cars.sort() // Sorts the array
```

# The length Property

The `length` property of an array returns the length of an array ( the number of array elements).

``` javascript 
const fruits = ["Banana", "Orange", "Apple", "Mango"]
let length = fruits.length;
```

the `length` property is always one more than the highest array index.

# Accessing the First Array Element

``` javascript
const fruits = ["Banana", "Orange", "Apple", "Mango"]
let fruit = fruits[0]'
```

# Accessing the Last Array Element

``` javascript
const fruits = ["Banana", "Orange", "Apple", "Mango"]
let fruit = fruits[fruits.length - 1];
```

# Looping Array Elements

one way to loop through an array, is using a `for` loop:

``` html
<!DOCTYPE html>
<html>
	<body>
		<h2>JavaScript Arrays</h2>

		<p>The best way to loop through an array is using a standard for loop:</p>

		<p id="demo"></p>

		<script>
			const fruits = ["Banana", "Orange", "Apple", "Mango"];
			let fLen = fruits.length;

			let text = "<ul>";
			for (let i = 0; i <ul fLen; i++) {
				text += "<li>" + fruits[i] + "</li>";
			}
			text += "</ul>";

			document.getElementById("demo").innerHTML = text;
		</script>
	</body>
</html>
```

you can also use the `Array.forEach()` function:

``` html
<!DOCTYPE html>
<html>
	<body>

		<h2>JavaScript Arrays</h2>

		<p>Array.forEach() calls a function for each array element.</p>

		<p id="demo"></p>

		<script>
			const fruits = ["Banana", "Orange", "Apple", "Mango"];

			let text = "<ul>";
			fruits.forEach(myFunction);
			text += "</ul>";
			document.getElementById("demo").innerHTML = text;

			function myFunction(value) {
			  text += "<li>" + value + "</li>";
			}
		</script>
	</body>
</html>
```

#  Adding Array Elments

The easiest way to add a new element to an array is using the `push()` method:

``` html
<!DOCTYPE html>
<html>
	<body>

		<h2>JavaScript Arrays</h2>

		<p>The push method append a new element to an array.</p>

		<button onclick="myFunction()">Try it</button>

		<p id="demo"></p>

		<script>
			const fruits = ["Banana", "Orange", "Apple"];
			document.getElementById("demo").innerHTML = fruits;

			function myFunction() {
			  fruits.push("Lemon");

			  document.getElementById("demo").innerHTML = fruits;
			}
		</script>

	</body>
</html>
```

New element can also be added to an array using the `length` property:

``` html
<!DOCTYPE html>
<html>
	<body>

		<h2>JavaScript Arrays</h2>

		<p>The length property provides an easy way to append new elements to an array without using the push() method.</p>

		<button onclick="myFunction()">Try it</button>

		<p id="demo"></p>

		<script>
			const fruits = ["Banana", "Orange", "Apple"];
			document.getElementById("demo").innerHTML = fruits;

			function myFunction() {
			  fruits[fruits.length] = "Lemon";

			  document.getElementById("demo").innerHTML = fruits;
			}
		</script>
	</body>
</html>
```

인덱스가 높은 요소를 추가하면 배열에 정의되지 않은 "구멍"이 생길 수 있습니다.

``` html
<!DOCTYPE html>
<html>
	<body>

		<h2>JavaScript Arrays</h2>

		<p>Adding elements with high indexes can create undefined "holes" in an array.</p>

		<p id="demo"></p>

		<script>
			const fruits = ["Banana", "Orange", "Apple"];
			fruits[6] = "Lemon";

			let fLen = fruits.length;
			let text = "";
			for (i = 0; i < fLen; i++) {
			  text += fruits[i] + "<br>";
			}

			document.getElementById("demo").innerHTML = text;
		</script>
	</body>
</html>
```

# Associative Arrays

Many programming languages support arrays with named indexes.

Arrays with named indexes are called associative arrays (or hashes).

JavaScript does not support arrays with named indexes.

In JavaScript, arrays always use numbered indexes.

``` html
<!DOCTYPE html>
<html>
	<body>

		<h2>JavaScript Arrays</h2>

		<p id="demo"></p>

		<script>
			const person = [];
			person[0] = "john";
			person[1] = "Doe";
			person[2] = 46;
			document.getElementById("demo").innerHTML = person[0] + " " + person.length;
		</script>
	</body>
</html>
```

If you use named indexes, JavaScript will redefine the array to an object.

After that, some array methods and properties will produce incorrect results.

``` html
<!DOCTYPE html>
<html>
	<body>

		<h2>JavaScript Arrays</h2>

		<p>If you use a named index when accessing an array, JavaScript will redefine the array to a standard object, and some array methods and properties will produce undefined or incorrect results.</p>

		<p id="demo"></p>

		<script>
			const person = []
			person["firstName"] = "John";
			person["lastName"] = "Doe";
			person["age"] = 46;
			document.getElementById("demo").innerHTML = person[0] + " " + person.length;
		</script>
	</body>
</html>
```

# The Difference Between Arrays and Objects

In JavaScript, arrays use numbered indexes.

In JavaScript, objects use named indexes.

Arrays are a special kind of objects, with numbered indexes.

# When to Use Arrays. When to use Objects.

- JavaScript does not support associative arrays.
- You should use objects when you want the element names to be strings(text).
- You should use arrays when you want the element names to be numbers.

# JavaScript new Array()

JavaScript has a built in array constructor `enw Array()`.

But you can safely use `[]` instead.

These two different statements both create a new empty array named points:

``` javascript 
const points = new Array();
const points = [];
```

These two different statements both create a new array containing 6 numbers:

``` javascript 
const points = new Array(40, 100, 1, 5, 25, 10);
const points = [40, 100, 1, 5, 25, 10];
```

``` html
<!DOCTYPE html>
<html>
	<body>

		<h2>JavaScript Arrays</h2>

		<p>Avoid using new Array(), Use [] instead.</p>

		<p id="demo"></p>

		<script>
			// const points = new Array(40, 100, 1, 5, 25, 10);
			const points = [40, 100, 1, 5, 25, 10];
			document.getElementById("demo").innerHTML = points[0];
		</script>
	</body>
</html>
```

The `new` keyword can produce some unexpected result:

``` html
<html>
	<body>

		<h2>JavaScript Arrays</h2>

		<p>Create an Array with three elements.</p>

		<p id="demo">

			<script>
				var points = new Array(40, 100, 1);
				document.getElementById("demo").innerHTML = points;
			</script>
		</p>
	</body>
</html>
```

``` html
<!DOCTYPE html>
<html>
	<body>

		<h2>JavaScript Arrays</h2>

		<p>Create an Array with two elements.</p>

		<p id="demo"></p>

		<script>
			var points = new Array(40, 100);
			document.getElementById("demo").innerHTML = points;
		</script>
	</body>
</html>
```

``` html
<!DOCTYPE html>
<html>
	<body>

		<h2>JavaScript Arrays</h2>

		<p>Avoid using new Array().</p>

		<p id="demo"></p>

		<script>
			var points = new Array(40);
			document.getElementById("demo").innerHTML = points;
		</script>
	</body>
</html>
```

## A Common Error

``` javascript 
const points = [40];
```

is not the same as:

``` javascript 
const points = new Array(40);

// Create an array with one element:
const points = [40];
```

``` html
<!DOCTYPE html>
<html>
	<body>

		<h2>JavaScript Arrays</h2>

		<p>Create an Array with one element.</p>

		<p id="demo"></p>

		<script>
			var points = [40];
			document.getELementById("demo").innerHTML = points;
		</script>
	</body>
</html>
```

``` html
<!DOCTYPE html>
<html>
	<body>

		<h2>JavaScript Arrays</h2>

		<p>Avoid using new Array().</p>

		<p id="demo"></p>

		<script>
			var points = new Array(40);
			document.getElementById("demo").innerHTML = points[0];
		</script>
	</body>
</html>
```

# How to Recognize an Array

A common question is: How do I know if a variable is an array?

The problem is that the JavaScript operator `typeof` return `object`:

``` javascript
const fruits = ["Banana", "Orange", "Apple"];
let type = typeof fruits;
```

``` html
<!DOCTYPE html>
<html>
	<body>

		<h2>JavaScript Arrays</h2>

		<p>The typeof operator, when used on array, return object:</p>

		<p id="demo"></p>

		<script>
			const fruits = ["Banana", "Orange", "Apple", "Mango"];
			document.getElementById("demo").innerHTMl = typeof fruits;
		</script>
	</body>
</html>
```

The typeof operator returns object because a JavaScript array is an object.

## Solution 1:

To solve this problem ECMAscript 5(JavaScript 2009) defined a new method
`Array.isArray()`:

``` html
<!DOCTYPE html>
<html>
	<body>

		<h2>JavaScript Arrays</h2>

		<p id="demo"></p>

		<script>
			const fruits = ["Banana", "Orange", "Apple"];
			document.getElementById("demo").innerHTML = Array.isArray(fruits);
		</script>
	</body>
</html>
```

## Solution 2:

The `instanceof` operator returns true if an object is created by a given constructor:

``` html
<!DOCTYPE html>
<html>
	<body>

		<h2>JavaScript Arrays</h2>

		<p>the instanceof operator returns true when used on an array:</p>

		<p id="demo"></p>

		<script>
			var fruits = ["Banana", "Orange", "Apple"];
			document.getElementById("demo").innerHTML = fruits instanceof Array;
		</script>
	</body>
</html>
```

# REFERENCE
https://www.w3schools.com/js/js_arrays.asp







