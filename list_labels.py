'''
Description: This file appends instances of Promotion Label data
                to a list, in order to count the number of
                occurences on the Hot 100 charts for each label.
                This data will be used as a measure of success.

'''


###########################
### STEP 6: SCRIPT 2: ###
# Append labels to list
########################

import pandas as pd
import xlsxwriter


# Individual sheets from 'webpage scraping.py' have been saved to
# the aggreated Excel file below:
fn = "Hot-100_data_Aggregate.xlsx"
sn = "aggregate_data_Weekly-2010s"

label_lists = []

removed_duplicates = pd.read_excel(fn, sheet_name=sn)

labels_raw = removed_duplicates['Promotion Labels']

for label_entry in labels_raw[:]:

    label_instances = label_entry.split("/")

    label_lists.append(label_instances)



all_labels = [item for labels in label_lists for item in labels]

print(all_labels)


labels_df = pd.DataFrame({"Labels": all_labels})

writer = pd.ExcelWriter("Labels_count_Weekly-2010s.xlsx", engine = "xlsxwriter", mode="w")

labels_df.to_excel(writer, index=False, header="Label Instances")

print(all_labels)

########################
########################

writer.close()