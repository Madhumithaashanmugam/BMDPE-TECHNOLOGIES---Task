
from fastapi import HTTPException, Depends
from sqlalchemy.orm import Session
from Models.Product.models import Product
from Models.Product.schema import CreateProduct, UpdateProduct
from config.db.session import get_db
from datetime import datetime
from typing import Optional

def create_product(product: CreateProduct, db: Session = Depends(get_db)) -> Product:
    new_product = Product(
        name=product.name,
        category=product.category,
        quantity=product.quantity,
        price=product.price,
    )
    db.add(new_product)
    db.commit()
    db.refresh(new_product)
    return new_product

def get_product_by_id(product_id: str, db: Session = Depends(get_db)) -> Product:
    product = db.query(Product).filter(Product.id == product_id).first()
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product

def update_product(product_id: str, product_data: UpdateProduct, db: Session = Depends(get_db)) -> Product:
    product = get_product_by_id(product_id, db)
    if product_data.name is not None:
        product.name = product_data.name
    if product_data.category is not None:
        product.category = product_data.category
    if product_data.quantity is not None:
        if product_data.quantity < 0:
            raise HTTPException(status_code=400, detail="Quantity cannot be negative")
        product.quantity = product_data.quantity
    if product_data.price is not None:
        product.price = product_data.price

    product.updated_datetime = datetime.utcnow()
    db.commit()
    db.refresh(product)
    return product

def delete_product(product_id: str, db: Session = Depends(get_db)):
    product = get_product_by_id(product_id, db)
    db.delete(product)
    db.commit()
    return {"message": "Product deleted successfully"}

def read_products(category: Optional[str], sort_by: str, db: Session = Depends(get_db)):
    query = db.query(Product)
    if category:
        query = query.filter(Product.category == category)
    if sort_by == "asc":
        query = query.order_by(Product.price.asc())
    elif sort_by == "desc":
        query = query.order_by(Product.price.desc())
    else:
        raise HTTPException(status_code=400, detail="Invalid sort order")
    return query.all()
