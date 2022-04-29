if __name__ == '__main__':
tableName = "product"
    sqlCreateTable="create table product(" \
        "id     int  PRIMARY KEY AUTO_INCREMENT," \
        "name   varchar(64),"\
        "pid    varchar(64),"\
        "spec   varchar(64)   , " \
        "price  varchar(64)   ," \
        "market_price   varchar(64)   " \
        ");"

    sqlDB(dbName,sqlCreateTable)