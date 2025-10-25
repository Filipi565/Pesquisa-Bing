try:
    from enum import StrEnum #type: ignore
except ImportError:
    from .strenum import StrEnum

__all__ = (
    "StrEnum",
)