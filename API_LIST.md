# My YouTube Music API list

## PlayListController

#### 플레이리스트 목록 조회 : `index_playlist()`

- Argument : 없음
- Return
    1. 조회 성공 시 : 플레이리스트 목록을 배열로 반환
    2. 데이터가 없을 경우 : 빈 배열을 반환

#### 플레이리스트 생성 : `create_playlist()`

- Argument

  1.  playlist_name : 플레이리스트 이름(String)
  2.  music : 음악 정보 목록(Array) _(option)_

- Return

  1. 플레이리스트 생성 성공 시 : "플레이리스트 '{playlist_name}' 이(가) 생성되었습니다.
  2. 플레이리스트 생성 + 음악 저장 : 2번 메시지 + (00곡 저장 완료)
  3. 중복되는 이름 입력 시 : "이미 저장된 플레이리스트 이름입니다."

#### 플레이리스트 이름 변경 : `modify_playlist_name()`

- Argument

  1.  playlist_id : 변경할 플레이리스트 Id(Integer)
  2.  new_playlist_name : 새로운 플레이리스트 이름(String)

- Return

  1. 이름 변경 성공 시 : 플레이리스트 이름이 '{new_playlist_name}' (으)로 변경되었습니다.
  2. 이름 변경 실패 시
     - 잘못된 플레이리스트 Id : 존재하지 않는 플레이리스트입니다.
     - 기존 이름과 동일 : 기존 플레이리스트 이름과 동일합니다.
     - 중복된 이름 : 이미 저장된 플레이리스트 이름입니다.
     - 알수없는 오류 : 플레이리스트 이름 변경에 실패하였습니다.

#### 플레이리스트 삭제 : `destroy_playlist()`

- Argument

  1.  playlist_id : 삭제할 플레이리스트 Id(Integer)

- Return

  1. 삭제 성공 시 : '{playlist_name}' 플레이리스트가 삭제되었습니다.
  2. 삭제 실패 시
     - 잘못된 플레이리스트 Id : 존재하지 않는 플레이리스트입니다.

## MusicListController

#### 플레이리스트의 음악 목록 조회 : `index_music_list()`

- Argument : 조회할 플레이리스트 Id(Integer)
- Return

    1. 조회 성공 시 : 플레이리스트에 저장된 악 목록을 배열로 반환
    2. 데이터가 없을 경우 : 빈 배열을 반환
    3. 조회 실패 시
        - 잘못된 플레이리스트 Id : 존재하지 않는 플레이리스트입니다.

#### 플레이리스트에 음악 추가 : `add_music_list()`

- Argument

  1.  playlist_id : 음악을 추가할 플레이리스트 Id(Integer)
  2.  musics : 추가할 음악 정보의 목록(Array)

- Retrun

  1. 추가 성공 시 : '{playlist_name}' 에 새롭게 {count}곡이 추가되었습니다.\n(중복곡 제외)
  2. 추가된 곡이 없을 시 : 플레이리스트에 새롭게 추가된 음악이 없습니다.
  3. 추가 실패 시
     - 잘못된 플레이리스트 Id : 존재하지 않는 플레이리스트입니다.

#### 플레이리스트에서 음악 삭제 : `delete_music_list()`

- Argument

  1. musics : 삭제할 음악 Id(Array)

- Retrun

  1. 삭제 성공 시 : {count} 곡이 삭제되었습니다.
  2. 삭제된 곡이 없을 시 : 삭제된 음악이 없습니다.

## CrawlerController

#### YouTube URL 에서 음악 목록 크롤링 : `get_music_list()`

- Argument

    1. URL : 크롤링을 할 YouTube URL(String)
    
- Return

    1. 크롤링 성공 시 : 크롤링 결과 수집된 음악목록을 배열로 반환
        - link : 음악 링크 포함 여부
        - title / musician : 음악 이름 / 가수
        - url : 음악 링크 정보
    2. 크롤링 실패 시(네트워크 오류, 연결 거부 등) : 음악 목록 조회에 실패하였습니다.
    3. 크롤링 데이터 없을 시 : 등록된 음악 정보가 없습니다. 