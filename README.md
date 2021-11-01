# NewsArticalClassifier

#### IIITH Final project ***( By Swati Surampudi and Oggu Rachana)***

### Problem Statement:
Classify News Articles into categories - With information overload today users are inundated with news articles of all topics, even the ones which may not be relevant to users. 
Design a system which can classify incoming news articles and appropriately tag the corresponding category. Develop a data pipeline which includes the all the 
following stages of Machine Learning Project Life Cycle –
1. Data Ingestion
2. Data Preparation
3. Data segregation & Model Training
4. Model Deployment
5. Model Prediction

### Requirements:
- MongoDB for database
- Apache Zookeeper + Kafka for message streams
- Pyspark for stream processing
- POSTMAN for testing Flask API’s
- MLFLOW for model versioning +hyper-parameters versioning
- Dockers for containarizing 

### 1.Data Ingestion

- Installation of kafka in local system: https://github.com/rachanaoggu/CapstoneProject/blob/50dfcfcd2a90b28c52f3dc51e9123dd17bd29a8f/DataIngestion/How%20to%20set%20up%20Kafka%20and%20use%20consumer%20&%20producer%20part.docx
- Commands to run for data Ingestion:
- Used free new API keys from https://mediastack.com/ and https://rapidapi.com/newscatcher-api-newscatcher-api-default/api/free-news/

### 2&3.Data Preparation and Model training:

- Run following command: python data.py
- This will create a pkl file(newsclassifier_model.pkl) and topics.csv file

### 4.Model Deployment:

- Run the docker file for web app view and predection: docker-compose up

All the commands are present in commands file

### 5.Model Prediction:
Here is the our final application

![image](https://user-images.githubusercontent.com/86909953/139672660-4b399988-1ef6-4cc3-abbf-e35d69dc198c.png)

