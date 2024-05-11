import json 

# Load JSON data from file
with open("C:/Users/Anan/Downloads/indonesia_villages_border.json", "r", encoding="utf-8") as input_file:
    data = json.load(input_file)

# Initialize list for features
features = []

# Iterate through data and create GeoJSON features
for d in data:
    feature = {
        "type": "Feature",
        "geometry": {
            "type": "Polygon",
            "coordinates": [d["border"]]
        },
        "properties": {
            "province": d["province"],
            "district": d["district"],
            "sub_district": d["sub_district"],
            "village": d["village"]
        }
    }
    features.append(feature)

# Create GeoJSON object
geojson = {
    "type": "FeatureCollection",
    "features": features
}

# Print GeoJSON object
# print(json.dumps(geojson, indent=4))

# Write GeoJSON object to file
with open("C:/Users/Anan/Downloads/123.geojson", "w", encoding="utf-8") as output_file:
    json.dump(geojson, output_file)



