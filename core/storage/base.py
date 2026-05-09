from abc import ABC, abstractmethod


class BaseStorage(ABC):

    @abstractmethod
    def save(self, long_url: str) -> str:
        """Save a URL and return the short code"""
        pass

    @abstractmethod
    def get(self, short_code: str) -> str | None:
        """Get the long URL from a short code, or None if not found"""
        pass

    @abstractmethod
    def delete(self, short_code: str) -> bool:
        """Delete a short code, return True if deleted False if not found"""
        pass

    @abstractmethod
    def list_all(self) -> list:
        """Return all shortened URLs"""
        pass