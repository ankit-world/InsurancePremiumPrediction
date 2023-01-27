import pymongo # Pip install pymongo
import pandas as pd
import json


client = pymongo.MongoClient("mongodb+srv://mongodb:mongodb@cluster0.pfkbq.mongodb.net/?retryWrites=true&w=majority")
db = client.test

DATA_FILE_PATH = (r"D:\Insights\MachineLearning\InsurancePremiumPrediction\insurance.csv")
DATABASE_NAME = "INSUARNCE"
Collection_Name = "INSURANCE_PROJECT"

if __name__ == "__main__":
    df = pd.read_csv(DATA_FILE_PATH)
    print(f"Rows and columns: {df.shape}")

    df.reset_index(drop=True, inplace=True)

    # To convert the csv file to json format
    json_record = list(json.loads(df.T.to_json()).values())
    print(json_record[0])

    # To insert the record in the MongoDB database
    client[DATABASE_NAME][Collection_Name].insert_many(json_record)




