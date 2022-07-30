# -*- coding: utf-8 -*-

import requests
import json
import yaml


# header = {
#     'Authorization': 'Bearer ' + envMain.NOTION_TOKEN,
#     'Content-Type': 'application/json',
#     'Notion-Version': '2022-02-22'
# }
#
# dbId = "100faa3de8dd44198ceb878c4784a7f7"


def getUrl(dbId):
    return "https://api.notion.com/v1/databases/" + dbId + "/query"


def getHeader(NOTION_TOKEN):
    return {
        'Authorization': 'Bearer ' + NOTION_TOKEN,
        'Content-Type': 'application/json',
        'Notion-Version': '2022-02-22'
    }


def submmitRequest(url, headers):
    # 제이슨 형태로 출력.
    response = requests.post(url, headers=headers).json()
    return response


def submmitRequestToJson(url, headers):
    response = requests.post(url, headers=headers).json()
    response = json.dumps(response, indent=4, sort_keys=True, ensure_ascii=False)
    return response


# 제이슨형태로 현재 경로에 저장.

def saveNotionResponse(response):
    file = open('./pyPackage/DB/notionResponse.json', 'w', encoding='utf-8')
    print(response, file=file)
    file.close()


def saveNotionResponseYaml(response):
    file = open('./pyPackage/DB/notionResponse.yaml', 'w', encoding='utf-8')
    response_obj = json.loads(response)
    print(yaml.dump(response_obj,allow_unicode=True),file=file)
    file.close()

