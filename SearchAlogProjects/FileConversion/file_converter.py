import pandas as pd
from datetime import datetime

csv_df = pd.read_csv("employee_dataset.csv")
csv_df['timestamp'] = pd.to_datetime(datetime.now())

out_put_file_name = "employee_workbook.xlsx"

# reading excel file into multiple df with sheet names as keys
xlx_df = pd.read_excel(out_put_file_name, sheet_name=None)

# Updating the Specific df with csv df
xlx_df['Sheet3'] = csv_df

#Create a Pandas Excel writer using openpyxl as the engine
with pd.ExcelWriter(out_put_file_name, engine='openpyxl') as writer:
    # Write each DataFrame to a different sheet
    for key, value in xlx_df.items():
        xlx_df[key].to_excel(writer, sheet_name=key, index=False)

# print(xlx_df)

print(f"DataFrame written to {out_put_file_name} successfully.")