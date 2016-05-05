__author__ = 'hyeonsj'
import re
from konlpy.tag import Kkma
from konlpy.utils import pprint


def remove_tag(mystring):
    #태그 제거
    mystring = re.sub('<[^>]*>', '', mystring)
    #숫자 제거
    mystring = re.sub('[\d]+', '', mystring)[1:]
    #콤마 구분
    mystring = re.sub(',', '.', mystring)[1:]
    #\n 구분
    mystring = re.sub('\n', '.', mystring)[1:]
    #영문 제거
    mystring = re.sub('[a-zA-Z]+', '.', mystring)[1:]

    #가로 안 제거
    mystring = re.sub('\([가-힣a-zA-Z]+\)', '', mystring)
    #가로가로 제거
    mystring = re.sub('\([\(가-힣·\) a-z A-Z]+\)', '', mystring)
    #대가로 제거
    mystring = re.sub('\[[가-힣 a-z A-Z]+\]', '', mystring)
    #특수시호 제거
    mystring = re.sub('[\{\}\[\]\/?,;:|\)*~`!^\-_+<>@\#$%&\\\=\(\'\"…]+', '', mystring)

    #none 제거
    line_list = [x.strip() for x in mystring.split('.') if x != '']

    #none 제거
    result = [x for x in line_list if x]
    #가로 안 없애기

    return result

import pymysql
conn = pymysql.connect(host='127.0.0.1', user='root', passwd='123qwe', db='word', charset='utf8')
cur = conn.cursor()
kkma = Kkma()

f = open("negative.txt", "r")
while True:
    line = f.readline()
    if not line:
        break
    temp_list = remove_tag(line)
    for word in temp_list:
        temp_list = kkma.pos(word)
        cur.execute("SELECT count(*) as cnt  FROM negative where word = '"+temp_list[0][0]+"'")

        for response in cur:
            if int(response[0]) > 0:
                pass
            else:
                cur.execute("INSERT INTO negative(word, type) values('"+temp_list[0][0]+"', '"+temp_list[0][1]+"')")
                conn.commit()
            break

cur.close()
conn.close()
f.close()