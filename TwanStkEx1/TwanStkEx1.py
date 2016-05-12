# -*- coding: utf-8 -*-

from sys import exit
from sys import argv
from pandas.io.data import DataReader
import matplotlib.pyplot as plt
import datetime as dtime

def main():
    '''
    1. The data from Yahoo! Finance is not grabbed by calling url apis, is by using Pandas APIs.
    2. This program is to get TWSE data only, if wants OTC data, need to modify code.
    '''
    #Setup figure
    stock_fig = plt.figure()
    stock_plt = plt.subplot2grid((1, 1), (0, 0), colspan=1)
    stock_title= "{} day price".format(stock_num)
    plt.suptitle(stock_title)
    startday = dtime.date(2000, 1, 1)
    
    # Add ".TW" to tell yahoo!Finance to query TWSE stock data.
    # If want to query OTC, please add ".TWO"
    stock_str = "{}.TW".format(stock_num)
    #print stock_str
    
    #about how the DataReader() works, please refer to data.py from pandas
    try:
        stock_data = DataReader(stock_str, 'yahoo', startday)
        #Clear the current axes
        stock_plt.cla()
        #Turn the axes grids on 
        stock_plt.grid(True)
        #plot date and price
        stock_plt.plot(stock_data.index, stock_data['Close'])
        #show
        plt.show()
    except:
        exit("Error happened!!\nTry: python TwanStkEx1.py 2330")

if __name__ == '__main__':
    try:
        py_script, stock_num = argv
    except:
        exit("You need to give the stock number.\nFor example:\n#python TwanStkEx1.py 2330")
    
    #main loop
    main()