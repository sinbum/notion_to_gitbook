# -*- coding: utf-8 -*-

import requests
import json


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

