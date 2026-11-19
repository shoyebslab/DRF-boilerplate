"""
Script to seed default RBAC roles and permissions into the database.
Usage:
    python scripts/seed_roles.py
Or inside django shell:
    python manage.py shell < scripts/seed_roles.py
"""
import os
import sys
from pathlib import Path

# Setup Django environment if run directly as script
BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.append(str(BASE_DIR))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.development")

import django

django.setup()

from django.contrib.auth.models import Group, Permission

from common.constants import RoleConstants


def seed_roles_and_permissions():
    print("Seeding roles and permissions...")

    # Define roles and their standard model permission patterns
    role_definitions = {
        RoleConstants.ADMIN: {
            "description": "Full access to all system entities and configuration.",
            "permissions": Permission.objects.all(),  # All permissions
        },
        RoleConstants.MANAGER: {
            "description": "Can view, create, update, and manage users and domain models.",
            "permissions": Permission.objects.filter(
                codename__in=["view_user", "change_user", "add_user"]
            ),
        },
        RoleConstants.DOCTOR: {
            "description": "Medical professional access: manage patients and view users.",
            "permissions": Permission.objects.filter(
                codename__in=["view_user"]
            ),
        },
        RoleConstants.STAFF: {
            "description": "Hospital staff member.",
            "permissions": Permission.objects.filter(
                codename__in=["view_user"]
            ),
        },
        RoleConstants.PATIENT: {
            "description": "Hospital patient with read-only/self-service access.",
            "permissions": [],
        },
        RoleConstants.VIEWER: {
            "description": "Read-only access across the platform.",
            "permissions": Permission.objects.filter(codename__startswith="view_"),
        },
    }

    for role_name, config in role_definitions.items():
        group, created = Group.objects.get_or_create(name=role_name)
        status_msg = "Created" if created else "Existing"
        print(f"  - [{status_msg}] Role: {role_name}")

        perms = config["permissions"]
        if perms:
            group.permissions.set(perms)
            print(f"    Assigned {len(perms)} permissions.")
        else:
            group.permissions.clear()

    print("\nRole and permission seeding completed successfully!")


if __name__ == "__main__":
    seed_roles_and_permissions()
