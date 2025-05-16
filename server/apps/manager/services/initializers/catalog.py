from typing import List

from server.apps.catalog.models import Category
from server.apps.catalog.choices import CategoryChoices
from .base import ModelInitializer


class CategoryInitializer(ModelInitializer):
    """Initializer for Category model."""

    def __init__(self):
        super().__init__(Category)

    def get_initial_data(self) -> List[dict]:
        """Return initial category data based on CategoryChoices."""
        return [
            {'name': choice.value}
            for choice in CategoryChoices
        ] 