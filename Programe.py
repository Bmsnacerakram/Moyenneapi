from datetime import datetime
import os 
import pandas as pd
import requests

class api :
    def __init__(self,longtitud,latitud,url=None):
        self.url = url
        self.longtitud = longtitud_user
        self.latitud = latitud_user

longtitud_user=float(input("give me ur longtitud : "))
latitud_user=float(input("give me ur latitud : "))
date=datetime.today().strftime("%Y-%m-%d")

#Api 01 : 
ap1=api(longtitud_user,latitud_user)
ap1.url=f"https://api.open-meteo.com/v1/forecast?latitude={ap1.latitud}&longitude={ap1.longtitud}&daily=temperature_2m_max&timezone=auto&start_date={date}&end_date={date}"
respond=requests.get(ap1.url)
data1=respond.json()
print(data1)

#ap2 : 
ap2=api(longtitud_user,latitud_user)

ap2.url=f"https://www.7timer.info/bin/api.pl?lon={ap2.longtitud}&lat={ap2.latitud}&product=civillight&output=json"

respond=requests.get(ap2.url)  
data2=respond.json()
print(data2)
api_key = input("Enter your WeatherAPI key: ").strip()

#ap3 : 
ap3=api(longtitud_user,latitud_user)
ap3.url =f"https://api.weatherapi.com/v1/history.json?key={api_key}&q={latitud_user},{longtitud_user}&dt={date}"
respond=requests.get(ap3.url)
data3=respond.json()
print(data3)

#-----------------------------------------------------
temp1=float(data1['daily']['temperature_2m_max'][0])
temp2 = float(data2["dataseries"][0]["temp2m"]["max"])
temp3 = float(data3["forecast"]["forecastday"][0]["day"]["maxtemp_c"])

df=pd.DataFrame({
    "tempo1":[temp1],
    "tempo2" :[temp2],
    "tempo3" :[temp3]
})
df["temporateur_moy"]=(df["tempo1"] + df["tempo2"] + df["tempo3"])/3
print("Donc table is \n ")
print(df)
print(f"Moyenne is : {df["temporateur_moy"].iloc[0]}")
# save table
if not os.path.exists("temporateur_moy") :
    os.makedirs("temporateur_moy")

df.to_csv("temporateur_moy/table.csv",index = False)



