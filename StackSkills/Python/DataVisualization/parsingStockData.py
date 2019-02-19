import matplotlib.pyplot as plt
from alpha_vantage.timeseries import TimeSeries
import matplotlib.dates as mdates
import urllib.request
import urllib.parse
import numpy as np

# # Build the cookie handler
# cookier = urllib.request.HTTPCookieProcessor()
# opener = urllib.request.build_opener(cookier)
# urllib.request.install_opener(opener)
#
# # Cookie and corresponding crumb
# _cookie = None
# _crumb = None
#
# # Headers to fake a user agent
# _headers = {
#     'User-Agent': 'Mozilla/5.0 (X11; U; Linux i686) Gecko/20071127 Firefox/2.0.0.11'
# }


def bytespdate2num(fmt, encoding='utf-8'):
    str_converter = mdates.strpdate2num(fmt)

    def bytesconverter(b):
        s = b.decode(encoding)

        return str_converter(s)

    return bytesconverter


# def graph_data(stock):
#     ts = TimeSeries(key='JGQU9ILE9JTG8CAG', output_format='pandas')
#     data, meta_data = ts.get_weekly_adjusted(symbol=stock)
#     # data['close'].plot()
#     plt.title('Weekly Times Series for the TSLA stock (1 Week)')
#     plt.show()


def graph_data(stock):
    """
    This function load the corresponding history/divident/split from Yahoo.
    """
    # Check to make sure that the cookie and crumb has been loaded
    global _cookie, _crumb

    print('Currently pulling: ', stock)

    url = 'https://query1.finance.yahoo.com/v7/finance/download/{}?{}' + stock
    source_code = urllib.request.urlopen(url).read().decode()
    stock_data = ''
    split_source = source_code.split('\n')

    # Format data using % signs
    date, closep, highp, lowp, openp, adjp, volume = np.loadtxt(stock_data, delimiter=',',
                                                                unpack=True,
                                                                converters={0: bytespdate2num('%Y%m%d')})

    for each_line in split_source:
        split_line = each_line.split(',')

        if len(split_line) == 7:
            if 'values' not in each_line:
                stock_data.join(each_line)

    print(date)


stock = input('Stock to plot: ')
graph_data(stock)
