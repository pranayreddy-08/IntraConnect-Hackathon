from django.db import models


class User(models.Model):
    ROLE_CHOICES = [
        ('ADMIN', 'Admin'),
        ('SDE', 'Software Engineer'),
        ('DS', 'Data Scientist'),
        ('FS', 'Full Stack Engineer'),
    ]

    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)
    skills = models.TextField(help_text="Comma separated skills")
    credits_balance = models.IntegerField(default=0)
    is_admin = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name} ({self.role})"
