"""Email API endpoints."""

from fastapi import APIRouter, HTTPException
from starlette import status

from app.crud.email import crud_email
from app.schemas.email import CreateEmail, CreateEmailResponse

router = APIRouter()

HTTP_STATUS_BAD_REQUEST = 400


@router.post('/emails', response_model=CreateEmailResponse, status_code=status.HTTP_201_CREATED)
async def create_email(user_data: CreateEmail = None) -> CreateEmailResponse:
    """
    Create a new email entry in the system.

    This will create a new email and associate it with a user.
    If the email already exists, it will return a 400 error.

    - **email**: The email address to create.
    - **user**: The username associated with the email address.

    :param user_data: CreateEmail object with 'email' and 'user' fields.
    :return: CreateEmailResponse object with operation result message and email data.
    :raises HTTPException: 400 error if email already exists.
    """
    if user_data is None:
        raise HTTPException(status_code=HTTP_STATUS_BAD_REQUEST, detail='User data is required')

    if crud_email.get(key=user_data.email):
        raise HTTPException(status_code=HTTP_STATUS_BAD_REQUEST, detail='Email already exists')

    crud_email.create(key=user_data.email, item=user_data.user)

    return CreateEmailResponse(message='Email created successfully', user_data=user_data)
