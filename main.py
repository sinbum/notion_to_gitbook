# -*- coding: utf-8 -*-
import json

from pyPackage.method import notionAPI
import pyPackage.envMain
import pyPackage.convertNotionToMd
import pyPackage.GitMain
import os

# Path and Config_file
PWD = os.path.abspath("./")
UPDATE_FILE_PATE = PWD+'/resources/blog/about/interest.md'
CONFIG_FILE = pyPackage.envMain.config_read(os.path.abspath("./config.cfg"))


#use function
git = pyPackage.GitMain
convert = pyPackage.convertNotionToMd
notion_db_id = pyPackage.envMain.get_notion_db_id(CONFIG_FILE)
notion_token = pyPackage.envMain.get_notion_token(CONFIG_FILE)


## dbID입력
URL =  notionAPI.getUrl(notion_db_id)
HEADER = notionAPI.getHeader(notion_token)

## API 요청
def mainExe():
    notionJSON = notionAPI.submmitRequestToJson(URL,HEADER)
    notionDic = json.loads(notionJSON)
    notionMd = convert.getTableResult(notionDic)


    ## 지정한 경로에 MD파일 저장 또는 업데이트
    file = open( UPDATE_FILE_PATE , 'w', encoding='utf-8')
    file.write(notionMd)
    file.close()

##깃에 업데이트
def git_update_exe():
    git.add()
    git.commit(COMMIT_MESSGE)
    git.push()







