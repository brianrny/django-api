from django.db import models

# Create your models here.
class User(models.Model):
    # title = models.CharField(max_length=200)
    # description = models.TextField()
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)

    def __str__(self):
        """A string representation of the model."""
        return self.username
