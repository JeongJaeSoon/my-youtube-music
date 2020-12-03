from controller.Controller import Controller
from controller.PlayListController import PlayListController
from controller.MusicListController import MusicListController
from controller.CrawlerController import CrawlerController

Controller().init_database()

# <<-- TEST DATA CODE -->>
playlist_name = "기분 좋아지는 노래1"
music_list = [
    {'link': True, 'title': 'Good Vibes', 'musician': 'HRVY, Matoma', 'url': 'Q1Yy0tNWtnE'},
    {'link': True, 'title': 'Push-ups', 'musician': 'Scarlet Pleasure', 'url': 'aXGOieAtYzk'},
    {'link': True, 'title': 'monday', 'musician': 'somegirlnamedanna', 'url': 'BO4PaNmqAkA'},
    {'link': True, 'title': 'happiness', 'musician': 'John K', 'url': 'oUcYb0iOivU'},
    {'link': True, 'title': 'On and On', 'musician': 'PREP', 'url': 'sqR9V-D6pQw'},
    {'link': True, 'title': 'OK Not To Be OK', 'musician': 'Marshmello, Demi Lovato',
     'url': 'eOPW5geTnEI'},
    {'link': True, 'title': 'Grateful', 'musician': '13 Crowns', 'url': 'a9-QT63rD5Y'},
    {'link': True, 'title': 'WAIT FOR YOU', 'musician': 'Jake Miller', 'url': 'Ttt-YV79KbY'},
    {'link': True, 'title': 'Lemonade', 'musician': 'Circa Waves', 'url': 'Bv12KhnJomc'},
    {'link': True, 'title': 'Backyard Boy', 'musician': 'Claire Rosinkranz, Jeremy Zucker',
     'url': 'WmnnvfP-j0k'},
]

# print(PlayListController().create_playlist(playlist_name, music_list))
# print(PlayListController().create_playlist(playlist_name))

# TODO 플레이리스트 목록 가져오기
# TODO 플레이리스트의 음악 목록 가져오기

# print(PlayListController().modify_playlist_name(5, "atsseddㅇfst"))
# print(PlayListController().destroy_playlist(1))
# print(MusicListController().delete_music_list([22, 23, 24]))

urls = [
    "https://www.youtube.com/watch?v=NqmY7gveaUY",
    "https://www.youtube.com/watch?v=Zf497FZfDp4",
    "https://www.youtube.com/watch?v=1pvOgxRQVDM",
    "https://www.youtube.com/watch?v=arQ13uAvnrM",
    "https://www.youtube.com/watch?v=gkIxUlJ8bvs",
    "https://www.youtube.com/watch?v=gkIxUlJ8bvs",
    "https://www.youtube.com/watch?v=_WXvQz4sjBU",
    "https://www.youtube.com/watch?v=Z1tAwwrhLAA",
    "https://www.youtube.com/watch?v=I-2WgNnX1IU",
    "https://www.youtube.com/watch?v=2NJLODCorFk"
]

# print(CrawlerController().get_music_list(urls[0]))
# print(CrawlerController().get_music_list("https://www.youtube.com/watch?v=DFH2NpzgQ2E"))

print(PlayListController().index_playlist())
print(MusicListController().index_music_list(14))
print(PlayListController().destroy_playlist(14))
print(MusicListController().index_music_list(14))
