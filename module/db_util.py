import sqlite3


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
# -->>
