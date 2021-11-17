# JavaScript Tutorial

- JavaScript는 세계에서 가장 인기있는 프로그래밍 언어입니다.
- JavaScript는 웹 프로그래밍 언어입니다.
- 자바스크립트는 배우기 쉽습니다.

# JavaScript를 배우는 이유

자바스크립트는 모든 웹 개발자가 배워야 하는 3가지 언어 중 하나입니다.

1. 웹 페이지의 내용을 정의하는 HTML
2. 웹 페이지의 레이아웃을 지정하는 CSS
3. 웹 페이지의 동작을 프로그래밍하는 JavaScript

# JavaScript Can Change HTML Content

- 많은 자바스크립트 HTML 메소드 중 하나는 getElementById()입니다.
- 아래 예는 HTML 요소(id="demo" 포함)을 "찾고" 요소 콘텐츠(innerHTML)를 "Hello JavaScript"로 변경합니다.

```javascript
document.getElementById("demo").innerHTML = "Hello JavaScript";
```

- 자바스크립트는 큰 따옴표와 작은 따옴표를 모두 허용합니다.

``` javascript
document.getElementById('demo').innerHTML = 'Hello JavaScript';
```

- JavaScript는 HTML 속성 값을 변경할 수 있습니다.
- JavaScript는 HTML 스타일(CSS)을 변경할 수 있습니다.
- HTML 요소의 스타일 변경은 HTML 속성 변경의 변형입니다.

``` html
	<!DOCTYPE html>
	<html>
		<body>

			<h2>What Can JavaScript Do?</h2>

			<p id="demo">JavaScript can change the style of an HTML element.</p>

			<button type="button" onclick="document.getElementById('demo').style.fontSize='35px'">Click Me!</button>
		</body>
	</html>
```

- 자바스크립트는 HTML 요소를 숨길 수 있습니다.
- display 스타일을 변경하여 HTML 요소를 숨길 수 있습니다.

``` html
<!DOCTYPE html>
<html>
	<body>
		<h2>What Can JavaScript Do?</h2>

		<p id="demo">JavaScript can hide html element</p>

		<button type="button" onclick="document.getElementById('demo').style.display='none'">Click Me!</button>
	</body>
</html>
```
- JavaScript HTML 요소를 보여줄 수 있습니다.
- display style을 변경하여 숨겨진 html 요소를 표시할 수도 있습니다.

``` html
<!DOCTYPE html>
<html>
	<body>
		<h2>What Can JavaScript Do?</h2>
		<p>JavaScript can show hidden HTML elements.</p>

		<p id="demo" style="display:none">Hello JavaScript</p>

		<button type="button" onclick="document.getElementById('demo').style.display='block'">
		Click Me!</button>
	</body>
</html>
```

- 자바스크립트는 자바는 개념과 디자인 면에서 완전히 다른 언어입니다.
- 자바스크립트는 1995년 Brendan Eich에 의해 발명되었으며 1997년 ECMA 표준이 되었습니다.
- ECMA-262는 표준의 공식 이름입니다.
- ECMAScript는 언어의 공식 이름입니다. 

# REFERENCE

https://www.w3schools.com/js/js_intro.asp