"""Module containing phone number-related Pydantic schemas."""

import re

from pydantic import BaseModel, Field, validator

MAX_USERNAME_LENGTH = 50
MIN_USERNAME_LENGTH = 3
US_PHONE_PATTERN = re.compile(r'^\+\d{1,3}-\d{1,3}-\d{3}-\d{4}$')


class CreatePhoneNumber(BaseModel):
    """Schema to create a new phone number."""

    phone_number: str = Field(..., example='+1-555-555-5555')
    user: str = Field(..., min_length=MIN_USERNAME_LENGTH, max_length=MAX_USERNAME_LENGTH, example='username')

    @validator('phone_number')
    @classmethod
    def validate_phone_number(cls, phone_number: str) -> str:
        """
        Validate the phone number format.

        For example, US format: +1-555-555-5555.

        :param phone_number: Phone number to validate.
        :return: The validated phone number.
        :raises ValueError: If the phone number format is invalid.
        """
        if not US_PHONE_PATTERN.match(phone_number):
            raise ValueError('Invalid phone number format')
        return phone_number


class CreatePhoneResponse(BaseModel):
    """Schema for creating phone number response."""

    message: str = Field(..., example='Phone number created successfully.')
    user_data: CreatePhoneNumber = Field(
        ..., example={'phone_number': '+1-555-555-5555', 'user': 'John Doe'},
    )
