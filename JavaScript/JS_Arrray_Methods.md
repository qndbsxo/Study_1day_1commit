# Converting Arrays to Strings

The JavaScript method `toString()` converts an array to a string of (comma separated) array values.

``` html
<!DOCTYPE html>
<html>
	<body>
		<h2>JavaScript Array Methods</h2>
		<h2>toString()</h2>
		<p>The toString() method returns an array as a comma separated string:</p>

		<p id="demo"></p>

		<script>
			const fruits = ["Banana", "Orange", "Apple", "Mango"];
			document.getElementById("demo").innerHTML = fruits.toString();
		</script>
	</body>
</html>
```

The `join()` method also join all array elements into a string.

It behaves just like `toString()`, but in addition you can specify the separator:

``` javascript
const fruits = ["Banana", "Orange", "Apple", "Mango"];
document.getElementById("demo").innerHTML = fruits.join("*");
```

# Popping and Pushing

When you work with arrays, it is easy to remove elements and add new elements.

This is what pooping and pushing is:

Popping items out of an array, or pushing items into an array.

# Popping

The `pop()` method removes the last element from an array:

``` javascript
const fruits = ["Banana", "Orange", "Apple", "Mango"];
fruits.pop();
```

The `pop()` method returns the value that was "popped out":

``` html
<!DOCTYPE html>
<html>
	<body>

		<h2>JavaScript Array Methods</h2>
		<h2>pop()</h2>
		<p>The pop() method returns the value was "popped out":</p>

		<p id="demo1"></p>
		<p id="demo2"></p>

		<script>
			const fruits = ["Banana", "Orange", "Apple", "Mango"];
			document.getElementById("demo1").innerHTML = fruits.pop();
			document.getElementById("demo2").innerHTML = fruits;
		</script>
	</body>
</html>
```

# Pushing

The `push()` method adds a new element to an array (at the end):

``` html
<!DOCTYPE html>
<html>
	<body>

		<h2>JavaScript Array Methods</h2>
		<h2>push()</h2>
		<p>The push() method appends a new element to an array:</p>

		<p id="demo1"></p>
		<p id="demo2"></p>

		<script>
			const fruits = ["Banana", "Orange", "Apple", "Mango"];
			document.getElementById("demo1").innerHTML = fruits;
			fruits.push("Kiwi");
			document.getElementById("demo2").innerHTML = fruits;
		</script>
	</body>
</html>
```

The `push()` method returns the new array length:

``` javascript
const fruits = ["Banana", "Orange", "Apple", "Mango"];
let length = fruits.push("Kiwi");
```

# Shifting Element

Shifting is equivalent to popping, working on the first element instead of the last.

The `shift()` method removes the first array element and "shifts" all other elements to a lower index.

``` html
<!DOCTYPE html>
<html>
	<body>
		<h2>JavaScript Array Methods</h2>
		<h2>shift()</h2>
		<p>The shift() method removes the first element of an array(and "shifts" the other elements to the left):</p>

		<p id="demo1"></p>
		<p id="demo2"></p>

		<script>
			const fruits = ["Banana", "Orange", "Apple", "Mango"];
			document.getElementById("demo1").innerHTML = fruits;
			fruits.shift();
			document.getElementById("demo2").innerHTML = fruits;
		</script>
	</body>
</html>
```


The `shift()` method returns the value that was "shifted out":
``` javascript 
const fruits = ["Banana", "Orange", "Apple", "Mango"];
let fruit = fruits.shift();
```

The `unshift()` method adds a ne element to an array (at the beginning), and "unshifts" older elements:

``` javascript
const fruits = ["Banana", "Orange", "Apple", "Mango"];
fruits.unshift("Lemon");
```

The `unshift()` method returns the new array length

``` javascript

const fruits = ["Banana", "Orange", "Apple", "Mango"];
fruits.unshift("Lemon");
```

# Changing Elements

Array elements are accessed using their index number:

``` javascript 
const fruits = ["Banana", "Orange", "Apple", "Mango"];
fruits[0] = "Kiwi";
```

The `length` property provides an easy way to append a new element to an array:

``` javascript 
const fruits = ["Banana", "Orange", "Apple", "Mango"];
fruits[fruits.length] = "Kiwi";
```

# Deleting Elements

Array elements can be deleted using the JavaScript operator `delete`.

Using `delete` leaves `undefinded` holes in the array.

Use pop() or shift() instead.

``` javascript
const fruits = ["Banana", "Orange", "Apple", "Mango"]
delete fruits[0];
```

# REFERENCE

https://www.w3schools.com/js/js_array_methods.asp
