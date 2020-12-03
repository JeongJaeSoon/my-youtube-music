from util.YoutubeCrawler import youtube_crawler
from controller.Controller import Controller


class CrawlerController(Controller):

    def get_music_list(self, URL):
        try:
            result = youtube_crawler(URL)
        except Exception:
            return "음악 목록 조회에 실패하였습니다."

        if len(result) == 0:
            return "등록된 음악 정보가 없습니다."

        return result
