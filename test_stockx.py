#importing necessary libraries
import requests
import json
import pandas as pd
import os
from google.cloud import storage

#api to get the weather data fot the cities Los Anegeles and Detroit.
url = 'https://api.worldweatheronline.com/premium/v1/past-weather.ashx?key=97b5155c1ac049c8b1c210914210207&q=Los Angeles&format=json&date=28-JUNE-2021&enddate=05-JULY-2021&tp=24'
url1 = 'https://api.worldweatheronline.com/premium/v1/past-weather.ashx?key=97b5155c1ac049c8b1c210914210207&q=Detroit&format=json&date=28-JUNE-2021&enddate=05-JULY-2021&tp=24'

x = requests.get(url).text
x1 = requests.get(url1).text

y = json.loads(x)
y1 = json.loads(x1)

 #converted the json data to pandas dataframe.
df = pd.json_normalize(y['data'],record_path=(['weather']))
df0= pd.json_normalize(y['data'],record_path=(['weather']))

df['city'] = 'Los Angeles, United States of America'
df0['city'] = 'Detroit, United States of America'
df1 = pd.concat([df,df0])
df2 = df1.drop(['astronomy','hourly'],axis = 1)

df2.to_csv('weather.csv',index = False)
path = os.path.abspath(os.getcwd()) #absolute path to the file
#json_path = path+'service-account-file.json'

os.environ["GOOGLE_APPLICATION_CREDENTIALS"]= path+'/service-account-file.json'


def upload_blob(bucket_name, source_file_name, destination_blob_name):
  """Uploads a file to the bucket."""
  storage_client = storage.Client()
  bucket = storage_client.get_bucket(bucket_name)
  blob = bucket.blob(destination_blob_name)

  blob.upload_from_filename(source_file_name)

  print('File {} uploaded to {}.'.format(
      source_file_name,
      destination_blob_name))

upload_blob('stockx_weather_bucket','weather.csv','weather')