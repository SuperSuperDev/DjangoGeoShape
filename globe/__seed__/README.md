# Seed Data

This app uses shapefiles to seed data, using .shp files for Country, Province, District and SubDistrict. Due to the large size of the shp files (many are over 1GB), the initial seed can be done using the Django loaddata command for a set which has alreqady been added to the database previously.

 For testing purposes I used shp files for Thailand. The json dumpfile is too large (729.8 MB) to upload to github but this can be downloaded from:

 [https://drive.infomaniak.com/app/share/143361/f1d274af-2c94-472b-bac4-d0a1693ef4c4/785224/download]('https://drive.infomaniak.com/app/share/143361/f1d274af-2c94-472b-bac4-d0a1693ef4c4/785224/download)

The original shp files can be found at:

[humdata.org]('https://data.humdata.org/dataset/thailand-administrative-boundaries')
