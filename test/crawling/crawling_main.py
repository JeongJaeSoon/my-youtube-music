# from bs4 import BeautifulSoup
# import requests
# import json
#
#
# def bs4_ver(URL):
#     crawling_result = []
#     row = -1
#     result = requests.get(URL)
#
#     if result.status_code != 200:
#         return {"error": f"[{result.status_code}] 연결에 실패하였습니다."}
#
#     soup = BeautifulSoup(result.text, "html.parser")
#     scripts = soup.find_all("script")
#     yt_initial_data = scripts[32]
#     yt_json_data = ""
#
#     # get json
#     for _, script in enumerate(yt_initial_data):
#         script_str = str(script).strip()
#         start = script_str.find("metadataRowContainerRenderer") - 1
#         end = script_str.find("showMoreText") - 3
#         temp = script_str[start:end]
#         yt_json_data = json.loads("{" + temp + "}")["metadataRowContainerRenderer"]["rows"]
#
#     for index, value in enumerate(yt_json_data):
#         # print(value)
#         # continue
#         if "metadataRowRenderer" in value:
#             data = value["metadataRowRenderer"]
#             simple_text = data["title"]["simpleText"]
#
#             if simple_text != "노래" and simple_text != "아티스트":
#                 continue
#             if simple_text == "노래":
#                 crawling_result.append({"link": False, "title": "", "musician": "", "url": ""})
#                 row += 1
#
#             contents = data["contents"][0]
#             if simple_text == "노래":
#                 if "simpleText" in contents:
#                     crawling_result[row]["title"] = contents["simpleText"]
#                 else:
#                     crawling_result[row]["title"] = contents["runs"][0]["text"]
#                     crawling_result[row]["url"] = contents["runs"][0]["navigationEndpoint"]["commandMetadata"][
#                         "webCommandMetadata"]["url"]
#                     crawling_result[row]["link"] = True
#             elif simple_text == "아티스트":
#                 # print(contents)
#                 if "simpleText" in contents:
#                     crawling_result[row]["musician"] = contents["simpleText"]
#                 else:
#                     crawling_result[row]["musician"] = contents["runs"][0]["text"]
#     return crawling_result
#
#
# # youtube_url = input("음악 정보를 크롤링할 URL 을 입력해주세요.\n").strip()
# urls = [
#     "https://www.youtube.com/watch?v=NqmY7gveaUY",
#     "https://www.youtube.com/watch?v=Zf497FZfDp4",
#     "https://www.youtube.com/watch?v=1pvOgxRQVDM",
#     "https://www.youtube.com/watch?v=arQ13uAvnrM",
#     "https://www.youtube.com/watch?v=gkIxUlJ8bvs",
#     "https://www.youtube.com/watch?v=gkIxUlJ8bvs",
#     "https://www.youtube.com/watch?v=_WXvQz4sjBU",
#     "https://www.youtube.com/watch?v=Z1tAwwrhLAA",
#     "https://www.youtube.com/watch?v=I-2WgNnX1IU",
#     "https://www.youtube.com/watch?v=2NJLODCorFk"
# ]

# err_count = 0
# for i in range(1):
#     for index, url in enumerate(urls):
#         print(f"[{index + 1}]", url)
#         try:
#             results = bs4_ver(url)
#         except Exception:
#             err_count += 1
#             print("데이터 조회에 실패하였습니다.")
#         else:
#             for result in results:
#                 print(result)
#         print()
#
# print(err_count)

# results = bs4_ver(urls[0])
# print(results)
