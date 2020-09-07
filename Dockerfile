# Base(Parent) 이미지 설정
FROM python:3.6.10-buster

# maintainer 지정
LABEL maintainer="yonghee.cheon@gmail.com"

# 환경변수 설정 (optional)
ENV LANG C.UTF-8

# pip upgrade
RUN pip install pip --upgrade

# 지금 디렉토리의 모든 파일들을 도커 컨테이너의 /로 복사
# 디렉토리는 따로 설정 가능
ADD . /app

# Working Directory로 이동
WORKDIR /app

# 패키지 설치
RUN pip install -r requirements.txt

# 실행하기
CMD python3.6 main.py