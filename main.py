from fastapi import FastAPI
from model import Product
from utils import api_response

app = FastAPI()


products = [
    {'id':1,'name':"Laptop",'price':50000,'quantity':10},
    {'id':2,'name':"Headphone",'price':20000,'quantity':4},
    {'id':3,'name':"IPhone",'price':120000,'quantity':7}
]

@app.get("/products/{product_id}")
def get_products(product_id:int):
    if len(products)==0:
        return api_response(None,"Products not found",False)
    else:
        if product_id:
            for product in products:
                if product["id"] == product_id:
                   return api_response(product,"Product fetched successfully",True)
                else:
                   return api_response(None,"Product not found",False)
        else:
             return api_response(products,"Products fetched successfully",True)
             
    
@app.post("/products")  
def add_product(product:Product):
    for _,v in product:
        if v == None:
            return api_response(None,"All fields required",False)
    else:
        products.append(product)
        return api_response(products,"Product added successfully",True)
       
        
@app.put("/products/{product_id}")
def update_product(product:Product,product_id:int):
    for prod in products:
        print(prod)
        if prod['id'] == product_id:
            prod = product
            return api_response(product,"Product updated successfully",True)     
    else:
        return api_response(None,"Product not found",False)
        
            
@app.delete("/products/{product_id}")
def delete_product(product_id:int):
    for product in products:
        if product["id"] == product_id:
            del product
            return api_response(None,"Product delete successfully",True)
    else:
        return api_response(None,"Product not found",False)