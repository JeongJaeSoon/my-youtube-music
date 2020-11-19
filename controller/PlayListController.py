import sqlite3
from controller.Controller import Controller
from model.Model import Model
from model.PlayList import PlayList
from model.MusicList import MusicList


class PlayListController(Controller):
    def create_playlist(self, playlist_name, musics=None):
        if musics is None:
            musics = []

        count = 0
        is_insert_music = True if len(musics) != 0 else False
        conn, cursor = Model().get_db_conn()

        try:
            # 플레이리스트 생성 및 음악 목록 저장
            playlist_id = PlayList().insert_playlist(cursor, playlist_name)
            if is_insert_music:
                count = MusicList().insert_music_list(cursor, playlist_id, musics)
        except sqlite3.IntegrityError:
            print("중복된 이름의 플레이리스트는 저장할 수 없습니다.")
            return
        # TODO 예외 처리 수정
        # except Exception:
        #     print("알 수 없는 오류로 종료되었습니다.")
        else:
            print(f"플레이리스트 '{playlist_name}' 이(가) 생성되었습니다.")
            print(f"({count}곡 저장 완료)" if
                  is_insert_music else "", end="")
            conn.commit()
