from module.db_util import \
    check_sqlite_db_table, create_sqlite_db_connection, create_playlist_table, \
    create_music_list_table, delete_playlist_table, delete_music_list_table


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

    print("==> 필요 DB 생성")
    if not is_table_exists['playlist']:
        create_playlist_table()
        print("플레이리스트 목록\t : 생성")

    if not is_table_exists['music_list']:
        create_music_list_table()
        print("노래 목록\t\t\t : 생성")


def insert_playlist(playlist_name, musics):
    # TODO 플레이리스트 중복 검사 알고리즘 추가 필요

    conn = create_sqlite_db_connection()
    cursor = conn.cursor()

    # 플레이리스트
    sql_insert_playlist = f"INSERT INTO playlist(name) VALUES ('{playlist_name}')"
    cursor.execute(sql_insert_playlist)

    # TODO name(기타 등등) 으로 정보 가져오는 함수 만들어서 추가
    sql_select_playlist_by_name = f"SELECT * FROM playlist WHERE name = '{playlist_name}'"
    cursor.execute(sql_select_playlist_by_name)
    print(cursor.fetchall())
    # for music in musics:
    #     if music['link']:
    #         sql_insert_music_list = "INSERT INTO music_list(title, musician, url, playlist_id)"
    #         print(music)


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
insert_playlist("기분 좋아지는 노래2", test_music_list)
