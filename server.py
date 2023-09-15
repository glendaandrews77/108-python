from flask import Flask
from config import developer
import json

app = Flask("server")



@app.get("/")
def hello():
    return  "Hello from Flask"


@app.get("/test")
def test():
    return "Look ma!, I'm a page"


@app.get("/name")
def name():
    return"Gigi Bailey"

#################################
###########Product API###########
#################################


@app.get("/api/about")
def about_me():
    return json.dumps(developer)



# get /api/products
#send the list of products
@app.get("/api/products")
def get_products():
    products = []

    return json.dumps(products)



app.run(debug=True)