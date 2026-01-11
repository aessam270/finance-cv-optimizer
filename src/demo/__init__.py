"""
Finance CV Optimizer - Demo Package

This package contains demonstration code showing the structure
and interfaces of the Finance CV Optimizer.

⚠️ This is NOT a functional implementation.
   Get the full version at: https://assam3.gumroad.com/
"""

from .models import RoleType, OptimizedCV, OptimizeRequest, OptimizeResponse
from .interfaces import BaseCVAgent, FinanceCVAgent, PDFGenerator

__all__ = [
    "RoleType",
    "OptimizedCV",
    "OptimizeRequest",
    "OptimizeResponse",
    "BaseCVAgent",
    "FinanceCVAgent",
    "PDFGenerator",
]
