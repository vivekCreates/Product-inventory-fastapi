# Product Inventory API

## API Routes

### 1. GET /products/{product_id}
Get a specific product by ID
- **Parameter**: `product_id` (integer)
- **Response**: Single product object or "Product not found"

### 2. POST /products
Add a new product
- **Body**: `{"id": int, "name": str, "price": int, "quantity": int}`
- **Requirements**: All fields required
- **Response**: Updated products list

### 3. PUT /products/{product_id}
Update an existing product
- **Parameter**: `product_id` (integer)
- **Body**: `{"id": int, "name": str, "price": int, "quantity": int}`
- **Requirements**: Product must exist
- **Response**: Updated product

### 4. DELETE /products/{product_id}
Delete a product
- **Parameter**: `product_id` (integer)
- **Requirements**: Product must exist
- **Response**: Success/not found message

## Running

```bash
pip install fastapi uvicorn pydantic
uvicorn main:app --reload
```

Access API at: `http://localhost:8000`
