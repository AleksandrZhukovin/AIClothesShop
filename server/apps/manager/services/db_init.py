from typing import List, Type

from django.db import transaction

from .initializers.base import ModelInitializer
from .initializers.catalog import CategoryInitializer


class DatabaseInitializer:
    """Service for managing database initialization."""

    def __init__(self):
        self.initializers: List[Type[ModelInitializer]] = [
            CategoryInitializer,
        ]

    @transaction.atomic
    def initialize_all(self) -> dict:
        """Initialize all registered models."""
        results = {}

        for initializer_class in self.initializers:
            initializer = initializer_class()
            model_name = initializer.model.__name__
            created_objects = initializer.initialize()

            results[model_name] = {
                "created_count": len(created_objects),
                "created_objects": created_objects,
            }

        return results
