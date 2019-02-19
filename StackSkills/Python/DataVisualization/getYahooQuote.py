import urllib.request
import urllib.parse
import pandas as pd
import numpy as np
import matplotlib.dates as mdates
import matplotlib.pyplot as plt

# Build the cookie handler
cookier = urllib.request.HTTPCookieProcessor()
opener = urllib.request.build_opener(cookier)
urllib.request.install_opener(opener)

# Cookie and corresponding crumb
_cookie = None
_crumb = None

# Headers to fake a user agent
_headers = {
    'User-Agent': 'Mozilla/5.0 (X11; U; Linux i686) Gecko/20071127 Firefox/2.0.0.11'
}


# def bytespdate2num(fmt, encoding='utf-8'):
#     str_converter = mdates.strpdate2num(fmt)
#
#     def bytesconverter(b):
#         s = b.decode(encoding)
#
#         return str_converter(s)
#
#     return bytesconverter


def _get_cookie_crumb():
    """
    This function perform a query and extract the matching cookie and crumb.
    """

    # Perform a Yahoo financial lookup on SP500
    req = urllib.request.Request('https://finance.yahoo.com/quote/^GSPC', headers=_headers)
    f = urllib.request.urlopen(req)
    alines = f.read().decode('utf-8')

    # Extract the crumb from the response
    global _crumb
    cs = alines.find('CrumbStore')
    cr = alines.find('crumb', cs + 10)
    cl = alines.find(':', cr + 5)
    q1 = alines.find('"', cl + 1)
    q2 = alines.find('"', q1 + 1)
    crumb = alines[q1 + 1:q2]
    _crumb = crumb

    # Extract the cookie from cookiejar
    global cookier, _cookie

    for c in cookier.cookiejar:
        if c.domain != '.yahoo.com':
            continue
        if c.name != 'B':
            continue
        _cookie = c.value


# Print the cookie and crumb
print('Cookie:', _cookie)
print('Crumb:', _crumb)


def load_yahoo_quote(ticker, begindate, enddate, info='quote', format_output='list'):
    """
    This function load the corresponding history from Yahoo.
    """

    print('Currently pulling: ', ticker)

    # Check to make sure that the cookie and crumb has been loaded
    global _cookie, _crumb

    if _cookie is None or _crumb is None:
        _get_cookie_crumb()

    param = dict()
    param['interval'] = '1d'

    if info == 'quote':
        param['events'] = 'history'
    param['crumb'] = _crumb
    params = urllib.parse.urlencode(param)
    url = f'https://query1.finance.yahoo.com/v7/finance/download/{ticker}?{params}'

    print(url)

    req = urllib.request.Request(url, headers=_headers)

    # Perform the query
    # There is no need to enter the cookie here, as it is automatically handled by opener
    f = urllib.request.urlopen(req)
    alines = f.read().decode('utf-8')
    # print(alines)
    if format_output == 'list':
        return alines.split('\n')

    if format_output == 'dataframe':
        nested_alines = [line.split(',') for line in alines.split('\n')[1:]]
        cols = alines.split('\n')[0].split(',')
        adf = pd.DataFrame.from_records(nested_alines[:-1], columns=cols)

        return adf

    stock_data = ''
    split_source = f.split('\n')

    for each_line in split_source:
        split_line = each_line.split(',')

        if len(split_line) == 7:
            if 'values' not in each_line:
                stock_data.join(each_line)

    # # Format data using % signs
    # date, closep, highp, lowp, openp, adjp, volume = np.loadtxt(stock_data, delimiter=',',
    #                                                             unpack=True,
    #                                                             converters={0: mdates.bytespdate2num('%Y%m%d')})

    plt.plot_date(enddate, begindate, '-')
    plt.show()


def load_quote(ticker):
    stock = input(ticker)
    print('===', stock, '===')
    print(load_yahoo_quote(stock, '20100618', '20190218'))


load_quote('')
# plt.plot(load_quote(''))
# plt.show()
