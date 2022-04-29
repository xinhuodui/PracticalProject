def star(msg):
    # 图形化界面
    userChoices = g.buttonbox(msg, "朴朴超市商品信息", choices=('模糊搜索', '删除', '显示信息并退出'))
    print(userChoices)

    if userChoices.__eq__("显示信息并退出"):
        t = g.textbox(msg="详细信息查询,点击OK退出", title='朴朴超市商品信息', text=msg, codebox=True, callback=None, run=True)
        print(t)
        if t is None:
            star(msg)
