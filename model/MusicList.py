import sqlite3
from model.Model import Model


class MusicList(Model):
    def __init__(self):
        super().__init__()

    # 음악 저장 시, 중복 검사
    def distinct_music_list(self, cursor, playlist_id, music_url):
        sql_music_list_select = f"SELECT COUNT(*) FROM music_list WHERE playlist_id = {playlist_id} and url = '{music_url}'"
        cursor.execute(sql_music_list_select)
        is_distinct_music = cursor.fetchall()[0][0] == 0
        return is_distinct_music

    # 재생목록에 저장된 음악목록 조회
    def select_music_list(self, cursor, playlist_id):
        sql_playlist_search = f"SELECT * FROM music_list WHERE playlist_id = '{playlist_id}'"
        cursor.execute(sql_playlist_search)
        try:
            playlist = cursor.fetchall()[0]
        except IndexError:
            return None

        return playlist

    # 음악목록 저장, 음악목록 추가
    def insert_music_list(self, cursor, playlist_id, musics):
        count = 0

        for music in musics:
            if music['link'] and self.distinct_music_list(cursor, playlist_id, music['url']):
                sql_music_list_insert = "INSERT INTO music_list(title, musician, url, playlist_id) VALUES(?, ?, ?, ?)"
                cursor.execute(
                    sql_music_list_insert,
                    (music['title'], music['musician'], music['url'], playlist_id)
                )
                count = count + 1

        return count

    def delete_playlist_music(self, cursor, playlist_id):
        sql_playlist_music_delete = f"DELETE FROM music_list WHERE playlist_id = {playlist_id}"
        cursor.execute(sql_playlist_music_delete)
        deleted_music = self.select_music_list(cursor, playlist_id)

        return deleted_music

    def delete_musics(self, cursor, musics):
        count = 0

        for music in musics:
            sql_music_list_delete = f"DELETE FROM music_list WHERE id = {music}"
            cursor.execute(sql_music_list_delete)
            count = count + 1

        return count
