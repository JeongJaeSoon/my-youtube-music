from model.Model import Model


class PlayList(Model):
    # 플레이리스트 생성
    def insert_playlist(self, cursor, playlist_name):
        sql_playlist_insert = f"INSERT INTO playlist(name) VALUES ('{playlist_name}')"
        cursor.execute(sql_playlist_insert)
        created_playlist_id = self.select_playlist(cursor, 'name', playlist_name)

        return created_playlist_id

    # 플레이리스트 검색
    def select_playlist(self, cursor, column_name, playlist_name):
        sql_playlist_search = f"SELECT * FROM playlist WHERE {column_name} = '{playlist_name}'"
        cursor.execute(sql_playlist_search)
        playlist_id = cursor.fetchall()[0][0]

        return playlist_id
