def parseMiddleSelect(middle_select):
    if middle_select is None:
        middle_select = '주제X'
        return middle_select

    return middle_select['name']


def parseMultiSelect(multiSelects):
    resultList = []

    if multiSelects == 0:
        return multiSelects

    for row in multiSelects:
        multiSelect = row['name']
        resultList.append(multiSelect)

    return resultList


def getTableResult(notion_DicType):
    # 기본 변수 선언
    description = "---" \
                  "\ndescription: 아래 interest 페이지는 저의 개인적인 흥미 및 관심사를 노션으로 스크래핑 한 모음으로, 노션API를 사용해 자동으로 작성되었습니다."\
                  "\ncover: >-"\
                  "\n  https://images.unsplash.com/photo-1580927752452-89d86da3fa0a?crop=entropy&cs=tinysrgb&fm=jpg&ixid=MnwxOTcwMjR8MHwxfHNlYXJjaHw1fHxjb2Rpbmd8ZW58MHx8fHwxNjU1NTM0Njc2&ixlib=rb-1.2.1&q=80" \
                  "\ncoverY: 263.4640234948605" \
                  "\n---"



    header = "\n\n# 개발 관심 흥미도(시간순)"
    newline = "\n---"
    tableColumn = "\n|주제|이름|태그|참고링크|"
    talbeFormat = "\n|:--:|:-----------------------------------------------|:-----:|:---:|"

    mdTable = description + \
              header + \
              newline + \
              tableColumn + \
              talbeFormat

    mdLines = []

    # 제이슨 리스트 내 한줄 출력
    for row in notion_DicType['results']:
        ## 이름
        name = row['properties']['이름']['title'][0]['plain_text']

        ## 주제 또는 중분류
        # middle_select = row['properties']['중분류']['select']['name']
        middle_select = parseMiddleSelect(row['properties']['중분류']['select'])

        ## 태그 또는 소분류
        tagNames = row['properties']['소분류']['multi_select']
        tagNames = parseMultiSelect(tagNames)

        url = row['properties']['URL']['url']

        ## 한줄 포멧에 값 담기
        mdLine = f"""\n|{middle_select}|{name}| {tagNames} |[링크]({url})|"""

        mdLines.append(mdLine)

    # 최종 md 파일에 한줄씩 담기
    for mdLine in mdLines:
        mdTable += mdLine

    md = mdTable
    return md
