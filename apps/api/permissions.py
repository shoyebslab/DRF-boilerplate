"""
API Permissions adopted from DRF reference standard.
"""
from common.permissions import (
    FullDjangoModelPermission,
    HasAnyRole,
    HasModelPermission,
    IsAdminOrReadOnly,
    IsOwnerOrReadOnly,
    IsSuperAdminUser,
)

__all__ = [
    "IsAdminOrReadOnly",
    "FullDjangoModelPermission",
    "IsSuperAdminUser",
    "HasAnyRole",
    "HasModelPermission",
    "IsOwnerOrReadOnly",
]
