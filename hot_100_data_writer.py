'''
Description: This file stores input song data into a dataframe, to be
                written to Excel.
'''


###########################
### DEF NEW FUNCTION: 4 ###
# Write dataframe structures
########################

import pandas as pd
# import openpyxl
# from openpyxl import Workbook


# Creating a writer object to send data to excel file "Hot-100_data.xlsx"
def hot_100_data_writer(date_str, rankings, songs, artists, features, weeks,
                        labels):

    # Creating dataframe structure to be written to Excel:
    # (Some songs are missing Promotion Label data)
    try:
        df = pd.DataFrame({'Date': date_str, 'Ranking': rankings, 'Song': songs,
                           'Artist': artists, 'Features': features,
                           'Weeks on Chart': weeks, 'Promotion Labels': labels})
    except:
        df = pd.DataFrame({'Date': date_str, 'Ranking': rankings, 'Song': songs,
                           'Artist': artists, 'Features': features,
                           'Weeks on Chart': weeks})



    return df

    print("Successful data writing!")
    print(df)
    
    ###############################
    ###############################

