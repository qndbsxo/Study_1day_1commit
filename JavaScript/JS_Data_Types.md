# JavaScript Data Types

자바스크립트 변수는 숫자, 문자열, 개체 등 다양한 데이터 유형을 보유할 수  있습니다.

``` javascript
let length = 16; // Number
let lastName = "Johnson"; // String
let x = {firstName:"John", lastName:"Doe"}; // Object
```

# 데이터 타입의 개념

- 프로그래밍에서 데이터 타입은 중요한 개념입니다.
- 변수에 대해 연산을 수행하려면, type에 관해서 아는 것이 중요하다.
- data types 없이 컴퓨터는 이것을 안전하게 해결할 수 없습니다.

``` javascript
let x = 16 + "Volvo";
```

- 16에 "볼보"를 추가하는 것이 의미가 있습니까? 
- 오류가 발생합니까? 아니면 결과가 발생합니까?
- JavaScript는 위의 예를 다음과 같이 처리합니다.

``` javascript
let x = "16" + "Volvo";
```

- 첫 번째 피연사자가 문자열이면 모든 피연산자는 문자열로 처리

# 자바스크립트 Types은 동적이다.

- 자바스크립트는 동적인 타입이다. 
- 같은 변수에 다른 데이터 타입을 포함할 수 있다는 것을 의미합니다.

``` javascript
let x; // Now x is undefined
x = 5; // Now x is a Number
x = "John" // Now x is a String
```

# JavaScript Strings

- 문자열( 또는 텍스트 문자열)은 "John Doe"와 같은 일련의 문자입니다."
- 문자열은 따옴표와 함께 사용됩니다.
- 작은 따옴표, 큰 따옴표 모두 사용 가능합니다.

``` javascript
let carName1 = "Volvo xc60"; // Using double quotes
let carName2 = `Volvo xc60`; // Using single quotes
```


