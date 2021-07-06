# stockx-weather
this folder consists of two main files
1. test_stockx.py #code file
2. service-account-file.json #for connecting GCS from python

##Download both files to the same repository and execute the files from that location.
Note: if .py file is running from different path copy json file to the same location as well.

#to verify the data loaded to GCS
GCS Bucket link: https://console.cloud.google.com/storage/browser/stockx_weather_bucket
GCS Bucket name: stockx_weather_bucket

##DDL File for the table
create schema if not exists public
drop table if exists weather_daily_table
create external table stockxproject.pubilc.weather_daily_table
(
weather_date string,
maxtempC string,
maxtempF string,
mintempC string,
mintempF string,
avgtempC string,
avgtempF string,
totalSnow_cm string,
sunHour string,
uvIndex string,
city string
)
options (
    fromat = 'CSV',
    uris = ['gs://stockx_weather_bucket/weather.csv']
)

