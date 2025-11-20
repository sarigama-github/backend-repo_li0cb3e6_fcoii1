"""
Database Schemas

Define your MongoDB collection schemas here using Pydantic models.
These schemas are used for data validation in your application.

Each Pydantic model represents a collection in your database.
Model name is converted to lowercase for the collection name:
- User -> "user" collection
- Product -> "product" collection
- BlogPost -> "blogs" collection
"""

from pydantic import BaseModel, Field, EmailStr
from typing import Optional, List

# Example schemas (retain examples for reference)

class User(BaseModel):
    """
    Users collection schema
    Collection name: "user" (lowercase of class name)
    """
    name: str = Field(..., description="Full name")
    email: str = Field(..., description="Email address")
    address: str = Field(..., description="Address")
    age: Optional[int] = Field(None, ge=0, le=120, description="Age in years")
    is_active: bool = Field(True, description="Whether user is active")

class Product(BaseModel):
    """
    Products collection schema
    Collection name: "product" (lowercase of class name)
    """
    title: str = Field(..., description="Product title")
    description: Optional[str] = Field(None, description="Product description")
    price: float = Field(..., ge=0, description="Price in dollars")
    category: str = Field(..., description="Product category")
    in_stock: bool = Field(True, description="Whether product is in stock")

# Coffee shop specific schemas

class CoffeeItem(BaseModel):
    """
    Coffee menu items
    Collection name: "coffeeitem"
    """
    name: str = Field(..., description="Drink or pastry name")
    description: Optional[str] = Field(None, description="Short description of the item")
    price: float = Field(..., ge=0, description="Price in local currency")
    category: str = Field("coffee", description="Category like coffee, tea, pastry, seasonal")
    tags: Optional[List[str]] = Field(default=None, description="Tags like hot, iced, vegan, new")
    available: bool = Field(True, description="Whether currently available")

class ContactMessage(BaseModel):
    """
    Contact messages from website form
    Collection name: "contactmessage"
    """
    name: str = Field(..., description="Sender name")
    email: EmailStr = Field(..., description="Sender email")
    message: str = Field(..., min_length=5, max_length=2000, description="Message body")
    subject: Optional[str] = Field(None, description="Optional subject")
