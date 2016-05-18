__author__ = 'hyeonsj'
import pymysql
import init


class Connect:

    conn = None
    cur = None

    def __init__(self):
        try:
            conn = pymysql.connect(host=init.host, user=init.user, passwd=init.passwd, db=init.db, charset=init.charset)
            self.conn = conn
            self.cur = conn.cursor()
        except pymysql.InternalError as error:
            code, message = error.args
            print(">>>>>>>>>>>>>", code, message)

    def get_cursor(self):
        return self.cur

    def find(self, sql):
        return_cur = None

        try:
            self.cur.execute(sql)
            for response in self.cur:
                return_cur = response[0]
        except pymysql.InternalError as error:
            code, message = error.args
            print(">>>>>>>>>>>>>", code, message)

        return return_cur

    def close_db(self):
        try:
            self.cur.close()
            self.conn.close()
        except pymysql.InternalError as error:
            code, message = error.args
            print(">>>>>>>>>>>>>", code, message)



