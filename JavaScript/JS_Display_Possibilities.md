# JavaScript Display Possibilities

자바스크립트는 다양한 방식을 데이터를 "표시"할 수 있습니다.

- innerHTML을 사용하여 HTML 요소에 쓰기.
- document.write()를 사용하여 HTML 출력에 쓰기.
- window.alert()를 사용하여 경고 상자에 쓰기.
- console.log()를 사용하여 브라우저 콘솔에 쓰기.

# innerHTML 사용하기

- HTML 요소에 접근하기 위해 JavaScript는 document.getElementById(id) 메서드를 사용할 수 있습니다.
- id 속성은 HTML 요소를 정의합니다.
- innerHTML 속성은 HTML 콘텐츠를 정의합니다.

``` html
<!DOCTYPE html>
<html>
 <body>

  <h1>My First Web Page</h1>
  <p>My First Paragraph</p>

  <p id="demo"></p>

  <script>
   document.getElementById("demo").innerHTML = 5+6;
  </script>
 </body>
</html>
```

HTML 요소의 innerHTML 속성을 변경하는 것은 HTML에 데이터를 표시하는 일반적인 방법입니다.

# document.write() 사용하기

테스트 목적으로 document.write()를 사용하는 것이 편리합니다.

``` html
<!DOCTYPE html>
<html>
 <body>

  <h1>My First Web Page</h1>
  <p>My first paragraph</p>

  <script>
   document.write(5+6);
  </script>
 </body>
</html>
```

HTML 문서가 로드된 후 document.write()를 사용하면 기존 HTML이 모두 삭제됩니다.

``` html
<!DOCTYPE html>
<html>
 <body>

  <h1>My First Web Page</h1>
  <p>My first paragraph.</p>

  <button type="button" onclick="document.write(5+6)">Try it</button>


 </body>
</html>
```

document.write() 메서드는 테스트용으로만 사용해야 합니다.

# window.alert() 사용하기

경고 상자를 사용하여 데이터를 표시할 수 있습니다.

``` html
<!DOCTYPE html>
<html>
 <body>

  <h1>My First Web Page</h1>
  <p>My First paragraph.</p>

  <script>
   window.alert(5+6);
  </script>
 </body>
</html>
```

- `window` 키워드는 건너뛸 수 있습니다.
- JavaScript에서 window 객체는 전역 범위 객체입니다.
- 즉, 기본적으로 변수, 속성 및 메서드는 window 객체에 속합니다.
- 이것은 또한 window 키워드를 지정하는 것이 선택 사항임을 의미합니다.

# console.log() 사용하기

- 디버깅을 위해 브라우저에서 console.log() 메서드를 호출하여 데이터를 표시할 수 있습니다.

``` html
<!DOCTYPE html>
<html>
 <body>
  <script>
   console.log(5+6);
  </script>
 </body>
</html>  
```

# JavaScript Print

- 자바스크립트에는 인쇄 개체나 인쇄 방법이 없습니다.
- 자바스크립에서 출력 장치에 접근할 수 없습니다.
- 유일한 예외는 브라우저에서 window.print() 메서드를 호출하여 현재 창의 내용을 인쇄할 수 있다는 것입니다.

``` html
<!DOCTYPE html>
<html>
	<body>
		<h2>The window.print() Method</h2>

		<p>Click the button to print the current page.</p>
		<button onclick="window.print()">Print this page</button>

	</body>
</html>
```

# REFERENCE

https://www.w3schools.com/js/js_output.asp

