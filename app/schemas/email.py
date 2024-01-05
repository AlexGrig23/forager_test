"""Module containing email-related Pydantic schemas."""

from pydantic import BaseModel, EmailStr, Field

MAX_USERNAME_LENGTH = 50
MIN_USERNAME_LENGTH = 3


class CreateEmail(BaseModel):
    """Schema to create a new email."""

    email: EmailStr = Field(..., example='user@example.com')
    user: str = Field(..., min_length=MIN_USERNAME_LENGTH, max_length=MAX_USERNAME_LENGTH, example='username')


class CreateEmailResponse(BaseModel):
    """Schema for creating email response."""

    message: str = Field(..., example='Email created successfully.')
    user_data: CreateEmail = Field(
        ..., example={'email': 'user@example.com', 'user': 'John Doe'},
    )
