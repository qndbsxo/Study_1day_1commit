# JavaScript Debugging

- 새로운 컴퓨터 코드를 작성할 때마다 에러는 발생할 수 있다.


# Code Debugging

- 프로그래밍 코드에는 문법에러나 논리적 에러가 포함될지도 모른다.
- 이러한 많은 에러들은 진단하기 어렵습니다.
- 가끔 프로그래밍 코드에 에러가 포할될 때, 아무 일도 나지 않습니다.
- 에러메시지도 나타나지 않습니다. 그리고 오류를 검색할 위치가 표시되지 않습니다.
- 프로그래밍 코드에서 오류를 검색(및 수정)하는 것을 코드 디버깅이라고 합니다.

# JavaScript Debuggers

- 디버깅은 쉽지 않습니다. 운이 좋게도, 대부분의 현대 브라우저에는 자바스크립트 디버거가 내장되어 있습니다.
- 내장 디버거는 키거나 끌 수 있으며,강제로 오류를 사용자에게 보고합니다.
- 디버거를 사용하여 중단점(코드 실행을 중지할 수 있는 위치)을 설정할 수 있습니다.
- 코드가 실행되는 동안 변수를 검사합니다.
- F12 키를 사용하여 브라우저에서 디버깅을 활성화하고 디버거 메뉴에서 "콘솔"을 선택합니다.

# The console.log() Method

- 브라우저가 디버거를 지원한다면, `console.log()`를 사용하여 디버거 창에 자바스크립트 값을 나타낼 수 있습니다.

``` html
<!DOCTYPE html>
<html>
	<body>

		<h2>My First Web Page</h2>

		<p>Activate debugging in your browser (Chrome, IE, Firefox) with F12, and select "Console" in the debugger menu.</p>

		<script>
			a = 5;
			b = 6;
			c = a + b;
			console.log(c);
		</script>
	</body>
</html>
```

# Setting Breakpoints

- 디버깅 창에서 JavaScript 코드에 중단점을 설정할 수 있습니다.
- 각 브레이크 포인트에서, 자바스크립트는 실행을 중답하니다. 그리고 자바스크립트 value를 검사합니다.
- values를 검사한 이후에 코드 실행을 재개할 수 있습니다.

# The debugger Keyword

- The `debuger` keyword stops the execution of JavaScript, and calls (if available) the debugging function
- This has the same function as setting a breakpoint in the debugger.
- If no debugging is available, the debugger statement has no effect
- With the debugger turned on, this code will stop executing before it execute the third line.

``` html
<!DOCTYPE html>
<html>
	<body>
		<h2>JavaScript Debugger</h2>
		<p id="demo"></p>

		<p>Withe teh debugger turned on, the code below should stop executing before it execute the third line</p>

		<script>
			let x 15 * 5
			debugger;
			document.getElementById("demo").innerHTML = x;
		</script>
	</body>
</html>
```

# Major Browsers'Debugging Tools

Normally, you activate debugging in your browser with F12, and select "Console" in the debugger menu.

Otherwise follow these steps:

## Chrome

- Open the browser
- From the menu, select "More tools".
- From tools, choose "Developer tools".
- Finally, select Console.

 Debugging is the process of testing, finding, and reducing bugs(errors) in computer |programs.
The first known computer bug was a real bug (an insect) stuck in the electronics.

# REFERENCE
https://www.w3schools.com/js/js_debugging.asp

