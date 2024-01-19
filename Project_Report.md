# Project Report CS 210: Introduction to Data Science Project
### İbrahim Bartık 

## Introduction

The purpose of this project is to conduct a comprehensive analysis of personal Google Account usage by leveraging data extracted from various Google products. The analysis covers three main aspects: Mapping IP Activity, YouTube Comments Analysis, Google Maps Data Analysis, and Gmail Email Data Analysis is included to gain insights into email communication patterns. Since Google products are a suit of different applications that most people use daily, they can provide good insight to our internet usage.

The project data was requested from Google. Anyone can download their own data by following the directions here: [Request account data](https://support.google.com/accounts/answer/3024190?hl=en)

However, not all data was usable in my case, most of the Google products, I noticed, were not used. (Eg. Google Classroom, Blogger etc.). Thus, upon requesting and downloading the data, I had to hand pick the potentially usable ones, and then work on them quite a lot (sometimes with scripts, sometimes by hand) to get them to be usable in my project.

The main goal of the project was to provide insight about my usage of Google's products, and myself. Which I believed I achieved with this project.

This report explains every part of the project notebook, and other files in the repo, also has the comments & future work section. 

## 1. Mapping IP Activity in Google Account

### 1.1 Data Preparation

The script `geolocation_df_prep.py` is utilized to create a geolocation dataframe from login IPs. The data is sourced from [geolocation-db.com](https://geolocation-db.com/), this website was selected because it doesn't require an API key. The resulting dataframe is cleaned, removing duplicates and null values, and then visualized on interactive maps using the `folium` library.

### 1.2 Data Overview

The geolocation dataframe consists of 61 entries with latitude and longitude information. The data is visualized on two maps, showcasing all locations and specifically those in Turkey.

These maps, along with the Google Maps Destination Map (explained below) is available on the project map browser website. [link](https://ibrahimbartik.github.io/ibartik_cs210/)

## 2. YouTube Comments Analysis

### 2.1 Data Labeling

YouTube comments data is labeled manually. Sentiment mappings are as follows: 1 = Neutral, 2 = Positive, 3 = Negative. Initially, the plan for the project was to use BERT-Turkish model for sentimental analysis. But I had to abandon this idea due to some issues with Tensorflow library.

### 2.2 Initial Naive Bayes Model and Random Forest Classifier

A Naive Bayes model and a random forest classifier are trained for sentiment prediction, but initial results show challenges in detecting positive and negative comments, indicating a potential data imbalance issue. This was verified with F1 metrics and data histogram. 

While the imbalance was seemingly not too much, the size of the data might have been contributed to this issue being resulted in more error than normal.

### 2.3 Refined Random Forest Classifier

A Random Forest classifier is implemented to address the data imbalance, but the issue persists. Further analysis includes undersampling neutral data using the `NearMiss` algorithm.

### 2.4 Model Improvement

Hyperparameter tuning is performed on the Refined Random Forest model using grid search. The best model achieved an improved F1-score for negative comments, but was still not enough for reliable use. Unfortunately, in this area, our project fell short. 

The possible causes are the size of the dataset, but also the toughness of the problem at hand. Usage of pre-trained models in the future is sure to improve this results.

## 3. Google Maps Data Analysis and Visualization

### 3.1 Data Extraction

Google Maps data is processed from the `maps_rotalar.json` file, extracting information about visited places.

### 3.2 Visualization

Coordinates of visited places are visualized on a map using the `folium` library, providing a geographical overview of my movements.
This map can also be seen on the website

## 4. Gmail Email Data Analysis & Visualization

### 4.1 Email Sender Analysis
Sender information is extracted from the Gmail mbox file, and the distribution of email senders is visualized using pie charts.

Here we see clearly that most of my mail comes from mail lists, corporations, websites I signed up for, and funnily enough, other google products. Youtube making the overwhelming amount (almost %80) of the mails I recieve. This is probably due to email notification function of YouTube, which was not turned off for me. 

### 4.2 Sender-Recipient Network Analysis

A network graph is constructed to represent sender-recipient relationships in email communication, providing insights into communication patterns. As expected from the piecharts, It is almost never ME sending the emails, rather a bunch of websites bombarding me with emails. The network graph shows this very clearly. 

I only provided the top 30 nodes, because the graph would be unlegible otherwise. 
There are also a few nodes where I've sent some emails to my other emails, and family members.

This graph analysis would be super interesting to do on an active e-mail user, nevertheless, it did confirm what charts predicted with a better visual twist.

## What Could Be Done Better & Future Plans

My future plan is to definitely use BERT-Turkish model on my Youtube Comments data. It could've provided interesting and witty insights to my internet alter-ego. 
I would also like to repeat the mailbox graph analysis with someones corporate email for example.

## Conclusion

I learned a lot while making this project, implementing different ideas due to the nature of seperate datasets provided by Google was fun, and interesting. I think I achieved what I planned, although there is still room for improvement.