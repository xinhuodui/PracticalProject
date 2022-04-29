if __name__ == '__main__':
    res = pd.DataFrame(list(res), columns=['id', 'name', 'pid', 'spec', 'price', 'market_price'])
    msg = "id\t名称\t\t\t规格\t\t\t当前价格\t市场价\n"
    for i in range(size):
        id = str(res['id'][i])
        spec = str(res['spec'][i])
        name = str(res['name'][i])
        price = str(res['price'][i])
        market_price = str(res['market_price'][i])
        msg = msg + id + "\t" + name + "\t\t\t" + spec + "\t\t\t" + price + "\t" + market_price + "\n"
    star(msg)