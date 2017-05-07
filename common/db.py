#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    Note:
        封装数据库查询语句，供爬虫调用。
        By Yanxingfei(1139),2016.08.10
"""

# requirements
import pyodbc


# 关系数据库，二维表结构，灵活性受限
class SqlServer:
    def __init__(self, host, port, user, pwd, db):  # 注意：sql中的字符串数据用单引号，不能用双引号
        self._conn = pyodbc.connect(
            "DRIVER={SQL Server Native Client 10.0};" +
            "SERVER={0},{1};DATABASE={2};UID={3};PWD={4}".format(host, port, db, user, pwd)
        )
        self._cursor = self._conn.cursor()

    def query(self, sql, is_select=True):
        self._cursor.execute(sql)
        if is_select:
            rows = self._cursor.fetchall()
            return rows
        else:
            self._conn.commit()

    def select(self, column, table, condition, order=False, order_condition="", order_asc=False, distinct=False):
        if distinct:
            if order:
                if order_asc:
                    self._cursor.execute("select distinct {0} from {1} where {2} order by {3} asc"
                                         .format(column, table, condition, order_condition))
                else:
                    self._cursor.execute("select distinct {0} from {1} where {2} order by {3} desc"
                                         .format(column, table, condition, order_condition))
            else:
                self._cursor.execute("select distinct {0} from {1} where {2}"
                                     .format(column, table, condition))
        else:
            if order:
                if order_asc:
                    self._cursor.execute("select {0} from {1} where {2} order by {3} asc"
                                         .format(column, table, condition, order_condition))
                else:
                    self._cursor.execute("select {0} from {1} where {2} order by {3} desc"
                                         .format(column, table, condition, order_condition))
            else:
                self._cursor.execute("select {0} from {1} where {2}"
                                     .format(column, table, condition))
        rows = self._cursor.fetchall()
        return rows

    def check_item(self, table, pk_id):  # 不能执行复杂语句（子查询等）。根据id检查是否存在此记录，不存在则插入
        self._cursor.execute("select * from {0} where id={1}"
                             .format(table, pk_id))
        if self._cursor.fetchall():
            pass
        else:
            print("SQL:insert into {0}(id) values({1})"
                  .format(table, pk_id))
            self._cursor.execute("insert into {0}(id) values({1})"
                                 .format(table, pk_id))

    def update(self, table, keys_and_values, condition):
        print("SQL:update {0} set {1} where {2}"
                             .format(table, keys_and_values, condition))
        self._cursor.execute("update {0} set {1} where {2}"
                             .format(table, keys_and_values, condition))

    def delete(self, table, condition):
        self._cursor.execute("delete from {0} where {1}"
                             .format(table, condition))

    def commit(self):
        print("SQL:commit")
        self._conn.commit()  # 插入、更新操作必须先提交才会生效

    def disconnect(self):
        self._conn.close()


# 虽然也是关系数据库，但扩展了对json格式的支持
class PostgreSQL:
    def __init__(self):
        pass
