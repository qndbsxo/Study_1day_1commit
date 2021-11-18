# JavaScript Syntax

자바스크립트 구문은 자바스크립트 프로그램이 구성되는 규칙의 집합입니다.

``` javascript 
// How to create variables:
var x;
let y;

// How to use variables:
x = 5;
y = 6;
let z = x + y;
```

# JavaScript Values

자바스크립트 구믄은 두 가지 유형의 값을 정의합니다.
  
- Fixed values
- Variable values
- 고정된 값을 Literals라고 합니다.
- 변수 값을 변수라고 합니다.

# JavaScript Literals

고정 값에 대한 가장 중요한 두 가지 구문 규칙은 다음과 같습니다.:

1. 숫자는 소수점 유무에 관계없이 작성됩니다.

``` html
<!DOCTYPE html>
<html>
	<body>

		<h2>JavaScript Numbers</h2>

		<p>Number can be written with or without decimals.</p>

		<p id="demo"></p>

		<script>
			document.getElementById("demo").innerHTML = 10.50;
		</script>
	</body>
</html>
```

2. 문자열은 큰 따옴표 또는 작은 따옴표로 묶인 텍스트입니다.

``` html
<!DOCTYPE html>
<html>
	<body>

		<h2>JavaScript Strings</h2>

		<p>Strings can be written with double or single quotes.</p>
		<p id="demo"></p>

		<script>
			document.getElementById("demo").innerHTML = 'John Doe';
		</script>
	</body>
</html>
```

# JavaScript 변수

- 프로그래밍 언어에서 변수는 데이터 값을 저장하기 위해서 사용됩니다.
- 자바스크립트는 변수를 선언하기 위해 `var`, `let` 그리고 `const` 키워드를 사용합니다.
- 등호는 변수에 값을 할당하는 데 사용됩니다.
- 이 예에서 x는 변수로 정의됩니다. 
- 그런 다음 x에 값이 6이 할당됩니다.

``` html
<!DOCTYPE html>
<html>
	<body>

		<h2>JavaScript Variables</h2>

		<p>In this example, x is defined as a variable.
			Then, x is assigned the value of 6:
		</p>

		<p id="demo"></p>

		<script>
			let x;
			x = 6;
			document.getElementById("demo").innerHTML = x;
		</script>
	</body>
</html>
```

# JavaScript 연산자

자바스크립트는 값을 계산하기 위해 산술 연산자(+ - * /)를 사용합니다.

``` html
<!DOCTYPE html>
<html>
	<body>

		<h2>JavaScript Operators</h2>

		<p>JavaScript uses arithmetic operator to compute values (just like algebra).</p>

		<p id="demo"></p>

		<script>
			document.getElementById("demo").innerHTMl = (5 + 6) * 10;
		</script>
	</body>
</html>
``` 

자바스크립트는 변수에 값을 할당하기 위해 할당 연산자(=)을 사용합니다.

``` html
<html>
	<body>

		<h2>Assigning JavaScript Values</h2>

		<p>In JavaScript the = operator is used to assign values to variables.</p>

		<p id="demo">

			<script>
				let x, y;
				x = 5;
				y = 6;
				document.getElementById("demo").innerHTML = x + y;
			</script>
	</body>
</html>
```

# 자바스크립트 표현식

- 표현식은 값을 계산하는 값, 변수 및 연산자의 조합입니다.
- 계산을 평가라고 합니다.
- 예를 들어 5 * 10은 50으로 평가됩니다.

``` html
<!DOCTYPE html>
<html>
<body>
<h2>JavaScript Expressions</h2>

<p>Expressions compute to values.</p>

<p id="demo"></p>

<script>
document.getElementById("demo").innerHTML= 5* 10;</script>
</body></html>
```

표현식에는 변수 값도 포함될 수 있습니다.

``` html
<!DOCTYPE html>
<html>
	<body>

		<h2>JavaScript Expressions</h2>

		<p>Expressions compute to values.</p>

		<p id="demo"></p>

		<script>
			var x;
			x = 5;
			document.getElementById("demo").innerHTML = X * 10;
		</script>
	</body>
</html>
```

- 값은 숫자 및 문자열과 같은 다양한 유형일 수 있습니다.
- 예를 들어 "John" + "" + "Doe"는 "John Doe"로 평가됩니다.

``` html
<!DOCTYPE html>
<html>
	<body>
		<h2>JavaScript Expressions</h2>

		<p>Expressions compute to values.</p>

		<p id="demo"></p>

		<script>
			document.getElementById("demo").innerHTML = "John" + " " + "Doe";
		</script>
	</body>
</html>
```

# 자바스크립트 키워드

- 자바스크립트 키워드는 수행할 작업을 식별하는 데 사용됩니다.
- let 키워드는 브라우저에 변수를 생성하도록 지시합니다.

``` html
<!DOCTYPE html>
<html>
	<body>

		<h2>The <>let</b> Keyword Creates Variables</h2>

		<p id="demo"></p>

		<script>
			let x, y;
			x = 5 + 6;
			y = x * 10;
			document.getElementById("demo").innerHTML = y;
		</script>

	</body>
</html>
```

var 키워드는 또한 브라우저에 변수를 생성하도록 지시합니다.
``` html
<!DOCTYPE html>
<html>
	<body>

		<h2>THe var Keyword Creates Variables</h2>

		<p id="demo"></p>

		<script>
			var x, y;
			x = 5 + 6;
			y = x * 10;
			document.getElementById("demo").innerHTML = y;
		</script>
	</body>
</html>
```

- 이 예에서 var 또는 let을 사용하면 동일한 결과가 생성됩니다.

# JavaScript Comments

- 모든 JavaScript 문이 "실행"되는 것은 아닙니다.
- 이중 슬래시 `//` 또는 /*와 */ 사이의 코드는 주석으로 처리됩니다.
- 주석은 무시되며 실행되지 않습니다.

``` html
<!DOCTYPE html>
<html>
	<body>

		<h2>JavaScript Comment are Not Executed</h2>

		<p id="demo"></p>

		<script>
			let x;
			x = 5;
			// x = 6; I will not be executed
			document.getElementById("demo").innerHTML = x;
		</script>
	</body>
</html>
```

# 자바스크립트 식별자

- 식별자는 이름입니다.
- 자바스크립트에서 식별자는 변수를 이름짓기 위해 사용됩니다(키워드, 함수, 레이블).
- legal names에 대한 규칙은 대부분의 프로그래밍 언어에서 거의 동일합니다.
- 자바스크립트에서 첫 번째 문자는 문자, 밑줄(_), 또는 달러 기호($)여야 합니다.
- 후속 문자는 문자, 숫자, 밑줄 또는 달러 기호 일 수 있습니다.
- 숫자는 첫 번째 문자로 사용할 수 없습니다.
- 이 방법으로 JavaScript는 식별자와 숫자를 쉽게 구별할 수 있습니다.

# 자바스크립트는 대소문자를 구분합니다.

- 모든 자바스크립트 식별자는 대소문자를 구분합니다.
- 변수 `lastname`과 `lastName`은 다른 두 개의 변수입니다.

``` html
<!DOCTYPE html>
<html>
	<body>

		<h2>JavaScript is Case Sensitive</h2>

		<p>Try to change lastName to lastname.</p>

		<p id="demo"></p>

		<script>
			let lastname, lastName;
			lastName = "Doe";
			lastname = "Peterson";
			document.getElementById("demo").innerHTML = lastName;
		</script>
	</body>
</html>
```
JavaScript는 `LET` 또는 `Let`을 키워드 `let`로 해석하지 않습니다.

# 자바스크립트와 카멜 케이스

- 역사적으로 프로그래머는 여러 단어를 하나의 변수 이름으로 결합하는 다양한 방법을 사용했습니다.
- `Hypens`:
  - first-name, last-name, master-card, inter-city.
- 하이픈은 자바스크립트에서 허용되지 않습니다. 
- 뺼셈을 위해 예약되어 있습니다.
- `Underscore`:
  - first_name, last_name, master_card, inter_city.
- `Upper Camel Case (Pascal Case)`:
  - FirstName, LastName, MasterCard, InterCity.
- `Lower Camel Case`:
  - 자바스크릅티 프로그래머들은 소문자로 시작하는 카멜 케이스를 사용하는 경향이 있습니다.
  - firstName, lastName, masterCard, interCity 

# 자바스크립트 문자 집합

- 자바스크립트는 유니코드 문자 집합을 사용합니다.
- 유니코드는 (거의) 세계의 모든 문자, 구두점 및 기호를 다룹니다.
  

# REFERENCE

https://www.w3schools.com/js/js_syntax.asp
