DEBUG = True
TESTING = False 

SERVER = 'dev'
DB_NAME = 'biomarkerkbdb'
DB_COLLECTION = 'biomarker_collection'
DB_USERNAME = 'biomarkeradmin'
DB_PASSWORD = 'biomarkerpass'
MONGO_URI = f'mongodb://{DB_USERNAME}:{DB_PASSWORD}@localhost:27017/{DB_NAME}?authSource={DB_NAME}'