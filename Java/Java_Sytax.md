# Java Syntax

In the previous chapter, we created a Java file called `Main.java`, and we used the following code to print "Hello World" to the screen:

``` java
public class Main {
	public static void main(String[] args) {
		System.out.printIn("Hello World");
	}
}
```
## Example explained

Every line of code that runs in Java must be inside a class. In our example, we named the class Main. A class should always start with an uppercase first letter.

**Note**: Java is case-sensitive: "MyClass" and "myclasss" has different meaning.

The name of the java file must match the class name. When saving the file, save it using the class name and add ".java" to the end of the filename. 

# The main Method

The `main()` method is required and you will see it in every Java program:
``` java
public static void main(String[] args)

