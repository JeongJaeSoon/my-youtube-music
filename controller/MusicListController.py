import sqlite3
from controller.Controller import Controller


class MusicListController(Controller):
    def add_music_list(self, playlist_id, musics):
        # 플레이리스트가 존재하지 않는 경우
        playlist = self.playlist.check_playlist(self.cursor, playlist_id)
        if playlist is False:
            return "존재하지 않는 플레이리스트입니다."

        playlist_name = self.playlist.select_playlist(self.cursor, 'id', playlist_id)[1]
        count = self.music_list.insert_music_list(self.cursor, playlist_id, musics)
        if count == 0:
            return f"플레이리스트에 새롭게 추가된 음악이 없습니다."

        self.conn.commit()
        return f"'{playlist_name}' 에 새롭게 {count}곡이 추가되었습니다.\n(중복곡 제외)"

    def delete_music_list(self, musics):
        deleted_music_count = self.music_list.delete_musics(self.cursor, musics)
        if deleted_music_count == 0:
            return "삭제된 음악이 없습니다."

        self.conn.commit()
        return f"{deleted_music_count}곡이 삭제되었습니다."
