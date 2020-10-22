from bs4 import BeautifulSoup
import requests
import json


def bs4_ver(URL):
    crawling_result = []
    result = requests.get(URL)
    soup = BeautifulSoup(result.text, "html.parser")
    scripts = soup.find_all("script")
    yt_initial_data = scripts[32]
    yt_json_data = ""

    # get json
    for _, script in enumerate(yt_initial_data):
        script_str = str(script).strip()
        start = script_str.find("metadataRowContainerRenderer") - 1
        end = script_str.find("showMoreText") - 3
        temp = script_str[start:end]
        yt_json_data = json.loads("{" + temp + "}")['metadataRowContainerRenderer']['rows']

    for index, value in enumerate(yt_json_data):
        crawling_result.append({"title": "", "musician": "", "url": ""})

        if "metadataRowRenderer" in value:
            data = value['metadataRowRenderer']
            simple_text = data['title']['simpleText']

            if simple_text == "노래" or simple_text == "아티스트":
                contents = data['contents'][0]
                row = index // 3 - 1
                if index % 3 == 0:
                    crawling_result[row]["title"] = contents['runs'][0]["text"]
                    crawling_result[row]["url"] = contents["runs"][0]["navigationEndpoint"]["commandMetadata"][
                        "webCommandMetadata"]["url"]
                elif index % 3 == 1:
                    if "simpleText" in contents:
                        crawling_result[row]["musician"] = contents["simpleText"]
                    else:
                        crawling_result[row]["musician"] = contents["runs"][0]["text"]
    return crawling_result


# youtube_url = input("음악 정보를 크롤링할 URL 을 입력해주세요.\n").strip()
youtube_url = "https://www.youtube.com/watch?v=NqmY7gveaUY"

result = bs4_ver(youtube_url)
for i in result:
    print(i)
