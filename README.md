# My-YouTube-music

## 팀원
 - 1301257 정재순 
 - 1901249 장주영

## 사용 패키지
```
pip3 install sqlite3                # 기본 파이썬 패키지에 미 포함시, 설치
pip3 install beautifulsoup4         # YouTube 크롤링
```

## 프로젝트 소개

#### 유튜브를 통한 음악 스트리밍 이용 확대
- 유튜브에서 다양한 카테고리의 음악 플레이리스트 영상을 제공하는 채널이 인기
- 하나의 플레이리스트 영상에 여러 종류의 음악들이 수록되어 있음
  <table>
    <tr>
      <td align="center">
      <img src="https://user-images.githubusercontent.com/53788601/97783256-df1cec80-1bd9-11eb-9556-7a2f018bcf43.png" width="350px;" alt="멜론 총각&멜론 뮤직 채널"/><br />
      <sub><b>멜론 총각&멜론 뮤직 채널</b></sub>
      </td>
      <td align="center">
      <img src="https://user-images.githubusercontent.com/53788601/97783259-e47a3700-1bd9-11eb-9fbe-6db1d49374d9.png" width="350px;" alt="멜론 둥이 채널"/><br />
      <sub><b>멜론 둥이 채널</b></sub>
      </td> 
    </tr>
    <tr>
      <td align="center">
      <img src="https://user-images.githubusercontent.com/53788601/97783263-e7752780-1bd9-11eb-9ea6-aef6a11d8dbf.png" width="350px;" alt="한번 들어봐 채널"/><br />
      <sub><b>한번 들어봐 채널</b></sub>
      </td>
      <td align="center">
      <img src="https://user-images.githubusercontent.com/53788601/97783265-e9d78180-1bd9-11eb-85ca-d708dba22272.png" width="350px;" alt="essential 채널"/><br />
      <sub><b>essential 채널</b></sub>
      </td>   
    </tr>
  </table>

#### 원하는 곡만 선택해서 나만의 플레이리스트화가 어려움
- 유튜브 특성 상 각 영상에 대해서만 재생목록 저장이 가능
- 플레이리스트 영상에서 원하는 곡만 재생목록에 추가하고 싶을 경우, 재검색 과정이 필요
  <img src="https://user-images.githubusercontent.com/53788601/97783512-9ebe6e00-1bdb-11eb-93a8-0c1927a107df.png" width="600px" alt=""/>

#### 영상의 음악정보를 수집하여 플레이리스트화 서비스 제공
- 영상의 메타데이터 영상 내에 포함된 음악 정보 포함
- 크롤링을 통해 영상의 음악정보를 수집하고, 사용자에게 음악 목록을 제공
- 사용자가 원하는 음악 목록에서 원하는 곡만 선택하여 플레이리스트 재생성 가능
  <img src="https://user-images.githubusercontent.com/53788601/97783571-0bd20380-1bdc-11eb-89f0-aac137630e17.png" width="600px" alt=""/>

## 시스템 구성도
- 단일 프로그램에서 구동되고 검색창에 유튜브 링크 입력 시, 메타 데이터 크롤링 후 사용자에게 제공
- 사용자가 재생목록을 생성, 조회, 수정, 삭제 시 프로그램 설치 시 생성되는 문서 파일을 통해, 데이터 저장
  <img src="https://user-images.githubusercontent.com/53788601/97784532-99185680-1be2-11eb-9a3c-9fd1a725f47e.png" width="600px" alt="" />

## 사용 기술 키워드

#### GUI 구성 및 프로그램 제작
- PyQt5 : 프로그램 조작에 필요한 GUI 화면 구성
- PyInstaller : Windows 및 Mac OS 용 실행파일 제작
- YouTube DATA API : iframe-api 활용 음악 재생

#### 웹 크롤러 및 DB 저장
- Beautiful Soup 4, Selenium : 유튜브 메타 데이터 및 iframe 정보 크롤링
- SQlite : 문서를 통해 사용자 재생목록 저장