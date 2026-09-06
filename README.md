steps = 
1. install = python3 -m pip install geopandas pandas pyogrio
2. run = python3 extract_india.py





The important attributes = 
The original GIHS dataset contains these important fields:

Attribute	Meaning
FID	Record/object ID
Locations	Location information
Points_num	Number of VIIRS hotspot points associated with the object
Min_date	Earliest associated detection date
Max_date	Latest associated detection date
Type	GIHS classification/type
CONTINENT	Continent
Nation_Name	Country
date2012_p	Number of hotspot observations in 2012
date2013_p	Number in 2013
date2014_p	Number in 2014



The original dataset is distributed as a Shapefile, meaning the .shp, .dbf, .shx, .prj, etc. together form one GIS dataset
