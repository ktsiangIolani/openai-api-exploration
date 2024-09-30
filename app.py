from openai import OpenAI
from flask import Flask, request
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config
import os
from dotenv import load_dotenv

#Create flask app
app = Flask(__name__)

#read in the API key from the .env file
load_dotenv()
openai_api_key = os.environ["OPEN_AI_KEY"]
client = OpenAI(api_key = openai_api_key)

#CORS allows for cross-origin requests (ie requests from a different server)
CORS(app)

#Create database with SQLAlchemy
app.config.from_object(Config)

db=SQLAlchemy(app)
migrate=Migrate(app, db)

# ------------------------------- ROUTES --------------------------------------

@app.route('/api/thesaurus', methods=['POST'])
def thesaurus():
    word = request.json['word']
    print("hello!!!")
    return {'message': getSynonym(word)}

def getSynonym(word):
    prompt = '\nWhat is a better synonym: ' + word + '? Please return a terse list of synonyms.'
    completion = client.chat.completions.create(
        messages=[{"role": "user", "content": prompt}],
        model="gpt-4o")
    message = completion.choices[0].message.content
    return message

# ------------------------------- MAIN ----------------------------------------
if __name__ == '__main__':
    app.run()
