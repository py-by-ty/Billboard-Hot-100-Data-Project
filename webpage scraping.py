'''
Name: Tyler Pinaud
Date: 7/8/2024
Description: This file calls user-defined functions to request access
                to multiple webpage links, create BeautifulSoup objects
                from those webpages, parse the text from the soups,and
                write data from the webpages to an Excel file.

'''


###########################
### STEP 5: SCRIPT: FN'S 1 - 4 ###
# Iterate through function calling
########################

import pandas as pd
import xlsxwriter

# Import written functions:
from create_links_dict import create_links_dict
from make_soups import make_soups
from soup_parsing import soup_parsing
from hot_100_data_writer import hot_100_data_writer


# def webpage_iteration(file_x):

webpages_dict_output = create_links_dict("webpages.xlsx",
                                         "webpage_dates_Quarterly-200")


output_filename = "Hot-100_data.xlsx"
output_sheetname = "aggregate_data_Quarterly-200"

aggregate_df = pd.DataFrame()


# Defining a counter variable "i" to count number of iterations from
# the list of links:
i = 0
print(webpages_dict_output)

# For loop to call functions for each date/link from input Excel file:
for key in webpages_dict_output.keys():

    # Setting the date keys from webpages_dict_output as tab names for
    # the output Excel file:
    date_str = key

    # Call make_soups to create Beautiful Soup objects from the values
    # associated with webpage_dict_output keys:
    individual_s_soup, individual_c_soup = make_soups(webpages_dict_output[key])

    # Parse the soups to get full chart data for each link:
    rankings, songs, artists, weeks, features, labels = soup_parsing(
        individual_s_soup, individual_c_soup)


    # Create a writer object (returned from hot_100_data_writer) to write,
    # then close the new file:
    df_output = hot_100_data_writer(date_str, rankings, songs, artists, weeks,
                                    features, labels)

    # Append (concatenate) the last df_output to an aggregate dataframe, for each
    # date key, before writing to Excel:
    aggregate_df = pd.concat([aggregate_df, df_output])
    
    # last_row = len(pd.read_excel(aggregate_df))

    i = i + 1
    print(f"# completed iterations: {i}")


print(aggregate_df)


writer = pd.ExcelWriter(output_filename, engine = "xlsxwriter", mode="w")

aggregate_df.to_excel(writer, sheet_name = output_sheetname,
                      index=False, header=True)


########################
########################

writer.close()