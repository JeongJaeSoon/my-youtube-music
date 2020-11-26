from model.Model import Model
from model.PlayList import PlayList
from model.MusicList import MusicList


class Controller:
    def __init__(self):
        self.conn, self.cursor = Model().get_db_conn()
        self.model = Model()
        self.playlist = PlayList()
        self.music_list = MusicList()

    # 데이터베이스 초기화 함수
    #   -> 프로그램 실행 시, DB 상태를 점검
    #   -> DB 가 없을 경우, DB 를 생성
    #   -> 문제가 있을 경우, 데이터를 초기화 하고 다시 생성
    def init_database(self):

        conn, cursor = self.model.get_db_conn()
        is_table_exists = self.model.check_table_list(cursor)

        if not is_table_exists['result']:
            print("=> 테이블 재설정 진행\n")

            if is_table_exists['playlist']:
                self.playlist.drop_table(cursor, "playlist")
            if is_table_exists['music_list']:
                self.music_list.drop_table(cursor, "music_list")

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
            self.playlist.create_table(cursor, sql_create['playlist'])
            self.music_list.create_table(cursor, sql_create['music_list'])

        self.conn.commit()
