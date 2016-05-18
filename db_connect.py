__author__ = 'hyeonsj'
import pymysql
import init


class Connect:

    conn = None
    cur = None

    def __init__(self):
        conn = pymysql.connect(host=init.host, user=init.user, passwd=init.passwd, db=init.db, charset=init.charset)
        self.conn = conn
        self.cur = conn.cursor()

    def get_cursor(self):
        return self.cur

    def find(self, sql):
        return_cur = None
        self.cur.execute(sql)
        for response in self.cur:
            return_cur = response[0]
        return return_cur

    def close_db(self):
        self.cur.close()
        self.conn.close()



