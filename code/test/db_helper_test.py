#!/usr/bin/evn python
# coding=utf-8

import unittest

from help import db_helper
from help import datetime_helper
import datetime
class DbHelperTest(unittest.TestCase):
    """数据库操作包测试类"""

    def setUp(self):
        """初始化测试环境"""
        print('------ini------')

    def tearDown(self):
        """清理测试环境"""
        print('------clear------')


    def test(self):
        # 新增记录，不带return参数
        sql = """
            INSERT INTO product_class(
              id, name, is_enable,add_time)
            VALUES (%s,%s, %s,%s)
        """
        data = (4,'糖果',1,datetime.datetime.now())
        result = db_helper.write(sql, data)
        print(result)

        # 新增记录，使用return参数返回新增id
        # sql = """
        #     INSERT INTO product_class(
        #       name, is_enable)
        #     VALUES (%s, %s)
        #     RETURNING id;
        # """
        # data = ('饼干', 1)
        # result = db_helper.write(sql, data)
        # print(result)

        # 修改不存在的记录
        # sql = """
        #     UPDATE product_class
        #        SET name=%s, is_enable=%s
        #     WHERE id=10000
        #     RETURNING id;
        # """
        # data = ('糖果', 1)
        # result = db_helper.write(sql, data)
        # print(result)

        # 查询记录
        sql = """
            SELECT * FROM product_class
        """
        result = db_helper.read(sql)
        print(result)

if __name__ == '__main__':
    unittest.main()