# 리다이렉션

fd( file description, 파일 기술자)

- 0 | 표준입력 ( stdin [keyboard]) |
- 1 | 표준출력 ( stdout [screen])
- 2 | 표준에러 ( stderr [screen])

입력 리다이렉션

- cat 명령어는 입력 리다이렉션을 포함하는 명령어
- 쓰는 방법은 실행값과 같이 <, 0< 
- <<는 `Here Documentation`이라는 기호

출력 리다이렉션

- 출력 리다이렉션은 >, 1>, >> 
- `>>`, `>`이 두 기호의 차이점은 덮어쓰기와 추가하기
- `>>` 내용추가
- `>` 덮어쓰기


에러 출력 리다이렉션

- 에러 출력문을 파일로 보내는 것
- /dev/null 보통 출력을 보고 싶지 않을 때 이곳으로 많이 보냄
- /dev/null 주기적으로 비워지는 공간

# REFERENCE
https://m.blog.naver.com/PostView.naver?isHttpsRedirect=true&blogId=minki0127&logNo=220683488997
