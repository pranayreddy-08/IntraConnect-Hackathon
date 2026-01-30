from django.core.management.base import BaseCommand
from core.models import User

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        users = [
            User(name="Admin", email="admin@company.com", role="ADMIN", skills="Management", credits_balance=1000, is_admin=True),
            User(name="Alice", email="alice@company.com", role="SDE", skills="Python,Django", credits_balance=100),
            User(name="Bob", email="bob@company.com", role="DS", skills="ML,Python", credits_balance=100),
            User(name="Charlie", email="charlie@company.com", role="FS", skills="React,Node", credits_balance=100),
        ]

        for user in users:
            user.save()

        self.stdout.write("Demo users created")
