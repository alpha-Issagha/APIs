
from flask import Flask, request,jsonify

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
    return jsonify({"res": list_of_books})
app.debug = True
app.run()
