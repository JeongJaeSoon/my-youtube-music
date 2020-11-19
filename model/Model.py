import sqlite3


class Model:
    def get_db_conn(self):
        conn = sqlite3.connect("database/my_youtube_music_playlist.db")
        cursor = conn.cursor()
        return conn, cursor

    # 테이블의 상태를 점검하고 이상 유무를 반환
    def check_table_list(self, cursor):
        # cursor = conn.cursor()
        # DB 목록을 조회
        sql_get_table_list = "SELECT name FROM sqlite_master " \
                             "WHERE type IN ('table', 'view') " \
                             "AND name NOT LIKE 'sqlite_%' " \
                             "UNION ALL " \
                             "SELECT name FROM sqlite_temp_master " \
                             "WHERE type IN ('table', 'view') ORDER BY 1"
        cursor.execute(sql_get_table_list)
        rows = cursor.fetchall()

        is_table_exists = {
            "playlist": False,
            "music_list": False,
            "result": False
        }

        for row in rows:
            is_table_exists['playlist'] = True if row[0] == "playlist" else is_table_exists['playlist']
            is_table_exists['music_list'] = True if row[0] == "music_list" else is_table_exists['music_list']

        is_table_exists['result'] = is_table_exists['playlist'] and is_table_exists['music_list']

        # <<-- PRINT CHECK MSG -->>
        print(f"플레이리스트 목록\t : {'양호' if is_table_exists['playlist'] else '확인불가'}")
        print(f"노래 목록\t\t\t : {'양호' if is_table_exists['music_list'] else '확인불가'}")
        print("")

        return is_table_exists

    def create_table(self, cursor, sql_create_table):
        cursor.execute(sql_create_table)

    def drop_table(self, cursor, table_name):
        sql_drop_table = f"DROP TABLE {table_name}"
        cursor.execute(sql_drop_table)
