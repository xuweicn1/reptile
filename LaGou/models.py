import sqlite3 as lite


class Database():

    def __init__(self, db='lagou.db'):
        self.con = lite.connect(db, check_same_thread=False)
        self.cur = self.con.cursor()

    def create_lagou_position(self):
        """拉钩招聘表"""
        with self.con:
            sql = """create table position(
                            ID  INTEGER PRIMARY KEY AUTOINCREMENT,
                            position text,
                            city text,
                            area text,
                            release_time text,
                            money text,
                            need text,
                            company text,
                            tag text,
                            welfare text,
                            industry text)"""
            self.cur.execute("DROP TABLE IF EXISTS position")
            self.cur.execute(sql)

    def insert_position(self, position, city, area,release_time, money, need, company, tag, welfare, industry):
        """插入招聘信息"""
        with self.con:
            sql = "INSERT INTO position(position, city, area,release_time, money, need, company, tag, welfare,industry) VALUES(?, ?, ?,?,?,?, ?,?, ?, ?)"
            self.cur.execute(sql, (position, city, area,release_time,
                                   money, need, company, tag, welfare, industry))
            print('插入成功', city, area,company,position)

    def SELECT_position(self, username):
        """获取用户信息"""
        with self.con:
            sql = "SELECT * FROM position"
            self.cur.execute(sql)
            return self.cur.fetchall()


if __name__ == '__main__':

    db = Database()
    db.create_lagou_position()
    # db.insert_position('a','b','c','d','1','2','3','4')
