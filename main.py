from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from database import SessionLocal, engine, Base
import models
from schemas import SupplierCreate, ProductCreate, CategoryCreate, OrderCreate, OrderDetailCreate

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Inventory CRUD API")

# ------------------- DATABASE DEPENDENCY -------------------
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# ------------------- ROOT -------------------
@app.get("/")
def read_root():
    return {"message": "Welcome to Inventory CRUD API"}

# ------------------- CRUD: Categories -------------------
@app.post("/categories/")
def create_category(category: CategoryCreate, db: Session = Depends(get_db)):
    new_category = models.Category(category_name=category.category_name)
    db.add(new_category)
    db.commit()
    db.refresh(new_category)
    return new_category

@app.put("/categories/{category_id}")
def update_category(category_id: int, category: CategoryCreate, db: Session = Depends(get_db)):
    existing = db.query(models.Category).filter(models.Category.category_id == category_id).first()
    if not existing:
        raise HTTPException(status_code=404, detail="Category not found")
    existing.category_name = category.category_name
    db.commit()
    return existing

# ------------------- CRUD: Suppliers -------------------
@app.post("/suppliers/")
def create_supplier(supplier: SupplierCreate, db: Session = Depends(get_db)):
    new_supplier = models.Supplier(
        supplier_name=supplier.supplier_name,
        contact_email=supplier.contact_email,
        phone_number=supplier.phone_number
    )
    db.add(new_supplier)
    db.commit()
    db.refresh(new_supplier)
    return new_supplier

@app.put("/suppliers/{supplier_id}")
def update_supplier(supplier_id: int, supplier: SupplierCreate, db: Session = Depends(get_db)):
    existing = db.query(models.Supplier).filter(models.Supplier.supplier_id == supplier_id).first()
    if not existing:
        raise HTTPException(status_code=404, detail="Supplier not found")
    existing.supplier_name = supplier.supplier_name
    existing.contact_email = supplier.contact_email
    existing.phone_number = supplier.phone_number
    db.commit()
    return existing

# ------------------- CRUD: Products -------------------
@app.post("/products/")
def create_product(product: ProductCreate, db: Session = Depends(get_db)):
    new_product = models.Product(
        product_name=product.product_name,
        category_id=product.category_id,
        price=product.price,
        quantity_in_stock=product.quantity_in_stock
    )
    db.add(new_product)
    db.commit()
    db.refresh(new_product)
    return new_product

@app.put("/products/{product_id}")
def update_product(product_id: int, product: ProductCreate, db: Session = Depends(get_db)):
    existing = db.query(models.Product).filter(models.Product.product_id == product_id).first()
    if not existing:
        raise HTTPException(status_code=404, detail="Product not found")
    existing.product_name = product.product_name
    existing.category_id = product.category_id
    existing.price = product.price
    existing.quantity_in_stock = product.quantity_in_stock
    db.commit()
    return existing

# ------------------- CRUD: Orders -------------------
@app.post("/orders/")
def create_order(order: OrderCreate, db: Session = Depends(get_db)):
    new_order = models.Order(
        supplier_id=order.supplier_id,
        total_amount=order.total_amount
    )
    db.add(new_order)
    db.commit()
    db.refresh(new_order)
    return new_order

@app.put("/orders/{order_id}")
def update_order(order_id: int, order: OrderCreate, db: Session = Depends(get_db)):
    existing = db.query(models.Order).filter(models.Order.order_id == order_id).first()
    if not existing:
        raise HTTPException(status_code=404, detail="Order not found")
    existing.supplier_id = order.supplier_id
    existing.total_amount = order.total_amount
    db.commit()
    return existing

# ------------------- CRUD: OrderDetails -------------------
@app.post("/order-details/")
def create_order_detail(detail: OrderDetailCreate, db: Session = Depends(get_db)):
    new_detail = models.OrderDetail(
        order_id=detail.order_id,
        product_id=detail.product_id,
        quantity=detail.quantity,
        price=detail.price
    )
    db.add(new_detail)
    db.commit()
    db.refresh(new_detail)
    return new_detail

@app.put("/order-details/{order_detail_id}")
def update_order_detail(order_detail_id: int, detail: OrderDetailCreate, db: Session = Depends(get_db)):
    existing = db.query(models.OrderDetail).filter(models.OrderDetail.order_detail_id == order_detail_id).first()
    if not existing:
        raise HTTPException(status_code=404, detail="OrderDetail not found")
    existing.quantity = detail.quantity
    existing.price = detail.price
    db.commit()
    return existing
