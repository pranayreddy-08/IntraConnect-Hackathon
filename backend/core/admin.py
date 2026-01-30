from django.contrib import admin
from .models import User, Task, CreditTransaction, ActivityLog

admin.site.register(User)
admin.site.register(Task)
admin.site.register(CreditTransaction)
admin.site.register(ActivityLog)
