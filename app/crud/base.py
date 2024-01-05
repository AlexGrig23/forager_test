"""Module for basic CRUD operations."""

from typing import Any


class CRUDBase:
    """Base class for CRUD operations."""

    def __init__(self, db):
        """
        Initialize the database for CRUD operations.

        :param db: Dictionary to store data.
        """
        self.data_storage = db

    def create(self, key: str, user_name: str) -> str:
        """
        Create a new item in the database.

        :param user_name:
        :param key: Key for the new item.
        :param user_name: Value for the new item.
        :return: The added value.
        :raises ValueError: If the key already exists.
        """
        if key in self.data_storage:
            raise ValueError('Key already exists.')
        self.data_storage[key] = user_name
        return user_name

    def get(self, key: str) -> str:
        """
        Return an item by its key.

        :param key: The key of the item to retrieve.
        :return: The value of the item.
        """
        return self.data_storage.get(key)

    def update(self, key: str, user_name: str) -> str:
        """
        Update an item in the database.

        :param key: The key of the item to be updated.
        :param user_name: The new value for the item.
        :return: The updated value.
        :raises KeyError: If the key does not exist.
        """
        if key not in self.data_storage:
            raise KeyError('Key does not exist.')
        self.data_storage[key] = user_name
        return user_name

    def delete(self, key: str) -> Any:
        """
        Delete an item from the database.

        :param key: The key of the item to be deleted.
        :return: The value of the deleted item.
        :raises KeyError: If the key does not exist.
        """
        if key not in self.data_storage:
            raise KeyError('Key does not exist.')
        return self.data_storage.pop(key)
