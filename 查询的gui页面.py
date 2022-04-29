def star(msg):
    if userChoices.__eq__('模糊搜索'):
        sreach = g.enterbox(msg='你要查找的产品名', title='模糊查询', default='牛奶', strip=True)

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