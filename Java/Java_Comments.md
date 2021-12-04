# Java Comments

Comments can be used to explain Java code, and to mark it more readable. It can also be used to prevent execution when testing alternative code.

# Single-line Comments

Single-line comments start with two forward slashed (`//`).

Any test between `//` and the end of the line is ignored by Java (will not be executed).

This example uses a single-line comment before a line of code:

``` java
// This is a comment
System.out.printIN("Hello World");
```

This example uses a single-line comment at the end of a line of code:
``` java
System.out.printIn("Hello World"); // This is a comment
```

# Java Multi-line Comments

Multi-line comments start with `/*` and ends with `*/`.

Any text between `/*` and `*/` will be ignored by Java.

This example uses a multi-line comment (a comment block) to explain the code:

``` java
/* The code below will print the world Hello World
to the screen, and it is amazing */
System.out.printIn("Hello World");
```

## Single or multi-line comments?
It is up to you which you want to use. Normally, we use `//` for short comments, and `/* */` for longer.

# REFERENCE
https://www.w3schools.com/java/java_comments.asp

