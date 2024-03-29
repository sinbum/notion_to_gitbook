# -*- coding: utf-8 -*-
import json

from pyPackage.method import notionAPI as N_API
from pyPackage.method import WordCloud as WC_API
import pyPackage.envMain
import pyPackage.convertNotionToMd
import pyPackage.GitMain
import os
import json

git = pyPackage.GitMain
env = pyPackage.envMain
convertN2M = pyPackage.convertNotionToMd

## dbID입력
URL = N_API.getUrl(env.DB_ID)
HEADER = N_API.getHeader(env.NOTION_TOKEN)
DATA = {}

## API 요청

notionJson = N_API.submmitRequestToJson(URL, HEADER, DATA)
notionDic = json.loads(notionJson)
notionJsonSecond = N_API.AddNextCursor(URL, HEADER, notionDic['has_more'], notionDic['next_cursor'])

notionMd = convertN2M.getTableResult(notionDic)
notionWordCloudImage = WC_API.part_csv_Maker(notionDic)

## 지정한 경로에 MD파일 저장 또는 업데이트

if not os.path.exists('./about'):
    os.mkdir('./about')

with open('about/interest.md', 'w', encoding='utf-8') as file:
    file.write(notionWordCloudImage)
    file.write(notionMd)

##로컬에 저장
# N_API.saveNotionResponse(notionJSON)
# N_API.saveNotionResponseYaml(notionJSON)

##깃에 업데이트
# git.add()
# git.commit()
# git.push()

