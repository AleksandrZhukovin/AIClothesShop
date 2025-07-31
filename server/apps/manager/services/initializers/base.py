from abc import ABC, abstractmethod
from typing import Any, List, Type

from django.db import models


class ModelInitializer(ABC):
    """Base class for model data initialization."""

    def __init__(self, model: Type[models.Model]):
        self.model = model

    @abstractmethod
    def get_initial_data(self) -> List[dict]:
        """Return list of dictionaries containing initial data for the model."""
        pass

    def initialize(self) -> List[Any]:
        """Initialize the model with initial data."""
        created_objects = []
        initial_data = self.get_initial_data()

        for item_data in initial_data:
            obj, created = self.model.objects.get_or_create(**item_data)
            if created:
                created_objects.append(obj)

        return created_objects
