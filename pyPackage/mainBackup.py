# -*- coding: utf-8 -*-

import requests
import json

# 같은경로에 envMain 파일 추가로 토큰값을 가져옴.
from blog.pyPackage import envMain

headers = {
    'Authorization': 'Bearer ' + envMain.NOTION_TOKEN,
    'Content-Type': 'application/json',
    'Notion-Version': '2022-02-22'
}

dbId = "100faa3de8dd44198ceb878c4784a7f7"
url = "https://api.notion.com/v1/databases/" + dbId + "/query"

# 제이슨 형태로 출력.
response = requests.post(url, headers=headers).json()




# 제이슨형태로 현재 경로에 저장.
file = open('./DB/notionResponse.json', 'w', encoding='utf-8')

# print(response, file=file)
# print(json.dumps(response, indent=4, sort_keys=True))
response = json.dumps(response, indent=4, sort_keys=True, ensure_ascii=False)
print(response, file=file)






