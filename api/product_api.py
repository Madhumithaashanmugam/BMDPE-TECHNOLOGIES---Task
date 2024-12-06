
from fastapi import APIRouter, Depends, Query
from typing import Optional, List
from Models.Product.schema import CreateProduct, UpdateProduct, ViewProduct
from config.db.session import get_db
from sqlalchemy.orm import Session
from services.product_service import (
    create_product,
    get_product_by_id,
    update_product,
    delete_product,
    read_products,
)

router = APIRouter(tags=["products"])

@router.post("/products", response_model=ViewProduct, status_code=201)
def create_product_api(product: CreateProduct, db: Session = Depends(get_db)):
    return create_product(product, db)

@router.get("/products/{product_id}", response_model=ViewProduct)
def get_product_by_id_api(product_id: str, db: Session = Depends(get_db)):
    return get_product_by_id(product_id, db)

@router.put("/products/{product_id}", response_model=ViewProduct)
def update_product_api(product_id: str, product: UpdateProduct, db: Session = Depends(get_db)):
    return update_product(product_id, product, db)

@router.delete("/products/{product_id}")
def delete_product_api(product_id: str, db: Session = Depends(get_db)):
    return delete_product(product_id, db)

@router.get("/products", response_model=List[ViewProduct])
def read_products_api(
    category: Optional[str] = Query(None),
    sort_by: Optional[str] = Query("asc", regex="^(asc|desc)$"),
    db: Session = Depends(get_db)
):
    return read_products(category, sort_by, db)
