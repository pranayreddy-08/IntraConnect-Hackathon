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
    skills = models.TextField()
    credits_balance = models.IntegerField(default=0)
    is_admin = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Task(models.Model):
    STATUS_CHOICES = [
        ('OPEN', 'Open'),
        ('IN_PROGRESS', 'In Progress'),
        ('COMPLETED', 'Completed'),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField()
    required_skill = models.CharField(max_length=100)
    posted_by = models.ForeignKey(User, related_name='posted_tasks', on_delete=models.CASCADE)
    accepted_by = models.ForeignKey(User, related_name='accepted_tasks', null=True, blank=True, on_delete=models.SET_NULL)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='OPEN')
    created_at = models.DateTimeField(auto_now_add=True)


class CreditTransaction(models.Model):
    from_user = models.ForeignKey(User, null=True, blank=True, related_name='sent_credits', on_delete=models.SET_NULL)
    to_user = models.ForeignKey(User, related_name='received_credits', on_delete=models.CASCADE)
    amount = models.IntegerField()
    reason = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)


class ActivityLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    action = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)
