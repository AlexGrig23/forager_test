"""Crud module for email model."""
from app.crud.base import CRUDBase
from app.db.database import emails

crud_email = CRUDBase(emails)
