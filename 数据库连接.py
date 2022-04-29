dbName = "pupuDB"
conn = pymysql.connect(host="localhost",
                       user="root",
                       password="123456",
                       port=3306,
                       db=dbName,
                       charset='utf8')