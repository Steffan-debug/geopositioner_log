import pymongo
import subprocess

# Connect to MongoDB
client = pymongo.MongoClient('mongodb://localhost:27017/')

# Specify the database and collection
db = client['mydatabase']
collection = db['mycollection']

# Run the Python file and capture the output
result = subprocess.run(['python', 'my_script.py'], capture_output=True)

# Insert the result into the collection
collection.insert_one({'result': result.stdout.decode()})
