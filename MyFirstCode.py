#!/usr/bin/env python3
#-*- coding: utf-8 -*-

# 新股涨停板计算 2017.11.


def stockincome(openingprice, newprice, amount):    # 开盘价，现价，股数
    increase = (newprice / openingprice) - 1        # 累积涨幅
    accumulate = (newprice - openingprice) * amount # 累积收益
    return increase, accumulate


def stockprice(price, i):
    if i <= 1:
        exp = 0.44                                  # 第一天涨 44%
    else:
        exp = 0.1                                   # 以后涨停 10%
    temp1 = price * (1 + exp)                       # 计算涨停股价
    temp2 = round(float(temp1), 2)                  # 涨停股价取整
    exp = round(float((temp2 / price) - 1.0), 4)    # 重新计算涨幅，小数点后4位
    price = temp2                                   # 重新计算涨幅后的新股价
    return price, exp


openingprice0 = float(input('请输入中签价格 : '))
amount0 = int(input('请输入中签股数 : '))
countday0 = int(input('请输入计算天数 : '))

price0 = openingprice0
i = 0
for i in range(countday0):
    price0, exp0 = stockprice(price0, i + 1)
    stockincome0, accumulate0 = stockincome(openingprice0, price0, amount0)
    print ("第%2d天 涨幅:%5.2f%% 股价:%5.2f 累积涨幅:%6.2f%% 累积收益 %8.2f" % (
        i + 1, round(exp0 * 100, 2), price0, round(stockincome0 * 100, 2), accumulate0))