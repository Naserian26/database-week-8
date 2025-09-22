# Inventory CRUD API

A **full-featured Inventory Management CRUD Application** built with **FastAPI** and **MySQL**, enabling management of **Suppliers, Products, Categories, Orders, and Order Details**.

---

## Table of Contents
1. [Project Overview](#project-overview)
2. [Features](#features)
3. [Tech Stack](#tech-stack)
4. [Database Design](#database-design)
5. [Setup & Installation](#setup--installation)
6. [Running the Project](#running-the-project)
7. [API Endpoints](#api-endpoints)
8. [Testing the API](#testing-the-api)
9. [Explanation of Creation](#explanation-of-creation)
10. [Folder Structure](#folder-structure)
11. [Notes](#notes)

---

## Project Overview
This project implements a **RESTful API** for inventory management, supporting CRUD operations for multiple entities:

- Suppliers
- Products
- Categories
- Orders
- Order Details

The API is documented using **Swagger UI** for easy testing.

---

## Features
- Add, view, update, and delete **Suppliers**
- Add, view, update, and delete **Products**
- Add, view, update, and delete **Categories**
- Add, view, update, and delete **Orders** and **Order Details**
- Automatically generates database tables using **SQLAlchemy**
- FastAPI’s built-in interactive docs at `/docs`

---

## Tech Stack
- **Backend:** Python 3.x, FastAPI
- **Database:** MySQL
- **ORM:** SQLAlchemy
- **Data Validation:** Pydantic
- **Server:** Uvicorn (ASGI server)

---

## Database Design

**Entities and Relationships:**

1. **Categories**
   - `category_id` (PK)
   - `category_name` (Unique, Not Null)

2. **Suppliers**
   - `supplier_id` (PK)
   - `supplier_name` (Not Null)
   - `contact_email` (Unique)
   - `phone_number`

3. **Products**
   - `product_id` (PK)
   - `product_name` (Not Null)
   - `category_id` (FK → Categories.category_id)
   - `price` (Decimal)
   - `quantity_in_stock` (Default 0)

4. **Orders**
   - `order_id` (PK)
   - `supplier_id` (FK → Suppliers.supplier_id)
   - `order_date` (Default CURRENT_DATE)
   - `total_amount` (Decimal)

5. **OrderDetails**
   - `order_detail_id` (PK)
   - `order_id` (FK → Orders.order_id)
   - `product_id` (FK → Products.product_id)
   - `quantity`
   - `price`
   - Unique constraint: `(order_id, product_id)`

**Relationships:**
- **One-to-Many:** Category → Products, Supplier → Orders, Order → OrderDetails
- Foreign key constraints ensure data consistency.

---

## Setup & Installation

1. **Clone the repository:**
```bash
git clone <your-github-repo-url>
cd inventory_crudCreate a virtual environment:

python -m venv venv


Activate the virtual environment:

Windows PowerShell:

.\venv\Scripts\Activate.ps1

unning the Project

Start the FastAPI server:

uvicorn main:app --reload


API runs at: http://127.0.0.1:8000



