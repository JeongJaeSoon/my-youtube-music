from module.db_util import \
    check_sqlite_db_table, create_sqlite_db_connection, create_playlist_table, \
    create_music_list_table, delete_playlist_table, delete_music_list_table, \
    insert_playlist, insert_music_list
import sqlite3


# 데이터 초기화 함수
#   -> 프로그램 실행 시, DB 상태를 점검
#   -> 문제가 있을 경우, 데이터를 초기화 하고 다시 생성
def init_sqlite_db_tables():
    is_table_exists = check_sqlite_db_table()

    # DB 상태가 불안정할 경우, 프로그램 에러 방지를 위해 테이블 삭제 후 재생성
    if not is_table_exists['playlist'] == is_table_exists['music_list']:
        print("==> DB 재설정")
        is_table_exists['playlist'] = delete_playlist_table() if is_table_exists['playlist'] else is_table_exists[
            'playlist']
        is_table_exists['music_list'] = delete_music_list_table() if is_table_exists['music_list'] else is_table_exists[
            'music_list']
        print()

    if not is_table_exists['playlist']:
        create_playlist_table()
        print("플레이리스트 목록\t : 생성")

    if not is_table_exists['music_list']:
        create_music_list_table()
        print("노래 목록\t\t\t : 생성")
    print("==> 필요 DB 생성 완료\n")


# 플레이리스트를 생성하는 함수
#   -> 플레이리스트 이름, 플레이리스트 목록을 받음
#   -> 중복된 플레이리스트 이름은 사용 불가
#   -> 플레이 리스트 생성시,
def create_playlist(playlist_name, music_list=[]):
    conn = create_sqlite_db_connection()
    count = 0
    is_insert_music = True if len(music_list) != 0 else False

    try:
        # 플레이리스트 생성 및 음악 목록 저장
        playlist_id = insert_playlist(conn, playlist_name)
        if is_insert_music:
            count = insert_music_list(conn, playlist_id, music_list)
    except sqlite3.IntegrityError:
        print("중복된 이름의 플레이리스트는 저장할 수 없습니다.")
        return
    else:
        print(f"플레이리스트 '{playlist_name}' 이(가) 생성되었습니다.")
        print(f"({count}곡 저장 완료)" if
              is_insert_music else "", end="")
        # TODO 주석 풀기
        # conn.commit()


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
create_playlist("기분 좋아지는 노래9", test_music_list)
