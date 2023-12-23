import pandas as pd

# reads the csv file of the SPX historical data
all_data = pd.read_csv('SPXHistoricalData2013-2023.csv')

# only the date and closing price
date_close = all_data[["Date", "Close/Last"]]

# creates a dataframe of all third fridays
third_fridays = pd.DataFrame(pd.date_range('2013-12-23', '2023-12-22', freq='WOM-3FRI'))

# corrects format
third_fridays_converted = third_fridays[0].dt.strftime('%m/%d/%Y')

# corrects format of date_close
date_close['Date'] = pd.to_datetime(date_close['Date']).dt.strftime('%m/%d/%Y')

third_friday_prices = {}

# finds closing price for third fridays
for i in third_fridays_converted:
    third_friday_prices[i] = date_close.loc[date_close.Date == i, "Close/Last"].values[0]

# calculates percent change, sorts it based on value
percent_changes_greater_than = {}
percent_changes_less_than = {}
list_of_dates = list(third_friday_prices.keys())
for i in range(0, len(list_of_dates) - 1):
    percent_change = ((third_friday_prices[list_of_dates[i + 1]] - third_friday_prices[list_of_dates[i]]) /
                      third_friday_prices[list_of_dates[i]]) * 100
    if abs(percent_change) >= 5:
        percent_changes_greater_than[list_of_dates[i] + " to " + list_of_dates[i + 1]] = percent_change
    else:
        percent_changes_less_than[list_of_dates[i] + " to " + list_of_dates[i + 1]] = percent_change

print(len(percent_changes_greater_than))
