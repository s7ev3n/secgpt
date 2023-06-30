"""SEC filing types"""
from secgpt.schema.base import BaseFiling
from secgpt.schmea.types import Filing10K, Filing10Q, Filing8K

__all__ = ["BaseFiling",
            "Filing10K",
            "Filing10Q",
            "Filing8K"]