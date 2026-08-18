import pandas as pd


# Wikipedia maintains a table containing the current
# constituents of the S&P 500 index.
SP500_URL = "https://en.wikipedia.org/wiki/List_of_S%26P_500_companies"


def get_sp500_tickers():
    """
    Download the current S&P 500 constituent list.

    Returns
    -------
    list[str]
        Yahoo Finance compatible ticker symbols.
    """

    # pandas.read_html() searches the webpage for HTML tables.
    tables = pd.read_html(SP500_URL)

    # The first table on the page contains the S&P 500 companies.
    sp500_table = tables[0]

    # We only need the ticker-symbol column.
    tickers = sp500_table["Symbol"].tolist()

    # Yahoo Finance represents tickers containing "." using "-".
    #
    # Example:
    # BRK.B -> BRK-B
    #
    # Therefore we convert them before passing the symbols
    # to yfinance.
    tickers = [ticker.replace(".", "-") for ticker in tickers]

    return tickers


if __name__ == "__main__":

    tickers = get_sp500_tickers()

    print("Number of S&P 500 stocks:", len(tickers))

    print("\nFirst 10 tickers:")

    print(tickers[:10])