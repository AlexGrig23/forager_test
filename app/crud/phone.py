"""CRUD operations for phone model."""
from app.crud.base import CRUDBase
from app.db.database import phones

crud_phone = CRUDBase(phones)
