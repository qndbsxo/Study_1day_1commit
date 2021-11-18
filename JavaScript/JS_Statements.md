# JavaScript Statements

``` html
<!DOCTYPE html>
<html>
	<body>

		<h2>JavaScript Statements</h2>

		<p>A <b>JavaScript program</b> is a list of
		<b>statements</b> to be executed by a computer.</p>
		
		<p id="demo"></p>

		<script>
			let x, y, z; // Statement 1
			x = 5; // Statement 2
			y = 6; // Statement 3
			z = x + y; // Statement 4

			document.getElementById("demo").innerHTML = "The value of z is " + z + ".";
		</script>
	</body>
</html>


```

# JavaScript Programs

- 컴퓨터 프로그램은 컴퓨터에 의해 "실행"되는 "명령"의 목록입니다.
- 프로그래밍 언어에서는 이러한 프로그래밍 명령을 명령문이라고 합니다.
- JavaScript 프로그램은 프로그래밍 명령문의 목록입니다.
- HTML에서 JavaScript 프로그램은 웹 브라우저에 실행됩니다.

# JavaScript Statements

JavaScript 문은 다음으로 구성됩니다.

- 값, 연산자, 표현식, 키워드, 주석
- 이 명령문은 브라우저에 "Hello Dolly"를 쓰도록 지시합니다.
- id="demo"인 HTML 요소 내부:

``` html
<!DOCTYPE html>
<html>
	<body>
		<h2>JavaScript Statements</h2>

		<p>In HTML, JavaScript statements are executed by the browser.</p>

		<p id="demo"></p>

		<script>
			document.getElementById("demo").innerHTML = "Hello Dolly.";
		</script>
	</body>
</html>
```

- 대부분의 JavaScript 프로그램에는 많은 JavaScript 문이 포함되어 있습니다.
- 명령문은 작성된 순서대로 하나씩 실행됩니다.
- JavaScript 프로그램(및 JavaScript 문)은 종종 JavaScript 코드라고 합니다.

# 세미콜론;

- 세미콜론은 JavaScript 문을 구분합니다.
- 각 실행 문 끝에 세미콜론을 추가합니다.

``` html
<!DOCTYPE html>
<html>
	<body>

		<h2>JavaScript Statements</h2>

		<p>JavaScript statements are separated by semicolons.</p>

		<p id="demo1"></p>

		<script>
			let a, b, c;
			a = 5;
			b = 6;
			c = a + b;
			document.getElementById("demo1").innerHTML = c;
		</script>
	</body>
</html>
```

세미콜론으로 구분하면 한 줄에 여러 문이 허용됩니다.

``` html
<!DOCTYPE html>
<html>
	<body>

		<h2>JavaScript Statements</h2>

		<p>Multiple statements on one line are allowed.</p>

		<p id="demo1"></p>

		<script>
			let a, b, c;
			a = 5; b = 6; c = a + b;
			document.getElementById("demo1").innerHTML = c;
		</script>

	</body>
</html>
```

- 웹에서 세미콜론이 없는 예제를 볼 수 있습니다.
- 세미콜론으로 끝나는 문장은 필수는 아니지만 적극 권장합니다.

# 자바스크립트 공백

- JavaScript는 여러 공백을 무시합니다.
- 스크립트에 공백을 추가하여 가독성을 높일 수 있습니다.
- 다음 줄은 동일합니다.

``` javascript
let person = "Hege";
let person = "Hege";
```

좋은 방법은 연산자(=+-*/)주위에 공백을 넣는 것입니다.

``` javascript 
let x = y + z ;
```

# 자바스크립트 줄 길이 및 줄 바꿈

- 최고의 가독성을 위해 프로그래머는 종종 80자 보다 긴 코드 라인을 피하고 싶어합니다.
- JavaScript 문이 한 줄에 맞지 않는 경우 가장 좋은 위치는 연산자 다음입니다.

``` html
<!DOCTYPE html>
<html>
	<body>
		<h2>JavaScript Statements</h2>

		<p>
			The best place to break a code line is after an operator or a comma.
		</p>

		<p id="demo"></p>

		<script>
			document.getElementById("demo").innerHTML = "Hello Dolly!";
		</script>
	</body>
</html>
```

# 자바스크립트 코드 블록

- 자바스크립트 문은 중괄호 {...} 안에 있는 코드 블록으로 그룹화 할 수 있습니다.
- 코드 블록의 목적은 함께 실행할 명령문을 정의하는 것입니다.
- 블록으로 함께 그룹화된 명령문을 찾을 수 있는 곳은 JavaScript 함수입니다.

``` html
<!DOCTYPE html>
<html>
	<body>

		<h2>JavaScript Statements</h2>

		<p>JavaScript code blocks are written between {and}</p>

		<button type="button"
		onclick="myFunction()">Click Me!</button>

		<p id="demo1"></p>
		<p id="demo2"></p>

		<script>
			function myFunction() {
				document.getElementById("demo1").innerHTML = "Hello Dolly!";
				document.getElementById("demo2").innerHTML = "How are you?";
			}
		</script>
	</body>
</html>
```
# 자바스크립트 키워드

- 자바스크립트 문은 수행할 자바스크립트 작업을 식별하는 키워드로 시작하는 경우가 많습니다.

keyword | Description
---|---
var | 변수 선언
let | 블록 변수 선언
const | 블록 상수 선언
if | 조건에서 실행할 명령문 블록을 표시합니다.
switch | 다른 경우에 실행할 명령문 블록을 표시합니다.
for | 루프에서 실행할 명령문 블록을 표시합니다.
function | 함수 선언
return | 함수 종료
try | 명령문 블록에 대한 오류 처리를 구현합니다.

- JavaScript 키워드는 예약어입니다.
- 예약어는 변수 이름으로 사용할 수 없습니다.

# REFERENCE

https://www.w3schools.com/js/js_statements.asp






