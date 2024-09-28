import openai
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
openai.api_key = os.environ["OPEN_AI_KEY"]

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
    prompt = '\nWhat is a better synonym: ' + word + '?'
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages = [{"role": "user", "content": prompt}],
        max_tokens = 1024,
        temperature = 0.8)
    message = completion.choices[0].message.content
    return message

# ------------------------------- MAIN ----------------------------------------
if __name__ == '__main__':
    app.run()