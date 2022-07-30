# -*- coding: utf-8 -*-
import json

from pyPackage.method import notionAPI as API
import pyPackage.envMain
import pyPackage.convertNotionToMd
import pyPackage.GitMain

git = pyPackage.GitMain
env = pyPackage.envMain
convertN2M = pyPackage.convertNotionToMd

## dbID입력
URL =  API.getUrl(env.DB_ID)
HEADER = API.getHeader(env.NOTION_TOKEN)

## API 요청

notionJSON = API.submmitRequestToJson(URL,HEADER)
notionDic = json.loads(notionJSON)
notionMd = convertN2M.getTableResult(notionDic)

## 지정한 경로에 MD파일 저장 또는 업데이트
with open('about/interest.md', 'w', encoding='utf-8') as file:
    file.write(notionMd)

##로컬에 저장
API.saveNotionResponse(notionJSON)

##깃에 업데이트
git.add()
git.commit()
git.push()


