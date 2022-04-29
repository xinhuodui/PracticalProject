def sqlDB(dbName, sqls):
    try:

        # 创建游标
        cur = conn.cursor()
        # 执行sql查询语句

        cur.execute("use " + dbName)
        cur.execute(sqls)
        rows = cur.fetchall()
        for row in rows:
            print(row)
        return rows
        conn.commit()
        # 关闭游标
        cur.close()
        # 关闭数据库连接
        conn.close()
    except pymysql.err.MySQLError as _error:
        raise _error