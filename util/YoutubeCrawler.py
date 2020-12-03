from bs4 import BeautifulSoup
import requests
import json


def youtube_crawler(URL):
    crawling_result = []
    row = -1
    result = requests.get(URL)

    if result.status_code != 200:
        return {"error": f"[{result.status_code}] 연결에 실패하였습니다."}

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
        yt_json_data = json.loads("{" + temp + "}")["metadataRowContainerRenderer"]["rows"]

    for index, value in enumerate(yt_json_data):
        # print(value)
        # continue
        if "metadataRowRenderer" in value:
            data = value["metadataRowRenderer"]
            simple_text = data["title"]["simpleText"]

            if simple_text != "노래" and simple_text != "아티스트":
                continue
            if simple_text == "노래":
                crawling_result.append({"link": False, "title": "", "musician": "", "url": ""})
                row += 1

            contents = data["contents"][0]
            if simple_text == "노래":
                if "simpleText" in contents:
                    crawling_result[row]["title"] = contents["simpleText"]
                else:
                    crawling_result[row]["title"] = contents["runs"][0]["text"]
                    url = contents["runs"][0]["navigationEndpoint"]["commandMetadata"][
                        "webCommandMetadata"]["url"]
                    url = url.replace("/watch?v=", "")
                    crawling_result[row]["url"] = url
                    crawling_result[row]["link"] = True
            elif simple_text == "아티스트":
                # print(contents)
                if "simpleText" in contents:
                    crawling_result[row]["musician"] = contents["simpleText"]
                else:
                    crawling_result[row]["musician"] = contents["runs"][0]["text"]
    return crawling_result
