from flask import Flask
from flask_restful import Api, Resource, reqparse
import random
app = Flask(__name__)
api = Api(app)

life_quotes = [
    {
        "id": 0,
        "author": "Rolly - 101 Dalmations",
        "quote": "I'm so hungry I could eat a... a whole elephant."
    },
    {
        "id": 1,
        "author": "Dante Alighieri",
        "quote": "The darkest places in hell are reserved for those who maintain their neutrality in times of moral crisis."
    },
    {
        "id": 2,
        "author": "Hulk Hogan",
        "quote": "Watcha gonna do when the hulkster runs wild on YOU?"
    },
    {
        "id": 3,
        "author": "Jules - Pulp Fiction",
        "quote": "Hamburgers! The cornerstone of any nutritious breakfast."
    },
    {
        "id": 4,
        "author": "Lt. Gen. Lewis 'Chesty' Puller",
        "quote": "Hit hard, hit fast, hit often."
    },
    {
        "id": 5,
        "author": "Ash Ketchum - Pokemon",
        "quote": "Let's eat fast so we can eat again!"
    },
    {
        "id": 6,
        "author": "Alexander 'Dany' Jabban",
        "quote": "A double? Make it a triple."
    },
    {
        "id": 7,
        "author": "Red Hot Chili Peppers",
        "quote": "I like pelasure spiked with pain, and music is my aeroplane."
    },
    {
        "id": 8,
        "author": "Kanye West",
        "quote": "People be feeling like I'm cocky because of the s**t I say; \
            if you could imagine the s**t I think."
    },
    {
        "id": 9,
        "author": "Emma Goldman",
        "quote": "Give us what belongs to us in peace, \
            and if you don't give it to us in peace, we will take it by force."
    }
]


class Quote(Resource):
    def get(self, ID=0):
        if ID == 0:
            return random.choice(life_quotes), 200
        for quote in life_quotes:
            if quote["id"] == ID:
                return quote, 200
        return "Quote not found", 404


def post(self, ID):
    parser = reqparse.RequestParser()
    parser.add_argument("author")
    parser.add_argument("quote")
    params = parser.parse_args()
    for quote in life_quotes:
        if(id == quote["id"]):
            return f"Quote with id {ID} already exists", 400
        quote = {
          "id": int(ID),
          "author": params["author"],
          "quote": params["quote"]
        }
        life_quotes.append(quote)
        return quote, 201


def put(self, ID):
    parser = reqparse.RequestParser()
    parser.add_argument("author")
    parser.add_argument("quote")
    params = parser.parse_args()
    for quote in life_quotes:
        if ID == quote["id"]:
            quote["author"] = params["author"]
            quote["quote"] = params["quote"]
            return quote, 200
     
        quote = {
          "id": ID,
          "author": params["author"],
          "quote": params["quote"]
        }
     
        life_quotes.append(quote)
        return quote, 201


def delete(self, ID):
    global life_quotes
    life_quotes = [quote for quote in life_quotes if quote["id"] != ID]
    return f"Quote with id {ID} is deleted.", 200


api.add_resource(Quote, "/life-quotes", "/life-quotes/", "/life-quotes/<int:id>")
if __name__ == '__main__':
    app.run(debug=True)
