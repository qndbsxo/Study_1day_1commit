# JavaScript Functions

- JavaScript 함수는 특정 작업을 수행하도록 설계된 코드 블록입니다.
- JavaScript 함수는 "무언가" 이를 호출할 때 실행됩니다.

``` javascript
function myFunction(p1, p2) {
	return p1 * p2; // The function returns the product of p1 and p2
}
```

# JavaScript Function Syntax

- JavaScript 함수는 function 키워드, 이름, 괄호()로 정의됩니다.
- 함수 이름에는 문자, 숫자, 밑줄 및 달러 기호가 포함될 수 있습니다(변수와 동일한 규칙).
- 괄호에는 쉼표로 구분된 매개변수 이름이 포함될 수 있습니다.(파라미터, 파라미터2, ...)
- 함수에 의해 실행될 코드는 중괄호 안에 배치됩니다. {}
  
``` javascript
function name(parameter1, parameter2, parameter3) {
	// code to be executed
}
```

- 함수 매개변수는 함수 정의에서 괄호() 안에 나열됩니다.
- 함수 인수는 호출될 때 함수가 받는 값입니다.
- 함수 내에서 인수(매개변수)는 지역 변수로 작동합니다.
- 함수는 다른 프로그래밍 언어에서 프로시저 또는 서브루틴과 거의 동일합니다.

# 함수 호출

함수 내부의 코드는 "무언가"가 함수를 호출(호출)할 때 실행됩니다.

- 이벤트 발생 시(사용자가 버튼을 클릭했을 때)
- JavaScript 코드에서 호출(호출)될 떄
- 자동(자체 호출)

# 함수 반환

- JavaScript가 return 문에 도달하면 함수 실행이 중지됩니다.
- 함수가 명령문에서 호출된 경우 JavaScript는 호출한 명령문 다음에 코드를 실행하기 위해 "돌아가서" 실행됩니다.

``` javascript
// 두 숫자의 곱을 계산하고 결과를 반환합니다.
let x = myFunction(4, 3); // Function is called, return value will end up in x

function myFuntion(a, b) {
	return a * b; // Function return the product of a and b
}
```

# 왜 함수인가?

- 코드를 재사용할 수 있습니다.
- 코드를 한 번 정의하고 여러 번 사용하십시오.
- 다른 인수와 함께 동일한 코드를 여러 번 사용하여 다른 생성할 수 있습니다.

``` 


