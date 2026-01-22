from fastapi import FastAPI
from model import Product

app = FastAPI()


products = [
    {'id':1,'name':"Laptop",'price':50000,'quantity':10},
    {'id':2,'name':"Headphone",'price':20000,'quantity':4},
    {'id':3,'name':"IPhone",'price':120000,'quantity':7}
]

@app.get("/products")
def get_products():
    if len(products)==0:
        return {
            'data':None,
            'message':"Products not found",
            'success':False
        }
    else:
        return {
            'data':products,
            'message':"Products fetched successfully",
            'success':True
        }
    
@app.post("/products")  
def add_product(product:Product):
    for k,v in product:
        if v == None:
            return {
                "data":None,
                "message":"All fields required",
                "success":False
            }
    else:
        products.append(product)
        return {
                "data":product,
                "message":"Product added successfully",
                "success":True
        }