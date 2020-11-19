import sqlite3


def create_sqlite_db_connection():
    return sqlite3.connect("../database/my_youtube_music_playlist.db")


# <<-- DB 초기화 관련 util function
def check_sqlite_db_table():
    conn = create_sqlite_db_connection()
    cursor = conn.cursor()

    sql_select_table_names = "SELECT name FROM sqlite_master " \
                             "WHERE type IN ('table', 'view') " \
                             "AND name NOT LIKE 'sqlite_%' " \
                             "UNION ALL " \
                             "SELECT name FROM sqlite_temp_master " \
                             "WHERE type IN ('table', 'view') ORDER BY 1"

    print("==> DB 목록 확인")
    cursor.execute(sql_select_table_names)
    rows = cursor.fetchall()

    is_table_exists = {
        "playlist": False,
        "music_list": False
    }

    for row in rows:
        if row[0] == "playlist":
            is_table_exists['playlist'] = True
        if row[0] == "music_list":
            is_table_exists['music_list'] = True
    conn.close()

    print(f"플레이리스트 목록\t : {'양호' if is_table_exists['playlist'] else '확인불가'}")
    print(f"노래 목록\t\t\t : {'양호' if is_table_exists['music_list'] else '확인불가'}")
    print("")
    return is_table_exists


def create_playlist_table():
    conn = create_sqlite_db_connection()
    cursor = conn.cursor()
    sql_create_playlist_table = "CREATE TABLE playlist (" \
                                "       id INTEGER PRIMARY KEY AUTOINCREMENT," \
                                "       name TEXT UNIQUE NOT NULL," \
                                "       create_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP " \
                                ")"
    cursor.execute(sql_create_playlist_table)
    conn.close()


def delete_playlist_table():
    conn = create_sqlite_db_connection()
    cursor = conn.cursor()
    sql_delete_playlist_table = "DROP TABLE playlist"
    cursor.execute(sql_delete_playlist_table)
    conn.close()
    print("플레이리스트 목록\t : 삭제")

    return False


def create_music_list_table():
    conn = create_sqlite_db_connection()
    cursor = conn.cursor()
    sql_create_music_list_table = "CREATE TABLE music_list (" \
                                  "     id INTEGER PRIMARY KEY AUTOINCREMENT," \
                                  "     title TEXT NOT NULL," \
                                  "     musician TEXT NOT NULL," \
                                  "     url TEXT NOT NULL," \
                                  "     playlist_id INTEGER," \
                                  "     create_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP," \
                                  "     FOREIGN KEY (playlist_id) REFERENCES playlist (id)" \
                                  ")"
    cursor.execute(sql_create_music_list_table)
    conn.close()


def delete_music_list_table():
    conn = create_sqlite_db_connection()
    cursor = conn.cursor()
    sql_delete_playlist_table = "DROP TABLE music_list"
    cursor.execute(sql_delete_playlist_table)
    conn.close()
    print("노래 목록\t\t\t : 삭제")

    return False


# -->>

# <<-- playlist 관련 util function
def insert_playlist(conn, playlist_name):
    cursor = conn.cursor()

    sql_playlist_insert = f"INSERT INTO playlist(name) VALUES ('{playlist_name}')"
    cursor.execute(sql_playlist_insert)
    created_playlist_id = select_playlist(conn, playlist_name)

    return created_playlist_id


def select_playlist(conn, playlist_name):
    cursor = conn.cursor()

    sql_playlist_search = f"SELECT * FROM playlist WHERE name = '{playlist_name}'"
    cursor.execute(sql_playlist_search)
    playlist_id = cursor.fetchall()[0][0]

    return playlist_id


# -->>

# <<-- music_list 관련 util function
def insert_music_list(conn, playlist_id, music_list):
    cursor = conn.cursor()
    count = 0
    for music in music_list:
        if music['link']:
            sql_insert_music_list = "INSERT INTO music_list(title, musician, url, playlist_id) VALUES(?, ?, ?, ?)"
            cursor.execute(sql_insert_music_list, (music['title'], music['musician'], music['url'], playlist_id))
            count = count + 1

    return count
# -->>
