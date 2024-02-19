from django.db import models
from django.contrib.auth.models import User

class Articles(models.Model):
    title = models.CharField(max_length=100)
    summary = models.TextField()
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    category = models.CharField(max_length=50)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    views = models.PositiveBigIntegerField(default=0)
    
    def _str_(self):
        return self.title

