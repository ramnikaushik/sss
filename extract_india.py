import geopandas as gpd
import pandas as pd

# 1. Load the actual GIHS file
shp_path = "gihs/全球高耗能工业数据集（点）.shp"

print("Loading GIHS...")
gihs = gpd.read_file(shp_path)

print("GIHS loaded successfully!")

# 2. Basic information
print("\n==============================")
print("GIHS DATASET")
print("==============================")

print("Total records:", len(gihs))

print("\nColumns:")
print(gihs.columns.tolist())

print("\nFirst 10 rows:")
print(gihs.head(10).to_string())

# 3. Show unique values of every text column
print("\n==============================")
print("CHECKING ATTRIBUTES")
print("==============================")

for column in gihs.columns:
    if gihs[column].dtype == "object":
        print("\n", column)
        print(gihs[column].dropna().unique()[:30])

# 4. Find the country column
country_column = None

for column in gihs.columns:
    name = column.lower()

    if (
        "nation" in name
        or "country" in name
        or "国家" in column
    ):
        country_column = column
        break

print("\nCountry column found:", country_column)

if country_column is None:
    print("\nCould not automatically identify country column.")
    print("Look at the Columns printed above.")
    raise SystemExit

# 5. Show countries containing India
print("\nPossible India values:")

countries = gihs[country_column].dropna().astype(str).unique()

for country in countries:
    if "india" in country.lower() or "印度" in country:
        print(country)

# 6. Filter India
india = gihs[
    gihs[country_column]
    .astype(str)
    .str.strip()
    .str.lower()
    .isin(["india", "印度"])
].copy()

print("\n==============================")
print("INDIA")
print("==============================")

print("Indian records:", len(india))

# 7. Save India data
india.to_csv(
    "GIHS_India_2012_2021.csv",
    index=False
)

print("\nCreated:")
print("GIHS_India_2012_2021.csv")

# 8. Save geographic version
india.to_file(
    "GIHS_India_2012_2021.geojson",
    driver="GeoJSON"
)

print("GIHS_India_2012_2021.geojson")

print("\n==============================")
print("DONE")
print("==============================")