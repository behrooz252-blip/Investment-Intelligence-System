"""
Base class for all data sources.
"""

from abc import ABC, abstractmethod


class BaseDataSource(ABC):
    """
    Abstract base class for all market data providers.
    """

    @abstractmethod
    def connect(self):
        """Connect to data source."""
        pass

    @abstractmethod
    def fetch(self):
        """Fetch raw data."""
        pass

    @abstractmethod
    def validate(self, data):
        """Validate fetched data."""
        pass

    @abstractmethod
    def save(self, data):
        """Save validated data."""
        pass