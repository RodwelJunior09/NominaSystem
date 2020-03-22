from routes import app
from data.mongo_setup import global_init

def start_mongo_connection():
    global_init()

if __name__ == '__main__':
    start_mongo_connection()
    app.run("", 5000, True)