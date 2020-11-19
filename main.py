from controller.Controller import Controller
from controller.PlayListController import PlayListController

Controller().init_database()

# <<-- TEST DATA CODE -->>
playlist_name = "기분 좋아지는 노래3"
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

# PlayListController().create_playlist(playlist_name, music_list)
PlayListController().create_playlist(playlist_name)

# TODO 플레이리스트 이름 수정
# TODO 플레이리스트에 음악 추가(여러곡 또는 한곡)
# TODO 플레이리스트에서 음악 삭제(여러곡 또는 한곡)
# TODO 플레이리스트 삭제
