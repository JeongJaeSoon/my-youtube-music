from model.Model import Model


class PlayList(Model):

    def check_playlist(self, cursor, playlist_id):
        playlist = self.select_playlist(cursor, 'id', playlist_id)

        if playlist is None:
            return False

        return playlist

    # 플레이리스트 조회
    def select_playlist_all(self, cursor):
        sql_playlist_select = "SELECT * FROM playlist"
        cursor.execute(sql_playlist_select)
        playlists = cursor.fetchall()

        return playlists

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
        try:
            playlist = cursor.fetchall()[0]
        except IndexError:
            return None

        return playlist

    def update_playlist_name(self, cursor, playlist_id, new_playlist_name):
        sql_playlist_name_update = f"UPDATE playlist SET name = '{new_playlist_name}' WHERE id = {playlist_id}"
        cursor.execute(sql_playlist_name_update)
        updated_playlist = self.select_playlist(cursor, 'id', playlist_id)

        return updated_playlist

    def delete_playlist(self, cursor, playlist_id):
        sql_playlist_delete = f"DELETE FROM playlist WHERE id = {playlist_id}"
        cursor.execute(sql_playlist_delete)
        deleted_playlist = self.select_playlist(cursor, 'id', playlist_id)

        return deleted_playlist
