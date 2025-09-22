from pydantic import BaseModel
from typing import Optional

# ------------------- Categories -------------------
class CategoryCreate(BaseModel):
    category_name: str

# ------------------- Suppliers -------------------
class SupplierCreate(BaseModel):
    supplier_name: str
    contact_email: Optional[str] = None
    phone_number: Optional[str] = None

# ------------------- Products -------------------
class ProductCreate(BaseModel):
    product_name: str
    category_id: int
    price: float
    quantity_in_stock: Optional[int] = 0

# ------------------- Orders -------------------
class OrderCreate(BaseModel):
    supplier_id: int
    total_amount: Optional[float] = 0

# ------------------- OrderDetails -------------------
class OrderDetailCreate(BaseModel):
    order_id: int
    product_id: int
    quantity: int
    price: float
