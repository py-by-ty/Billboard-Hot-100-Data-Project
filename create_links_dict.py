'''
Description: This file reads an Excel file and assign links as dict
                values for date keys.
'''

import pandas as pd
import datetime


###########################
### DEF NEW FUNCTION: 1 ###
### Read Excel file and assign links from dataframe to variable names

# input_file is "webpages.xlsx"

def create_links_dict(file_x, sheetname):

    webpages_dataframe = pd.read_excel(file_x, sheet_name = sheetname)

    dates_list = []

    url_base = 'http://www.billboard.com/charts/hot-100/'

    url_list = []

    # link_vars = {}

    # Assigning link to dynamic variable names:
    for i in range(0, len(webpages_dataframe["Dates"])):
        
        # Grabbing each date string from "Dates" column in dataframe, to append
        # to base url:
        date_str = datetime.datetime.strftime(webpages_dataframe["Dates"][i],
                                                '%Y-%m-%d')

        dates_list.append(date_str)

        
        # Formatting url_var as a base url plus a date string:
        url_var = f"{url_base}{date_str}/"
        url_list.append(url_var)


    # Build a dictionary to link date keys from input file to webpage links
    # containing dates:
    webpages_dict = {date_key: link_value for date_key, link_value in
                     zip(dates_list, url_list)}
        
    return webpages_dict

