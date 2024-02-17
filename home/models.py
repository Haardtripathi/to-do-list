from django.db import models

# Create your models here.
class Tasks(models.Model):
    task=models.CharField(max_length=300)
    status=models.BooleanField(default=False)
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.task