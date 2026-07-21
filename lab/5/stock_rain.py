"""
CSCI 51P Lab 5: Rain vs. Stock

Author: arshtyi
Date: July 21, 2026

This program reads rainfall and stock-price data from CSV files, matches
records by date, and plots rainfall against daily stock-price changes.
"""

import matplotlib.pyplot as plt


def parse_rainfall(fname):
    """Read daily precipitation amounts from a rainfall data file.

    :param fname: str, the name of a CSV file containing rainfall data
    :return: dict mapping date strings in YYYY-MM-DD format to rainfall
             totals as floats; dates with missing precipitation are omitted
    """
    rainfall_by_date = {}

    with open(fname, "r") as rainfall_file:
        # The first line contains column names rather than a data record.
        next(rainfall_file)

        for line in rainfall_file:
            if line.strip() == "":
                continue

            columns = line.strip().split(",")
            date = columns[0].strip().strip('"')
            precipitation = columns[1].strip().strip('"')

            # A quoted NA indicates that no precipitation value is known.
            if precipitation != "NA":
                rainfall_by_date[date] = float(precipitation)

    return rainfall_by_date


def format_stock_date(date):
    """Convert a stock date from M/D/YY format to YYYY-MM-DD format.

    :param date: str, a slash-separated date from a stock CSV file
    :return: str containing the same date in YYYY-MM-DD format
    """
    month, day, year = date.split("/")

    if len(year) == 2:
        year = "20" + year

    return year.zfill(4) + "-" + month.zfill(2) + "-" + day.zfill(2)


def parse_stock(fname, sym):
    """Read daily price changes for one stock symbol from a CSV file.

    :param fname: str, the name of a CSV file containing stock data
    :param sym: str, the stock symbol whose records should be selected
    :return: dict mapping dates in YYYY-MM-DD format to closing price minus
             opening price as floats; rows missing either price are omitted
    """
    price_change_by_date = {}

    with open(fname, "r") as stock_file:
        # The first line contains column names rather than a data record.
        next(stock_file)

        for line in stock_file:
            if line.strip() == "":
                continue

            columns = line.strip().split(",")
            date = columns[0].strip()
            opening_price = columns[1].strip()
            closing_price = columns[4].strip()
            stock_symbol = columns[6].strip()

            if (stock_symbol == sym and opening_price != ""
                    and closing_price != ""):
                daily_change = float(closing_price) - float(opening_price)
                normalized_date = format_stock_date(date)
                price_change_by_date[normalized_date] = round(daily_change, 2)

    return price_change_by_date


def correlate_data(stock_dict, rain_dict):
    """Pair stock-price changes with rainfall totals from matching dates.

    :param stock_dict: dict mapping dates to daily stock-price changes
    :param rain_dict: dict mapping dates to daily rainfall totals
    :return: list of [stock price change, rainfall] lists for dates present
             in both input dictionaries
    """
    correlated_values = []

    # Iterating over the stock data preserves its original chronological order.
    for date in stock_dict:
        if date in rain_dict:
            correlated_values.append([stock_dict[date], rain_dict[date]])

    return correlated_values


def scatter_plot(data, format, name, done):
    """Add one stock's rainfall/price-change data to a scatter plot.

    :param data: list of [stock price change, rainfall] pairs
    :param format: str, a matplotlib format string for the plotted points
    :param name: str, the stock symbol used as the legend label
    :param done: bool, True exactly when this is the final data set to plot
    :return: None; the completed plot is displayed only when done is True
    """
    stock_changes = []
    rainfall_totals = []

    for stock_change, rainfall in data:
        stock_changes.append(stock_change)
        rainfall_totals.append(rainfall)

    # Rainfall is the hypothesized cause, so it belongs on the x-axis.
    plt.plot(rainfall_totals, stock_changes, format, label=name)
    plt.title("Rainfall vs Price Change")
    plt.xlabel("Rainfall")
    plt.ylabel("Price Change")

    if done:
        plt.legend()
        plt.show()


def main():
    """Collect file/symbol choices and plot exactly two stocks.

    The first symbol should be MSFT or AMZN, a Seattle-area company. The
    second should be a technology company headquartered elsewhere.

    :return: None; displays a combined rainfall-versus-price-change plot
    """
    rainfall_filename = input("Enter the name of a rainfall data file:\n")
    stock_filename = input("Enter the name of a stock data file:\n")
    first_symbol = input(
        "Enter a first stock symbol (e.g. MSFT or AMZN):\n"
    )
    second_symbol = input(
        "Enter a second stock symbol (not head-quartered in Seattle):\n"
    )

    rainfall_data = parse_rainfall(rainfall_filename)

    first_stock_data = parse_stock(stock_filename, first_symbol)
    first_correlated_data = correlate_data(first_stock_data, rainfall_data)
    scatter_plot(first_correlated_data, "b.", first_symbol, False)

    second_stock_data = parse_stock(stock_filename, second_symbol)
    second_correlated_data = correlate_data(second_stock_data, rainfall_data)
    scatter_plot(second_correlated_data, "r+", second_symbol, True)


if __name__ == "__main__":
    main()
