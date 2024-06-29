import pandas as pd


def normalize_dataframe(df, high_value_one=True):
    if high_value_one:
        normalized_df = (df - df.min()) / (df.max() - df.min())
    else:
        normalized_df = (df.max() - df) / (df.max() - df.min())
    return normalized_df




# Path to the Excel file
excel_file_path = 'data/extended_thruster_data.xlsx'  # Update this with your actual file path

df = pd.read_excel(excel_file_path)

name = df['Name']
mass = df['Filled Tank Mass (kg)']
size = df['Propellant Volume (m^3)']
power = df['Power (W)'].fillna(0)
isp = df['Isp (s)']
wet_mass = df['Wet Mass (kg)'] # with this you can see if data is complete
complete_data = wet_mass.notnull()


mass_score = normalize_dataframe(mass, high_value_one=False)
size_score = normalize_dataframe(size, high_value_one=False)
power_score = normalize_dataframe(power, high_value_one=False)
isp_score = normalize_dataframe(isp)
complete_data_score = complete_data.astype(int)

total_score = 0.4*mass_score + 0.2*size_score + 0.2*power_score + 0.1*isp_score + 0.1*complete_data_score

trade_off_table_numerical = pd.DataFrame({'Name': name, 'Mass': mass, 'Size': size, 'Power': power, 'Isp': isp, 'Complete Data': complete_data_score})
trade_off_table_scores = pd.DataFrame({'Name': name, 'Mass (40%)': mass_score, 'Size (20%)': size_score, 'Power (20%)': power_score, 'Isp (10%)': isp_score, 'Complete Data (10%)': complete_data_score, 'Total Score': total_score})
trade_off_table_scores = trade_off_table_scores.sort_values(by='Total Score', ascending=False)

# Call the function

trade_off_table_numerical.to_excel('data/trade_off_table_numerical.xlsx', index=False)
trade_off_table_scores.to_excel('data/trade_off_table_scores.xlsx', index=False)

print(f"Trade-off tables saved")










