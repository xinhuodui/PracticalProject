def selectDB(dbName, tableName, selectWhere):
    try:
        # 创建游标
        cur = conn.cursor()

        # 执行sql查询语句

        cur.execute("use " + dbName)
        cur.execute(" select * from " + tableName + " where " + selectWhere)
        rows = cur.fetchall()
        for row in rows:
            print(row)
        return rows

        # 关闭游标
        cur.close()
        # 关闭数据库连接
        conn.close()
    except pymysql.err.MySQLError as _error:
        raise _error