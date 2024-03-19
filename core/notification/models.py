from django.db import models

# Create your models here.


# notification module
class Notification(models.Model):
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.message)
