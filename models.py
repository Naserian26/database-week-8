from sqlalchemy import Column, Integer, String, ForeignKey, DECIMAL
from database import Base

class Supplier(Base):
    __tablename__ = "Suppliers"
    supplier_id = Column(Integer, primary_key=True, index=True)
    supplier_name = Column(String(100), nullable=False)
    contact_email = Column(String(100), unique=True)
    phone_number = Column(String(20))

class Product(Base):
    __tablename__ = "Products"
    product_id = Column(Integer, primary_key=True, index=True)
    product_name = Column(String(150), nullable=False)
    category_id = Column(Integer, nullable=False)
    price = Column(DECIMAL(10,2), nullable=False)
    quantity_in_stock = Column(Integer, default=0)
