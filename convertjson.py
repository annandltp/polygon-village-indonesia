import pandas as pd
 
df = pd.read_excel(r"C:\Users\Anan\Desktop\Make Dashboard NJOP\Villages.xlsx")
 
json_data = df.to_json(orient="records")
 
json_data_with_var = "var data = " + json_data
 
with open("output.js", "w") as json_file:
    json_file.write(json_data_with_var)
 
print("OK")
