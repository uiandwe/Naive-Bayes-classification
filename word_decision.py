from konlpy.tag import Kkma
import pymysql
conn = pymysql.connect(host='127.0.0.1', user='root', passwd='123qwe', db='word', charset='utf8')
cur = conn.cursor()
kkma = Kkma()


#조건부 확률 계산
def conditional_probability(test, train_table, all_count, table_count):
    counter = 0
    list_count = []

    #해당 문장이 해당 테이블에 존재 하는지 확인
    for word in test:
        cur.execute("SELECT count(*) as cnt  FROM "+train_table+" where word = '"+word+"'")
        for cnt in cur:
            if int(cnt[0]) > 0:
                counter += 1

        list_count.append(counter)
        counter = 0

    print(list_count)

    cal_list = []
    for j in range(len(list_count)):
        #다음에 * 연산할떄 0이 되지 않기 위해 +1을 해줌
        cal_list.append((list_count[j]+1)/float(table_count+all_count))
    result = 1
    for j in range(len(cal_list)):
        result *= float(round(cal_list[j], 6))

    return_value = float(result)*float(1.0/2.0)
    print(return_value)
    return return_value

# get the data
input_file = open('input.txt', 'r')

list_positive = []
list_negative = []

#형태소 분리
input_line = input_file.readline()
input_kkma = kkma.pos(input_line)

print(input_kkma)

test_output = []
for i in input_kkma:
    test_output.append(i[0])

#긍정 단어 전체 갯수
cur.execute("SELECT count(*) as cnt  FROM positive ")
positive_count = 0
for response in cur:
    positive_count = int(response[0])

#부정 단어 전체 갯수
cur.execute("SELECT count(*) as cnt  FROM negative ")
negative_count = 0
for response in cur:
    negative_count = int(response[0])

# naive bayes 값 계산
result_pos = conditional_probability(test_output, 'positive', positive_count+negative_count, positive_count)
result_neg = conditional_probability(test_output, 'negative', positive_count+negative_count, negative_count)

if result_pos > result_neg:
    print(u'긍정')
else:
    print(u'부정')
