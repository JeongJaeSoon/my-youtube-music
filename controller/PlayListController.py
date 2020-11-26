import sqlite3
from controller.Controller import Controller


class PlayListController(Controller):
    def create_playlist(self, playlist_name, musics=None):
        if musics is None:
            musics = []

        count = 0

        try:
            # 플레이리스트 생성 및 음악 목록 저장
            playlist_id = self.playlist.insert_playlist(self.cursor, playlist_name)[0]

            # 플레이리스트 생성 시 음악 목록에 추가될 경우
            is_insert_music = True if len(musics) != 0 else False
            if is_insert_music:
                count = self.music_list.insert_music_list(self.cursor, playlist_id, musics)
        except sqlite3.IntegrityError:
            return "이미 저장된 플레이리스트 이름입니다."
        # TODO 예외 처리 수정
        # except Exception:
        #     return "알 수 없는 오류로 종료되었습니다."
        else:
            self.conn.commit()
            msg = f"플레이리스트 '{playlist_name}' 이(가) 생성되었습니다.\n" + \
                  (f"({count}곡 저장 완료)" if is_insert_music else "")
            return msg

    def modify_playlist_name(self, playlist_id, new_playlist_name):
        # 플레이리스트가 존재하지 않는 경우
        playlist = self.playlist.check_playlist(self.cursor, playlist_id)
        if playlist is False:
            return "존재하지 않는 플레이리스트입니다."

        # 플레이리스트 이름이 변경되지 않을 경우
        if playlist[1] == new_playlist_name:
            return "기존 플레이리스트 이름과 동일합니다."

        try:
            # 플레이리스트 이름 변경 결과를 반환
            updated_playlist = self.playlist.update_playlist_name(self.cursor, playlist_id, new_playlist_name)
        except sqlite3.IntegrityError:
            return "이미 저장된 플레이리스트 이름입니다."
        # TODO 예외 처리 수정
        except Exception:
            return "알 수 없는 오류로 종료되었습니다."

        # 이름 변경 성공 시
        if updated_playlist[1] == new_playlist_name:
            self.conn.commit()
            return f"플레이리스트 이름이 '{new_playlist_name}' (으)로 변경되었습니다."
        # 이름 변경 실패 시
        else:
            return "플레이리스트 이름 변경에 실패하였습니다."

    def destroy_playlist(self, playlist_id):
        # 플레이리스트가 존재하지 않는 경우
        playlist = self.playlist.check_playlist(self.cursor, playlist_id)
        if playlist is False:
            return "존재하지 않는 플레이리스트입니다."

        delete_playlist = self.playlist.delete_playlist(self.cursor, playlist_id)
        delete_music_list = self.music_list.delete_playlist_music(self.cursor, playlist_id)

        if delete_playlist is None and delete_music_list is None:
            self.conn.commit()
            return f"'{playlist[1]}' 플레이리스트가 삭제되었습니다."
