"""
    CS051P Lab Assignments: Stock v.s. Rain

    Author: Your-Name-Here

    Date:   WHEN YOU COMPLETED IT

    The goal of this assignment is to familiarize you with data analysis
    and visualization. You'll practice handling files in csv format,
    create and manipulate Python dictionaries, and do some basic plotting
    using the matplotlib package.
"""
import matplotlib.pyplot as plt


def parse_rainfall(fname):
    """
    Parse the rainfall dataset and generate a dictionary data in the
    format of a pair of {date: rainfall}

    :param (file) fname: the rainfall dataset
    :return (dict) res: the resulting dictionary in the format of a
            pair of {date: rainfall}
    """
    res = {}

    try:
        with open(fname, 'r') as file_in:
            for index, line in enumerate(file_in):
                # skip the first row that lists the title of each column
                if index > 0:
                    cubic = line.split(',')
                    if len(cubic) == 5:
                        # call the replace function to remove quote
                        date = cubic[0].replace('"', '')
                        # handle the "NA" data
                        if cubic[1] != '"NA"':
                            prcp = float(cubic[1])
                            res[date] = prcp
    except IOError:
        print('Rainfall file ' + fname + ' cannot be opened \n')

    return res


def process_date(date):
    """
    Standardize the date format to be yyyy-mm-dd

    :param (str) date: the input date that is not in the standard format
    :return (str) res: the output date that follows in the standard format
    """
    d = date.split('/')
    year = '20' + d[2]
    month = '0' + d[0] if int(d[0]) < 10 else d[0]
    day = '0' + d[1] if int(d[1]) < 10 else d[1]
    res = year + '-' + month + '-' + day

    return res


def parse_stock(fname, sym):
    """
    Parse the stock dataset and generate a dictionary data in the format of
    {date: change_in_price} for a given stock with symbol 'sym'
    :param fname:
    :param sym:
    :return:
    """
    res = {}

    try:
        with open(fname, 'r') as file_in:
            for index, line in enumerate(file_in):
                if index > 0 and line != '\n':
                    cubic = line.split(',')
                    if cubic[6].rstrip() == sym:
                        # use the standard date format
                        date = process_date(cubic[0])
                        # handle cases that stock open price is missing
                        if cubic[1] != "" and cubic[4] != "":
                            change_in_price = round(float(cubic[4])
                                                    - float(cubic[1]), 2)
                            res[date] = change_in_price
    except IOError:
        print('Stock file ' + fname + ' cannot be opened \n')

    return res


def correlate_data(stock_dict, rain_dict):
    """
    Find the correlation between stock price change and rainfall

    :param (dict) stock_dict: the stock dictionary data
    :param (dict) rain_dict: the rainfall dictionary data
    :return (list) res: the resulting 2d-list of data in the
            format of [stock_price_change: rainfall] for dates
    """
    res = []

    for stock_date, stock_price_change in stock_dict.items():
        for rain_date, rain_amount in rain_dict.items():
            if stock_date == rain_date:
                res.append([stock_price_change, rain_amount])

    return res


def scatter_plot(data, format, name, done):
    """
    Plot the correlation using matplotlib package

    :param (2d-list) data: the correlation between stock price change
            and the rainfall
    :param (str) format: the format for the plot
    :param (str) name: name of the stock
    :param (boolean) done: False to wait for plot; True to plot
    :return: None
    """
    x = []
    y = []
    for line in data:
        x.append(line[1])
        y.append(line[0])
    plt.plot(x, y, format, label=name)

    if done:
        plt.ylabel('Stock change in price')
        plt.xlabel('Rainfall PRCP')
        plt.legend()
        plt.show()


def main():
    # rain_dict = parse_rainfall('rainTest4.csv')
    # print(rain_dict)
    # stock_dict = parse_stock('stocksTest4.csv', 'GOOGL')
    # print(stock_dict)
    # data = correlate_data(stock_dict, rain_dict)
    # print(data)
    # scatter_plot(data, 'or', 'IBM', True)
    # print(parse_rainfall('rainTest9.csv'))
    # print(parse_stock('stockTest4.csv', 'GOOGL'))
    # print(parse_rainfall('rainTest5.csv'))
    rain_dict = parse_rainfall('csvs/rainSeattle-2012-2017.csv')
    company = ['GOOGL', 'MSFT', 'AMZN', 'AAPL', 'IBM']
    format = ['or', '+b', '*k', 'xg', '^m']
    
    for index, sym in enumerate(company):
        stock_dict = parse_stock('csvs/stocks-2006-2017.csv', sym)
        data = correlate_data(stock_dict, rain_dict)
        if index != len(company) - 1:
            scatter_plot(data, format[index], sym, False)
        else:
            scatter_plot(data, format[index], sym, True)


if __name__ == '__main__':
    main()
