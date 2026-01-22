from fastapi import FastAPI
from model import Product

app = FastAPI()


products = [
    {id:1,'name':"Laptop",'price':50000,'quantity':10},
    {id:2,'name':"Headphone",'price':20000,'quantity':4},
    {id:3,'name':"IPhone",'price':120000,'quantity':7}
]

@app.get("/")
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
    
    
