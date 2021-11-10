## Bachup data from firebase to Mongo
### Steps to run script

1. Create a virtual environment
    ````shell script
    virtualenv venv
    ````
2. Activate virtual environment
    ````shell script
    venv\Scripts\activate
    ````
3. Install dependencies from requirements.txt
    ````shell script
    pip install -r requirements.txt
    ````
4. Create database in Mongo and replace URI in connection.py
    ````python
    def get_database():
        connection_string = "YOUR_URI"
        client = pymongo.MongoClient(connection_string)
        return client['NAME_YOUR_DB']
    ````
5. Run script
    ````shell script
    python main.py
    ````
