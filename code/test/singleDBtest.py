#!/usr/bin/evn python
# coding=utf-8
import unittest
import pymysql


class DBSingleTest(unittest.TestCase):

    def testDB(self):

        try:
            db = pymysql.connect(host="127.0.0.1", user="root",
                                 password="root", db="simple_db", port=3306)

            cursor = db.cursor()
            # 使用 execute() 方法执行 SQL，如果表存在则删除
            cursor.execute("DROP TABLE IF EXISTS EMPLOYEE")
            # 使用预处理语句创建表
            sql = """CREATE TABLE EMPLOYEE (
                             FIRST_NAME  CHAR(20) NOT NULL,
                             LAST_NAME  CHAR(20),
                             AGE INT,  
                             SEX CHAR(1),
                             INCOME FLOAT )"""
            cursor.execute(sql)
            # 提交
            db.commit()

        except Exception as e:

            print('连接数据库失败：' + str(e.args))
            db.rollback()
            # 使用cursor()方法获取操作游标


        finally:
            print('数据库关闭')
            db.close()




if __name__ == '__main__':
    unittest.main()
