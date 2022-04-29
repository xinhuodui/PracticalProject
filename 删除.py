def star(msg):
    if userChoices.__eq__('删除'):
        res1 = sqlDB(dbName, "select * from product")
        size1 = len(res1)
        res1 = pd.DataFrame(list(res1), columns=['id', 'name', 'pid', 'spec', 'price', 'market_price', 'share_content'])
        list1 = ["返回"]
        for i in range(size1):
            name1 = str(res1['name'][i])
            msg1 = name1
            list1.append(msg1)
        resdelete = g.choicebox(msg="选你要删除的信息", title="朴朴超市商品信息", choices=list1)
        print(resdelete)
        if resdelete.__eq__("返回"):
            star(msg)
        else:
            sqlDB("delete from product where name = " + resdelete)