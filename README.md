# InsurancePremiumPrediction

# Data_dump.py
```
1. Provide the connection string with username and password with MongoDB
2. Create database name and collection string in MongoDB
3. Insert the data into the MongoDB database
4. Save the code in data_dump.py file and run it in the terminal
```

# Template.py
```
1. Create folders that are required for the execution of the project
2. Run template.py file to create the folder structure
```

# Git Update
```
1. git add .
2. git commit -m "folder structure and data dump in database completed"
3. git push origin main(after signing in into your github account)
```

# setup.py
```
1.  Create setup.py file with all the require information
2. Once we run setup.py file Insurance.egg-info file will be created
```

# Git Update
```
1. git add .
2. git commit -m "setup file completed"
3. git push origin main(after signing in int your github account)
```

# Logger
```
1. update logger folder
2. Write the respective code in __init__.py file
```

# Exception
```
1. Create Exception folder
2. Inside create __init__.py file and updated it with required code.
```

# Main.py
```
1.Testing the logger and exception part with a sample code in main.py file
2.Run the main.py file and we will see logger file(defined name) created with exception.
```

# Git Update
```
1. git add .
2. git commit -m "logger & exception file updated"
3. git push origin main(after signing in int your github account)
```

# Utis.py
```
1. Create a function get_collection_as_dataframe to collect data from MongoDB database as dataframe
```

# .env
``` Create a .env file and save the url of connection string of database```


# Insurance/__init__.py
```
1. Create load_dotenv() function
```

# config.py
```
1. Create EnvironmentVariable class for variable we stored in .env file
2. define MongoDB url
```

# Main.py
```
1. Update get_collection_as_dataframe() function in main.py
2. Run main.py after requirement.txt run and we can see details of our data in logs
```

# Requirements.txt
```Update the required packages in requirements file and run it```

# Git Update
```
1. git add .
2. git commit -m "utils file and config file updated"
3. git push origin main(after signing in int your github account)
```

# Entity Folder
```
1. Create 2 files artifact_entity.py and config_entity.py used for training-testing pipelines
2. Write the respective required code in config_entity.py file
3. Create classes (TrainingPipelineConfig & DataIngestionConfig,DataValidationArtifact)
4. Write class (DataIngestionArtifact) in artifact_entity.py file.
5 Make respective updates in corresponding main.py file
```

# Git Update
```
1. git add .
2. git commit -m "config and artifact file updated"
3. git push origin main(after signing in int your github account)
```

# Components Folder-Data Ingestion
```
1. Create data_ingestion.py file and define class DataIngestion and related functions 
2. The above will create artifacts folder which will have splitted datasets
2. Update code in main.py
```

# Git Update
```
1. git add .
2. git commit -m "Data Ingestion"
3. git push origin main(after signing in int your github account)
```

# Componenet Folder - Data Validation
```
1. Create data_validation.py file and define class DataValidation and related functions
2. Update the config_entity.py, artifact_entity.py,utils.py  and main.py file simultaneously 
3. Update code in main.py
```

# Git Update
```
1. git add .
2. git commit -m "Data Validation"
3. git push origin main(after signing in int your github account)
```

# Componenet Folder - Data Transformation
```
1. Create data_transformation.py file and define class DataTransformation and related functions
2. Update the config_entity.py, artifact_entity.py,utils.py  and main.py file simultaneously 
3. Update code in main.py
```

# Git Update
```
1. git add .
2. git commit -m "Data Transformation"
3. git push origin main(after signing in int your github account)
```

# Model Trainer file
```
1. Create Model_trainer.py file in componenets folder of insuarnce folder
2. Create ModelTrainer class and its related functions
3. Update class ModelTrainingConfig in config_entity and artifact_entity, utils.py, main.py
```

# For new model when new data is received
```
1. Create ModelResolver class in predictor.py files in compnent folder and write the required functions
2. Also Update config_entity.py, artifact_entity.py, main.py file
```

# Git Update
```
1. git add .
2. git commit -m "Model Training and Evaluation"
3. git push origin main(after signing in int your github account)
```







