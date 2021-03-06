# DockerFile 작성법

- FROM: 생성할 이미지의 베이스가 될 이미지를 뜻합니다. 반드시 한 번 이상 입력해야 합니다.
- LABEL: 이미지에 `메타데이터`를 추가합니다. (나중에 원하는 조건의 컨테이너, 이미지 등을 쉽게 찾을 수 있또록 도와주기 때문에 기억해두는게 좋습니다)
- RUN: 이미지를 만들기 위해 컨테이너 `내부에서 명령어`를 실행합니다. (여기서 주의할 점은 설치과정에서 별도의 입력이 불가능하기 때문에 apache2를 설치할 때 뒤에 -y를 붙여줘야 합니다.)
- ADD: `파일을 이미지에 추가` 합니다. 여기서는 Dockerfile이 위치한 폴더에 test.html 파일을 가져와서 이미지의 /var/www/html 디렉터리에 추가합니다.
- WORKDIR: 명령어를 실행할 디렉토리. 배시 셸에서의 `cd명령어와 동일한 기능`을 합니다.
- EXPOSE: 이미지에서 `노출할 포트`를 설정합니다.
- CMD: `컨테이너가 시작될 때마다 실행할 명령어`.  Dockerfile 에서 한 번만 사용할 수 있습니다.
  
> 부가적으로 RUN ["/bin/bash", "-c", "echo hello > test2.html"] 
> => /bin/bash 셀을 이용해 echo hello > test2.html을 실행하라는 뜻입니다.


# REFERENCE
https://velog.io/@ckstn0777/%EB%8F%84%EC%BB%A4%ED%8C%8C%EC%9D%BCDockerfile
