# JavaScript Date Objects

``` html
<!DOCTYPE html>
<html>
	<body>

		<h2>JavaScript new Date()</h2>

		<p id="demo"></p>

		<script>
			const d = new Date();
			document.getElementId("demo").innerHTML = d;
		</script>
	</body>
</html>
```

# JavaScript Date Output

By default, JavaScript will use the browser`s time zone and display a date as a full text string

You will learn much more about how to display dates, later in this tutorial

# Creating Date Objects

Data objects are created with the `new Date()` constructor.

There are 4 ways to create a new date object:

``` javascript
new Date()
new Date(year, month, day, hours, minutes, seconds, milliseconds)
new Date(date string)
```

# new Date()

`new Date()` creates a new date object with the current date and time:

``` javascript
const d = new Date();
```

``` html
<!DOCTYPE html>
<html>
	<body>

		<h2>JavaScript new Date()</h2>
		<p>Using new Date(), creates a new date object with the current date and time:</p>

		<p id="demo"></p>

		<script>
			const d = new Date();
			document.getElementById("demo").innerHTML = d;
		</script>

	</body>
</html>
```

Date objects are static. The computer time is ticking, but date objects are not.

# new Date(year, month, ...)

`new Date(year, month, ...)` creates a new date object with a specified date and time.

7 numbers specify year, month, day, hour, minute, second, and millisecond (in that order):

``` html
<!DOCTYPE html>
<html>
	<body>

		<h2>JavaScript new Date()</h2>

		<p>Using new Date(7 numbers), creates a new date object with the specified date and time:</p>

		<p id="demo"></p>

		<script>
			const d = new Date(2018, 11, 24, 10, 33, 30, 0);
			document.getElementById("demo").innerHTML = d;
		</script>
	</body>
</html>
```

Note: JavaScript counts months from 0 to 11:
January = 0
December = 11

Specifying a month higher than 11, will not result in an error but add the overflow to the next year:

``` javascript
// Specifying:
const d = new Date(2018, 15, 24, 10, 33, 30);
// Is the same as:
const d = new Date(2019, 3, 24, 10, 33, 30);
```

# Using 6, 4, 3, or 2 Numbers

6 numbers specify year, month, day, hour, minute, second:

``` html
<!DOCTYPE html>
<html>
	<body>

		<h2>JavaScript new Date()</h2>
		<p>6 numbers specify year, month, day, hour, minute and second:</p>

		<p id="demo"></p>

		<script>
			const d = new Date(2018, 11, 24, 10. 33. 30);
			document.getElementById("demo").innerHTML = d;
		</script>
	</body>
</html>
```

5 numbers specify year, month, day, hour, and minute:

``` html
<!DOCTYPE html>
<html>
	<body>

		<h2>JavaScript new Date()</h2>
		<p>5 numbers specify year, month, day, hour, and minute:</p>

		<p id="demo"></p>

		<script>
			const d = new Date(2018, 11, 24, 10, 33);
			document.getElementById("demo").innerHTML = d;
		</script>
	</body>
</html>
```

4 numbers specify year, month, day, and hour:

``` javascript
const d = new Date(2018, 11, 24, 10);
```

3 numbers specify year, month, and day:

``` javascript
const d = new Date(2018, 11, 24);
```

2 numbers specify year and month:

``` javascript
const d = new Date(2018, 11);
```

You cannot omit month. If you supply only one parameter it will be treated as milliseconds.

``` javascript
const d = new Date(2018);
```

# Previous Century

One and two digit years will be interpreted as 19xx:

``` javascript
const d = new Date(99, 11, 24);
```

``` javascript 
const d = new Date(9, 11, 24);
```

# new Date(dateString)

`new Date(dateString)` creates a new date object from a date sting:

``` javascript 
const d = new Date("October 13, 2014 11:13:00");
```

``` html
<!DOCTYPE html>
<html>
	<body>

		<h2>JavaScript new Date()</h2>
		<p>A Date object can be created with a specified date and time:</p>

		<p id="demo"></p>

		<script>
			const d = new Date("October 13, 2014 11:13:00");
			document.getElementById("demo").innerHTML = d;
		</script>
	</body>
</html>
```

# JavaScript Stores Dates as Milliseconds

JavaScript stores dates as number of milliseconds since January 01, 1970, 00:00:00 UTC (Universal Time Coordinated).

Zero time is January 01, 1970 00:00:00 UTC.

Now the time is: 1637999294378 millisecond past January 01, 1970

# new Date(milliseconds)

`new Date(milliseconds)` creates a new date object as zero time plus milliseconds:

``` html
<!DOCTYPE html>
<html>
	<body>

		<h2>JavaScript new Date()</h2>
		<p>Using new Date(milliseconds), creates a new date object as January 1, 1970, 00:00:00 Universal Time (UTC) plus the milliseconds:</p>
		
		<p id="demo"></p>

		<script>
			const d = new Date(0);
			document.getElementById("demo").innerHTML = d;
		</script>

	</body>
</html> 
```

01 January 1970 plus 100 000 000 000 milliseconds is approximately 03 March 1973:

``` javascript
const d = new Date(1000000000000)
```

January 01 1970 minus 100 1000 000 milliseconds is approximately October 31 1966:

``` javascript
const d = new Date(-100000000000)
```

``` html
<!DOCTYPE html>
<html>
	<body>

		<h2>JavaScript new Date()</h2>
		<p>Using new Date(milliseconds), creates a new date object as January 1, 1970, 00:00:00 Universal Time (UTC) plus the milliseconds:</p>

		<p id="demo"></p>

		<script>
			const d = new Date(86400000);
			document.getElementById("demo").innerHTML = d;
		</script>
	</body>
</html>
```

One day (24 hours) is 86 400 000 milliseconds.

# Date Methods 

When a Date object is created, a number of methods allow you to operate on it

Date methods allow you to get and set the year, month, day, hour, minute, second, and millisecond of date objects, using either local time or UTC (universal, or GMT) time.

# Displaying Dates

JavaScript will (by default) output dates in full text string format:

``` html
<!DOCTYPE html>
<html>
	<body>
		
		<h2>JavaScript new Date()</h2>

		<p id="demo"></p>

		<script>
			const d =new Date();
			document.getElementById("demo").innerHTML = d;
		</script>
	</body>
</html>
```

When you display a date object in HTML, it is automatically converted to a string,
with the `toString` method.

``` html
<!DOCTYPE html>
<html>
	<body>

		<h2>JavaScript toString()</h2>
		<p>The toString() method converts a date to a string:</p>

		<p id="demo"></p>

		<script>
			const d = new Date();
			document.getElementById("demo").innerHTML = d.toString();
		</script>
	</body>
</html>
```

# REFERENCE
https://www.w3schools.com/js/js_dates.asp
