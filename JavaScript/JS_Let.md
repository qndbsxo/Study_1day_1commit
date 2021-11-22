# JavaScript Let

- `let` 키워드는 ES6(2015)에서 소개 되었다.
- `let`으로 정의된 변수는 재선언할 수 없습니다.
- `let`으로 정의된 변수는 사용하기 전에 선언되어야 합니다.
- `let`으로 정의된 변수에는 블록 범위가 있습니다.

# 재선언 불가

- `let`으로 정의된 변수는 다시 선언할 수 없습니다.
- 실수로 변수를 다시 선언할 수 없습니다.
  
``` javascript
let x = "John Doe";
let x = 0;
// SyntaxError: 'x' has already been declared
```

`var` 를 통해서는 가능하다.

``` javascript
var x = "John Doe";

var x = 0;
```

# Block Scope

- ES6(2015) 이전에는 JavaScript에 전역 범위와 함수 범위만 있었습니다.
- ES6에는 두 가지 중요한 새 JavaScript 키워드인 let과 const가 도입되었습니다.
- 이 두 키워드는 JavaScript에서 블록 범위를 제공합니다.
- {}블록 내부에 선언된 변수는 블록 외부에서 접근할 수 없습니다.

``` javascript
{
	let x = 2;
}
// x can NOT be used here
```

- var 키워드로 선언된 변수는 블록 범위를 가질 수 없습니다.
- {} 블록 내부에 선언된 변수는 블록 외부에서 접근할 수 있습니다.

``` javascript
{
	var x = 2;
}
// x CAN be used here
```

# 변수 재선언


- var 키워드를 사용하여 변수를 다시 선언하여 문제가 발생할 수 있습니다.
- 블록 내부의 변수를 다시 선언하면 블록 외부의 변수도 다시 선언됩니다.

``` javascript
var x = 10;
// Here x is 10

{
	var x = 2;
	// Here x is 2
}

// Here x is 2
```

- let 키워드를 사용하여 변수를 다시 선언하면 이 문제를 해결할 수 있습니다.
- 블록 내부의 변수를 다시 선언해도 블록 외부의 변수는 다시 선언되지 않습니다.

``` javascript
let x = 10;
// Here x is 10

{
	let x = 2;
	// Here x is 2
}

// Here x is 10
```

# 재선언

