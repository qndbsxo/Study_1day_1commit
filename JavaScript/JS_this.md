# The JavaScript this Keyword

``` javascript
const person = {
	firstName: "John",
	lastName: "Doe",
	id : 5566,
	fullName: function() {
		return this.firstName + " " + this.lastName;
	}
};
```

# What is this?

The JavaScript `this` keyword refers to the object it belongs to.

It has different values depending on where it is used:

- In a method, `this` refers to the owner object.
- Alone, `this` refers to the global object.
- In a function, `this` refers to the global object.
- In a function, in strict mode, `this` is `undefined`
- In an event, `this` refers to the element that received the event.
- Methods like `call()`, and `apply()` can refer `this` to any object.

# this is a Method

In an object method, `this` refers to the `owner` of the method.

In the example on the top of this page, `this` refers to the person object.

The person object is the owner of the fullName method.

``` javascript
fullName: function() {
	return this.firstName + " " + this.lastName;
}
```



# REFERENCE
https://www.w3schools.com/js/js_this.asp

