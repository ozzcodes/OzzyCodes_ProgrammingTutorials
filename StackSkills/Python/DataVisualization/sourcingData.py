from urllib.request import Request, urlopen
from urllib.parse import urlencode
import ystockquote


def _request(stock, stat):
    url = 'http://finance.yahoo.com/d/quotes.csv?s=%s&f=%s' % (stock, stat)
    req = Request(url)
    resp = urlopen(req)
    content = resp.read().decode().strip()

    return content


def get_all(stock):
    """
    Get all available quote data for the given ticker symbol.
    Returns a dictionary.
    """
    ids = \
        'ydb2r1b3qpoc1d1cd2c6t1k2p2c8m5c3m6gm7hm8k1m3lm4l1t8w1g1w4g3p' \
        '1g4mg5m2g6kvjj1j5j3k4f6j6nk5n4ws1xj2va5b6k3t7a2t615l2el3e7v1' \
        'e8v7e9s6b4j4p5p6rr2r5r6r7s7'
    values = _request(stock, ids).split(',')
    return dict(
        dividend_yield=values[0],
        dividend_per_share=values[1],
        ask_realtime=values[2],
        dividend_pay_date=values[3],
        bid_realtime=values[4],
        ex_dividend_date=values[5],
        previous_close=values[6],
        today_open=values[7],
        change=values[8],
        last_trade_date=values[9],
        change_percent_change=values[10],
        trade_date=values[11],
        change_realtime=values[12],
        last_trade_time=values[13],
        change_percent_realtime=values[14],
        change_percent=values[15],
        after_hours_change_realtime=values[16],
        change_200_sma=values[17],
        todays_low=values[18],
        change_50_sma=values[19],
        todays_high=values[20],
        percent_change_50_sma=values[21],
        last_trade_realtime_time=values[22],
        fifty_sma=values[23],
        last_trade_time_plus=values[24],
        twohundred_sma=values[25],
        last_trade_price=values[26],
        one_year_target=values[27],
        todays_value_change=values[28],
        holdings_gain_percent=values[29],
        todays_value_change_realtime=values[30],
        annualized_gain=values[31],
        price_paid=values[32],
        holdings_gain=values[33],
        todays_range=values[34],
        holdings_gain_percent_realtime=values[35],
        todays_range_realtime=values[36],
        holdings_gain_realtime=values[37],
        fiftytwo_week_high=values[38],
        more_info=values[39],
        fiftytwo_week_low=values[40],
        market_cap=values[41],
        change_from_52_week_low=values[42],
        market_cap_realtime=values[43],
        change_from_52_week_high=values[44],
        float_shares=values[45],
        percent_change_from_52_week_low=values[46],
        company_name=values[47],
        percent_change_from_52_week_high=values[48],
        notes=values[49],
        fiftytwo_week_range=values[50],
        shares_owned=values[51],
        stock_exchange=values[52],
        shares_outstanding=values[53],
        volume=values[54],
        ask_size=values[55],
        bid_size=values[56],
        last_trade_size=values[57],
        ticker_trend=values[58],
        average_daily_volume=values[59],
        trade_links=values[60],
        order_book_realtime=values[61],
        high_limit=values[62],
        eps=values[63],
        low_limit=values[64],
        eps_estimate_current_year=values[65],
        holdings_value=values[66],
        eps_estimate_next_year=values[67],
        holdings_value_realtime=values[68],
        eps_estimate_next_quarter=values[69],
        revenue=values[70],
        book_value=values[71],
        ebitda=values[72],
        price_sales=values[73],
        price_book=values[74],
        pe=values[75],
        pe_realtime=values[76],
        peg=values[77],
        price_eps_estimate_current_year=values[78],
        price_eps_estimate_next_year=values[79],
        short_ratio=values[80],
    )


# Grab stock data from Yahoo's API
def graph_data(stock, start_date, end_date):
    """
    Get historical prices for the given ticker symbol.
    Date format is 'YYYY-MM-DD'

    Returns a nested dictionary (dict of dicts).
    outer dict keys are dates ('YYYY-MM-DD')
    """
    params = urlencode({
        's': stock,
        'a': int(start_date[5:7]) - 1,
        'b': int(start_date[8:10]),
        'c': int(start_date[0:4]),
        'd': int(end_date[5:7]) - 1,
        'e': int(end_date[8:10]),
        'f': int(end_date[0:4]),
        'g': 'd',
        'ignore': '.csv',
    })
    url = 'http://real-chart.finance.yahoo.com/table.csv?%s' % params
    req = Request(url)
    resp = urlopen(req)
    content = str(resp.read().decode('utf-8').strip())
    daily_data = content.splitlines()
    hist_dict = dict()
    keys = daily_data[0].split(',')

    for day in daily_data[1:]:
        day_data = day.split(',')
        date = day_data[0]
        hist_dict[date] = \
            {keys[1]: day_data[1],
             keys[2]: day_data[2],
             keys[3]: day_data[3],
             keys[4]: day_data[4],
             keys[5]: day_data[5],
             keys[6]: day_data[6]}

    return hist_dict


stock = input('Stock to plot: ')
graph_data(stock, '2010-06-16', '2019-02-16')
