import pandas as pd

# Read Excel file into a pandas DataFrame
df = pd.read_excel(r"C:\Users\Anan\Desktop\Make Dashboard NJOP\Villages.xlsx")

# Convert DataFrame to JSON
json_data = df.to_json(orient="records")

# Add the prefix "var testJSON = " to the JSON data
json_data_with_var = "var data = " + json_data

# Write JSON data to a file
with open("output.js", "w") as json_file:
    json_file.write(json_data_with_var)

# Print "OK" to indicate that the writing process is complete
print("OK")
