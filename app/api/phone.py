"""Module for phone number related endpoints."""

from fastapi import APIRouter, HTTPException
from starlette import status

from app.crud.phone import crud_phone
from app.schemas import CreatePhoneNumber, CreatePhoneResponse

router = APIRouter()

HTTP_STATUS_BAD_REQUEST = 400


@router.post('/phones', response_model=CreatePhoneResponse, status_code=status.HTTP_201_CREATED)
async def create_phone(phone_data: CreatePhoneNumber = None) -> CreatePhoneResponse:
    """
    Create a new phone number entry in the system.

    This endpoint will add a new phone number to the system and associate it with a user.
    If the phone number already exists in the system, it will return a 400 error.

    - **phone_number**: The phone number to create. It should be in a valid format.
    - **user**: The username associated with the phone number.

    :param phone_data: CreatePhoneNumber object containing 'phone_number' and 'user' fields.
    :return: CreatePhoneResponse object with operation result message and phone data.
    :raises HTTPException: 400 error if phone number already exists in the system.
    """
    if phone_data is None:
        raise HTTPException(status_code=HTTP_STATUS_BAD_REQUEST, detail='Phone data is required')

    if crud_phone.get(key=phone_data.phone_number):
        raise HTTPException(status_code=HTTP_STATUS_BAD_REQUEST, detail='Phone number already exists')

    crud_phone.create(key=phone_data.phone_number, item=phone_data.user)

    return CreatePhoneResponse(message='Phone number created successfully', user_data=phone_data)
