import sqlite3

from model.Model import Model
from model.PlayList import PlayList
from model.MusicList import MusicList

playlist = PlayList()
music_list = MusicList()


# 데이터 초기화 함수
#   -> 프로그램 실행 시, DB 상태를 점검
#   -> DB 가 없을 경우, DB 를 생성
#   -> 문제가 있을 경우, 데이터를 초기화 하고 다시 생성
def init_sqlite_db_tables():
    model = Model()
    conn, cursor = model.get_db_conn()
    is_table_exists = model.check_table_list(cursor)
    if not is_table_exists['result']:
        print("=> 테이블 재설정 진행\n")

        if is_table_exists['playlist']:
            playlist.drop_table(cursor, "playlist")
        if is_table_exists['music_list']:
            music_list.drop_table(cursor, "music_list")

        sql_create = {
            "playlist": "CREATE TABLE playlist ("
                        "       id INTEGER PRIMARY KEY AUTOINCREMENT,"
                        "       name TEXT UNIQUE NOT NULL,"
                        "       create_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP "
                        ")",
            "music_list": "CREATE TABLE music_list ("
                          "     id INTEGER PRIMARY KEY AUTOINCREMENT,"
                          "     title TEXT NOT NULL,"
                          "     musician TEXT NOT NULL,"
                          "     url TEXT NOT NULL,"
                          "     playlist_id INTEGER,"
                          "     create_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,"
                          "     FOREIGN KEY (playlist_id) REFERENCES playlist (id)"
                          ")"
        }
        playlist.create_table(cursor, sql_create['playlist'])
        music_list.create_table(cursor, sql_create['music_list'])

    conn.close()


# 플레이리스트를 생성하는 함수
#   -> 플레이리스트 이름, 플레이리스트 목록을 받음
#   -> 중복된 플레이리스트 이름은 사용 불가
#   -> 플레이 리스트 생성시,
def create_playlist(playlist_name, musics=None):
    if musics is None:
        musics = []

    count = 0
    is_insert_music = True if len(musics) != 0 else False
    conn, cursor = Model().get_db_conn()

    try:
        # 플레이리스트 생성 및 음악 목록 저장
        playlist_id = playlist.insert_playlist(cursor, playlist_name)
        if is_insert_music:
            count = music_list.insert_music_list(cursor, playlist_id, musics)
    except sqlite3.IntegrityError:
        print("중복된 이름의 플레이리스트는 저장할 수 없습니다.")
        return
    # except Exception:
    #     print("알 수 없는 오류로 종료되었습니다.")
    else:
        print(f"플레이리스트 '{playlist_name}' 이(가) 생성되었습니다.")
        print(f"({count}곡 저장 완료)" if
              is_insert_music else "", end="")
        # TODO 주석 풀기
        conn.commit()


# TODO 플레이리스트 이름 수정
# TODO 플레이리스트에 음악 추가(여러곡 또는 한곡)
# TODO 플레이리스트에서 음악 삭제(여러곡 또는 한곡)
# TODO 플레이리스트 삭제

# <<-- TEST CODE -->>
test_music_list = [
    {'link': True, 'title': 'Good Vibes', 'musician': 'HRVY, Matoma', 'url': 'Q1Yy0tNWtnE'},
    {'link': True, 'title': 'Push-ups', 'musician': 'Scarlet Pleasure', 'url': 'aXGOieAtYzk'},
    {'link': True, 'title': 'monday', 'musician': 'somegirlnamedanna', 'url': 'BO4PaNmqAkA'},
    {'link': True, 'title': 'happiness', 'musician': 'John K', 'url': 'oUcYb0iOivU'},
    {'link': True, 'title': 'On and On', 'musician': 'PREP', 'url': 'sqR9V-D6pQw'},
    {'link': True, 'title': 'OK Not To Be OK', 'musician': 'Marshmello, Demi Lovato',
     'url': 'eOPW5geTnEI'},
    {'link': True, 'title': 'Grateful', 'musician': '13 Crowns', 'url': 'a9-QT63rD5Y'},
    {'link': True, 'title': 'WAIT FOR YOU', 'musician': 'Jake Miller', 'url': 'Ttt-YV79KbY'},
    {'link': True, 'title': 'Lemonade', 'musician': 'Circa Waves', 'url': 'Bv12KhnJomc'},
    {'link': True, 'title': 'Backyard Boy', 'musician': 'Claire Rosinkranz, Jeremy Zucker',
     'url': 'WmnnvfP-j0k'},
]

init_sqlite_db_tables()
create_playlist("기분 좋아지는 노래10", test_music_list)
create_playlist("기분 좋아지는 노래1")
