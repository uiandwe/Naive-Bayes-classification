__author__ = 'hyeonsj'
import re
from konlpy.tag import Kkma
from konlpy.utils import pprint
import pymysql
conn = pymysql.connect(host='127.0.0.1', user='root', passwd='123qwe', db='word', charset='utf8')
cur = conn.cursor()
kkma = Kkma()

#naive bayes classifier + smoothing
def naive_bayes_classifier(test, train_table, all_count, table_count):
    counter = 0
    list_count = []

    for word in test:
        cur.execute("SELECT count(*) as cnt  FROM "+train_table+" where word = '"+word+"'")
        for response in cur:
            if int(response[0]) > 0:
                counter = counter + 1

        list_count.append(counter)
        counter = 0
    print(list_count)
    list_naive = []
    for i in range(len(list_count)):
        list_naive.append((list_count[i]+1)/float(table_count+all_count))
    result = 1
    for i in range(len(list_naive)):
        result *= float(round(list_naive[i], 6))
    print(float(result)*float(1.0/2.0))
    return float(result)*float(1.0/2.0)

# get the data
f_test = open('test.txt', 'r')

# tag list (보통명사, 동사, 형용사, 보조동사, 명사추정범주)
# 참고 : https://docs.google.com/spreadsheets/d/1OGAjUvalBuX-oZvZ_-9tEfYD2gQe7hTGsgUpiiBSXI8/edit#gid=0
list_tag = [u'NNG', u'VV', u'VA', u'VXV', u'UN']
list_positive = []
list_negative = []

# extract test sentence
test_line = f_test.readline()
test_list = kkma.pos(test_line)
print(test_list)
test_output = []
for i in test_list:
    if i[1] == u'SW':
        if i[0] in [u'♡', u'♥']:
            test_output.append(i[0])
    if i[1] in list_tag:
        test_output.append(i[0])

cur.execute("SELECT count(*) as cnt  FROM positive ")
positive_count = 0
for response in cur:
    positive_count = int(response[0])
cur.execute("SELECT count(*) as cnt  FROM negative ")
negative_count = 0
for response in cur:
    negative_count = int(response[0])

ALL = positive_count+negative_count

# naive bayes 값 계산
result_pos = naive_bayes_classifier(test_output, 'positive', ALL, positive_count)
result_neg = naive_bayes_classifier(test_output, 'negative', ALL, negative_count)

if result_pos > result_neg:
    print(u'긍정')
else:
    print(u'부정')
