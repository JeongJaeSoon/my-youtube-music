import sqlite3
from model.Model import Model


class MusicList(Model):
    def __init__(self):
        super().__init__()

    # 음악목록 저장
    def insert_music_list(self, cursor, playlist_id, music_list):
        count = 0
        for music in music_list:
            if music['link']:
                sql_insert_music_list = "INSERT INTO music_list(title, musician, url, playlist_id) VALUES(?, ?, ?, ?)"
                cursor.execute(
                    sql_insert_music_list,
                    (music['title'], music['musician'], music['url'], playlist_id)
                )
                count = count + 1

        return count
