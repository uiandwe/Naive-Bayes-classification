from konlpy.tag import Kkma
import db_connect
db = db_connect.Connect()


#조건부 확률 계산
def conditional_probability(test, train_table, all_count, table_count):
    counter = 0
    list_count = []

    #해당 문장이 해당 테이블에 존재 하는지 확인
    for word in test:
        sql = "SELECT count(*) as cnt  FROM "+train_table+" where word = '"+word+"'"
        cur = db.find(sql)
        if int(cur) > 0:
            counter += 1

        list_count.append(counter)
        counter = 0

    cal_list = []
    for j in range(len(list_count)):
        #다음에 * 연산할떄 0이 되지 않기 위해 +1을 해줌
        cal_list.append((list_count[j]+1)/float(table_count+all_count))
    result = 1
    for j in range(len(cal_list)):
        result *= float(round(cal_list[j], 6))

    return_value = float(result)*float(1.0/2.0)
    print(train_table, list_count, " value = ", return_value)
    return return_value


#입력 문장
def get_input_file():
    kkma = Kkma()
    # get the data
    input_file = open('input.txt', 'r')

    #형태소 분리
    input_line = input_file.readline()
    input_kkma_str = kkma.pos(input_line)

    return input_kkma_str


def sentence_to_kkma(word):

    if len(word) < 1:
        return False

    kkma = Kkma()
    input_kkma_str = kkma.pos(word)

    return input_kkma_str


#긍정 부정 단어 전체 갯수
def get_word_counts():

    sql = "SELECT count(*) as cnt  FROM positive "
    cur = db.find(sql)
    positive_word_count = int(cur)

    #부정 단어 전체 갯수
    sql = "SELECT count(*) as cnt  FROM negative "
    cur = db.find(sql)
    negative_word_count = int(cur)

    return positive_word_count, negative_word_count

if __name__ == '__main__':
    input_kkma = get_input_file()
    print(input_kkma)
    test_output = []
    for i in input_kkma:
        test_output.append(i[0])

    positive_count, negative_count = get_word_counts()

    # naive bayes 값 계산
    result_pos = conditional_probability(test_output, 'positive', positive_count+negative_count, positive_count)
    result_neg = conditional_probability(test_output, 'negative', positive_count+negative_count, negative_count)

    if result_pos > result_neg:
        print(u'긍정')
    else:
        print(u'부정')

    db.close_db()