
from flask import Flask, request,jsonify
import json

app = Flask(__name__)
# add our firt end pont(route)

@app.route('/')
def home():
    reponse = jsonify({
        "msg": "Welcome ç to my Books API !!"
    })
    reponse.headers["Content-Type"] = "application/json;charset=utf-8"
    return reponse

list_of_books = [
    {
        "id":1,
        "name": "livre 1"
    },
    {
        "id":2,
        "name": "livre 2"
    }
]

#give all books
@app.route('/api/books', methods=["GET","POST"])
def books():
    print("Test la!!!")
    if request.method == 'GET':
        return jsonify({"res": list_of_books})
    else:
        new_book = {
             "id": len(list_of_books)+1,
             "name": request.json["name"]+str(len(list_of_books)+1) 
        }
        print(new_book)
        list_of_books.append(new_book)
        return jsonify({"res": "book created !!!"})
@app.route('/api/books/<int:id>',methods=["GET"])
def one_book(id):
    if request.method == "GET":
        book_index = id-1
        return jsonify({"res": list_of_books[book_index]})
app.debug = True
app.run()
