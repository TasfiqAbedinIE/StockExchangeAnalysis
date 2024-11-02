from itertools import count
from operator import index

import requests
from bs4 import BeautifulSoup
import re
from datetime import datetime


def extract_date_time(input_string):
    # Define regex patterns for date and time
    date_pattern = r"[A-Za-z]{3} \d{1,2}, \d{4}"  # Pattern to match the date (e.g., "Oct 24, 2024")
    time_pattern = r"\d{1,2}:\d{2} [APM]{2}"  # Pattern to match time (e.g., "10:42 AM")

    # Extract date using regex
    date_match = re.search(date_pattern, input_string)
    if date_match:
        extracted_date = date_match.group(0)
    else:
        extracted_date = None

    # Extract time using regex
    time_match = re.search(time_pattern, input_string)
    if time_match:
        extracted_time = time_match.group(0)
    else:
        extracted_time = None

    return extracted_date, extracted_time


# url = 'https://www.nytimes.com/'

def extracting_stock_data(url):
    r = requests.get(url)
    # print(r.text)

    soup = BeautifulSoup(r.text, "lxml")
    page_title = soup.title.string      # Extracting Title
    date_time_string = soup.find(class_="BodyHead topBodyHead").string      #Extracting latest date and time

    extracted_date, extracted_time = extract_date_time(date_time_string)
    # print(extracted_date, extracted_time)

    date_format = "%b %d, %Y"  # Month (abbreviated) Day, Year
    time_format = "%I:%M %p"   # Hour:Minute AM/PM

    date_obj = datetime.strptime(extracted_date, date_format).date()
    time_obj = datetime.strptime(extracted_time, time_format).time()


    # print(date_obj, time_obj)
    # Extracting columns Headers
    table_head_comp = soup.find("thead")
    table_head = table_head_comp.find_all("th")
    table_titles = []
    table_titles.extend(i.text for i in table_head)
    print(table_titles)

    table_section = soup.find("div", class_="table-responsive inner-scroll")
    # print(table_section)

    table_data = table_section.find("table", class_="table table-bordered background-white shares-table fixedHeader")
    # print(table_data)

    table_rows = table_data.find_all("tr")
    # print(len(table_rows))

    # Stock data Dictionary for dataframe
    stock_data_table = {}
    for key in table_titles:
        stock_data_table[key] = []


    # Stock data is extracted ------------>
    for item in table_rows[1:]:
        # print("A Item below")
        each_row_data = []
        for element in item:
            if element.text.strip() != "":
                each_row_data.append(element.text.strip())
                for key, value in zip(table_titles, each_row_data):
                    if len(table_titles) == len(each_row_data):
                        # Convert the data into suitable type using regular expression >>>>>>>>
                        try:
                            if value == "--":
                                value = 0
                            value = float(value.replace(",", ""))
                            stock_data_table[key].append(value)
                        except:
                            value = str(value)
                            stock_data_table[key].append(value)

    return stock_data_table, page_title, date_obj, time_obj
