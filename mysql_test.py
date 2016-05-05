import pymysql
conn = pymysql.connect(host='127.0.0.1', user='root', passwd='123qwe', db='word', charset='utf8')

cur = conn.cursor()


cur.execute("SELECT count(*) as cnt  FROM positive where word = '훌륭한'")
for response in cur:
    if int(response[0]) > 0:
        print("111")
    else:
        print("222")
    break
cur.close()
conn.close()