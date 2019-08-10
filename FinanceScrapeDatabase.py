# Import libraries
from lxml.html import fromstring
from datetime import datetime
import schedule
import requests
import sqlite3
import time
import sys

def flatten_list(multi_list):
    flatten_list = list()
    for single in multi_list:
        if len(single) == 1:
            for i in single:
                flatten_list.append(i)
        elif len(single) > 1:
            full_string = ''
            for i in range(0, len(single)):
                cur_string = single[i]
                full_string = full_string + str(cur_string)
            flatten_list.append(full_string)
    return flatten_list

def pull_text(table):
    text_list = list()
    value_list = list()
    for item in table:
        text_list.append(item.xpath('.//td[@class="C(black) W(51%)"]//text()'))
        value_list.append(item.xpath('.//td[@class="Ta(end) Fw(600) Lh(14px)"]//text()'))
    return text_list, value_list

def check_len(list1, list2):
    if len(list1) > len(list2) or len(list2) > len(list1):
        raise ValueError('Keys do NOT match values')

# Prompt user for total number of stocks for scraping
while True:
    try:
        total_stocks = int(input('Enter total number of stocks: '))
    except ValueError:
        print('Enter a positive whole number')
    if total_stocks <= 0:
        print('Enter a positive whole number')
        continue
    else:
        break

# Prompt user for stock symbols
stock_list = list()
for prompt in range(0, total_stocks):
    sel_stock = input('Enter stock symbol: ')
    stock_list.append(sel_stock)
stock_set_list = set(stock_list)
unique_stock_list = (list(stock_set_list))

def job():
    for current_stock in unique_stock_list:
        # Create Yahoo Finance URL
        url = 'https://finance.yahoo.com/quote/' + current_stock + '/'

        try:
            # Request data
            response = requests.get(url)

            # Determine if response is appropriate
            response.raise_for_status()
        except requests.exceptions.HTTPError as error:
            print('Invalid response: {}'.format(error.response.status_code))
            sys.exit(1)

        cur_datetime = datetime.now().strftime('%d/%m/%Y')

        tree = fromstring(response.text)
        left_table = tree.xpath('//*[@id="quote-summary"]/div[1]/table/tbody/tr')
        right_table = tree.xpath('//*[@id="quote-summary"]/div[2]/table/tbody/tr')

        # Create single dictionary of table values
        left_text, left_value = pull_text(left_table)
        right_text, right_value = pull_text(right_table)
        check_len(left_text, right_text)
        check_len(flatten_list(left_value), flatten_list(right_value))
        all_values = left_value + right_value + [cur_datetime]
        all_text = left_text + right_text + [['Date']]
        for table_row in range(len(all_text)):
            cur_val = all_text.pop(table_row)
            all_text.insert(table_row, str(cur_val).replace("'", "").replace('"', '') + ' TEXT')

        # Create and populate database
        conn = sqlite3.connect('Stocks.db')
        c = conn.cursor()

        # Create Table
        c.execute('CREATE TABLE IF NOT EXISTS ' + current_stock + ' (' + str(all_text)[1: -1].replace("'", "") + ')')
        conn.commit()

        # Insert Data
        c.execute('INSERT INTO ' + current_stock + ' VALUES (' + str(flatten_list(all_values))[1: -1] + ')')
        conn.commit()

        conn.close()
        time.sleep(5)

# Task scheduling
schedule.every().day.at("16:00").do(job)

while True:
    schedule.run_pending()
    time.sleep(1)