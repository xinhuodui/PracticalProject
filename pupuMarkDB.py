import easygui as g
import pymysql
import pandas as pd

# 连接数据库
dbName = "pupuDB"
conn = pymysql.connect(host="localhost",
                       user="root",
                       password="123456",
                       port=3306,
                       db=dbName,
                       charset='utf8')


def createDB(dbName):
    try:
        # 创建游标
        cur = conn.cursor()
        # 执行sql查询语句

        cur.execute("create database " + dbName)
        cur.execute("show databases ")
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


        # 查询
# def selectDB(dbName, tableName, selectWhere):
#     try:
#         # 创建游标
#         cur = conn.cursor()
#
#         # 执行sql查询语句
#
#         cur.execute("use " + dbName)
#         cur.execute(" select * from " + tableName + " where " + selectWhere)
#         rows = cur.fetchall()
#         for row in rows:
#             print(row)
#         return rows
#
#         # 关闭游标
#         cur.close()
#         # 关闭数据库连接
#         conn.close()
#     except pymysql.err.MySQLError as _error:
#         raise _error


def sqlDB(dbName, sqls):
    try:

        # 创建游标
        cur = conn.cursor()
        # 执行sql语句

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


# 图形化
def star(msg):
    # 图形化界面
    userChoices = g.buttonbox(msg, "朴朴超市商品信息", choices=('模糊搜索', '删除', '显示信息并退出'))
    print(userChoices)
    if userChoices.__eq__("显示信息并退出"):
        t = g.textbox(msg="详细信息查询,点击OK退出", title='朴朴超市商品信息', text=msg, codebox=True, callback=None, run=True)
        print(t)
    if userChoices.__eq__('删除'):
        res1 = sqlDB(dbName, "select * from product")
        size1 = len(res1)
        res1 = pd.DataFrame(list(res1), columns=['id', 'name', 'pid', 'spec', 'price', 'market_price'])
        list1 = ["返回"]
        for i in range(size1):
            name1 = str(res1['name'][i])
            msg1 =name1
            list1.append(msg1)
        resdelete = g.choicebox(msg="选你要删除的信息", title="朴朴超市商品信息", choices=list1)
        print(resdelete)
        if resdelete.__eq__("返回"):
            star(msg)
        else:
            sqldelete1="delete from product where name = ' "+resdelete+"'"
            sqlDB(dbName,sqldelete1)
            sqldelete2="select * from product"
            sqlDB(dbName, sqldelete2)

    if userChoices.__eq__('模糊搜索'):
        sreach=g.enterbox (msg='你要查找的产品名', title='模糊查询', default='牛奶', strip=True)

        sqlsreach = "select * from product where name LIKE \'%" + sreach + "%'"
        strachmsg = sqlDB(dbName, sqlsreach)


        size2 = len(strachmsg)
        res2 = pd.DataFrame(list(strachmsg), columns=['id', 'name', 'pid', 'spec', 'price', 'market_price'])
        msg2 = "id\t名称\t\t\t规格\t当前价格\t\t市场价\n"
        for i in range(size2):
            id = str(res2['id'][i])
            spec = str(res2['spec'][i])
            name = str(res2['name'][i])
            price = str(res2['price'][i])
            market_price = str(res2['market_price'][i])
            msg2 = msg2 + id + "\t" + name + "\t" + spec + "\t\t" + price + " \t\t\t" + market_price + "\n"
        star(msg2)




if __name__ == '__main__':
    tableName = "product"
    # sqlCreateTable="create table product(" \
    #     "id     int  PRIMARY KEY AUTO_INCREMENT," \
    #     "name   varchar(64),"\
    #     "pid    varchar(64),"\
    #     "spec   varchar(64)   , " \
    #     "price  varchar(64)   ," \
    #     "market_price   varchar(64)   " \
    #     ");"
    #
    # sqlDB(dbName,sqlCreateTable)
    #
    # selectDB(dbName, tableName, "name='蒙牛巴氏鲜牛奶180ml/袋'")
    sqlDB(dbName,"INSERT INTO product VALUES (1,'蒙牛巴氏鲜牛奶','44e7652b-a90e-4328-a89f-74471de7e218','180ml/袋','1.99','3.5');")
    sqlDB(dbName,"INSERT INTO product VALUES (2,'妃子笑荔枝','397a27fe-2a2a-43c8-bc23-adbdd3a61375','240-250g/份','17.90','19.80');")
    sqlDB(dbName,"INSERT INTO product VALUES (3,'圣农香煎牛排（黑椒味）','ef88141b-96d3-4d12-839e-433313867936','100g/袋','14.8','14.8');")
    sqlDB(dbName,"INSERT INTO product VALUES (4,'贝花子青汁牛奶','babf254e-7212-4d1d-bc32-6eeac3867b68','180g/袋','2.5','3.9');")
    sqlDB(dbName,"INSERT INTO product VALUES (5,'1Cake彩虹瑞士卷','7faf8d9d-0afd-47c7-a211-3f2b17af8371','150g/份','18.8','18.8');")
    sqlDB(dbName,"INSERT INTO product VALUES (6,'樱桃可可黑森林蛋糕','f61b1b9c-794e-4272-bcbe-7f034f27c06d','4寸','68.0','78.0');")
    sqlDB(dbName,"INSERT INTO product VALUES (7,'糕守道奶皮白蛋糕','349c0e02-2af3-4174-99ee-662db487c290','400g/箱','16.9','19.9');")
    sqlDB(dbName,"INSERT INTO product VALUES (8,'1cake抱抱卷','a7831b28-94cd-4a27-802b-fbb5047af20c','110g/盒','8.8','12.8');")
    sqlDB(dbName,"INSERT INTO product VALUES (9,'友梦虎皮蛋糕（冻）','497432a5-7a3f-422e-b95f-e44aeb236963','200g/份','6.98','12.8');")
    sqlDB(dbName,"INSERT INTO product VALUES (10,'鲜鸡蛋','6bc4d43c-33de-47a2-a199-6dc719b02380','15枚700g/盒','12.8','13.9');")
    res = sqlDB(dbName, "select * from product")
    size = len(res)
    res = pd.DataFrame(list(res), columns=['id', 'name', 'pid', 'spec', 'price', 'market_price'])
    msg = "id\t名称\t\t\t规格\t\t\t当前价格\t市场价\n"
    for i in range(size):
        id = str(res['id'][i])
        spec = str(res['spec'][i])
        name = str(res['name'][i])
        price = str(res['price'][i])
        market_price = str(res['market_price'][i])
        msg = msg + id + "\t" + name + "\t\t\t" + spec + "\t\t\t" + price + "\t" + market_price+"\n"
    star(msg)
