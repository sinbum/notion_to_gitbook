# def rowsForSpark(list):
#     i = 1
#     rows = []
#
#     for row in list:
#         rows.append(Row(sqNo=i, part_small_name=row))
#         i += 1
#
#     return rows
#
import os

import pandas as pd


def allGetterListToOne(list):
    result_list = []
    for row_list in list:

        if row_list is None: continue

        if len(row_list) > 1:
            for row in row_list:
                result_list.append(row)
            else:
                result_list.append(row_list[0])

    return result_list


def part_csv_Maker(notionDic):
    part_small = []
    part_middle = []
    part_big = []

    # 함수 선언부.
    def getPartSmall(part_small_list):
        resultList = []

        if (len(part_small_list) < 1): return None

        for part_small_row in part_small_list:
            resultList.append(part_small_row['name'])
        return resultList

    def getPartMiddle(middle_name):
        if middle_name is None:
            return None
        else:
            return middle_name['name']

    def getPartBig(big_name):

        if big_name is None:
            return None

        return big_name['name']

    def struct_maker(part_list):
        resultList = []
        i = 1
        for row in part_list:
            resultList.append([i, row])
            i += 1
        return resultList

    # 실행부

    for row in notionDic['results']:
        row_small_list = getPartSmall(row['properties']['소분류']['multi_select'])
        row_middle_name = getPartMiddle(row['properties']['중분류']['select'])
        row_big_name = getPartBig(row['properties']['대분류']['select'])

        part_small.append(row_small_list)
        part_middle.append(row_middle_name)
        part_big.append(row_big_name)

    part_small = allGetterListToOne(part_small)
    part_middle = list(filter(None, part_middle))
    part_big = list(filter(None, part_big))

    part_small = struct_maker(part_small)

    ## id 객체 id 넘버도 필요. 키값으로.
    ## ,columns=['sequenceNo', 'smallPartName']
    df = pd.DataFrame(data=part_small)
    path = os.path.abspath('./pyPackage/test')

    df.to_csv(path_or_buf=path + '\part_small.csv', header=['sequenceNo', 'smallPartName'], index_label=['index'])

    print(path)

    # print(part_small)

    # 프레임 만들기 (대분류)

    # 프레임 만들기 (중분류)

    # 프레임 만들기 (소분류)

    # 모두 조인

    # 워드 클라우드 이미지 생성.

    # 워드 클라우드 이미지 저장.

    # ![{WordCloud_image_날짜}](이미지 경로)
    return "image"
