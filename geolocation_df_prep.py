import pandas as pd
import requests
import json

#Creating the IP address dataframe
df1 = pd.read_csv("ibrahimbartik.SubscriberInfo_iptable.csv")
df2 = pd.read_csv("ibrahimbartik@sabanciuniv.edu.SubscriberInfo_iptable.csv")

df = pd.concat([df1,df2],ignore_index=True)
df=df.drop(columns=["Activity Type","Raw User Agents"])


#Getting geolocation from IP addresses, and creating geolocation dataframe
ip_data = df["IP Address"]
geolocation_df = pd.DataFrame()
lats=[]
longs=[]

for ip_address in ip_data:
    request_url = 'https://geolocation-db.com/jsonp/' + ip_address
    try:
        response = requests.get(request_url)
        result = response.content.decode()
        result = result.split("(")[1].strip(")")
        result  = json.loads(result) 
        lats.append(result["latitude"])
        longs.append(result["longitude"])
    except:
        print("Error occured. Continuing...")
        continue
geolocation_df["latitude"]=lats
geolocation_df["longitude"]=longs
geolocation_df.to_csv("geolocation.csv")