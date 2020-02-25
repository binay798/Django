from django.db import models

# Create your models here.
class Posts(models.Model):
    desc = models.TextField()
    img = models.ImageField(upload_to='pics')
    topic = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'posts'
    
    def __str__(self):
        return f"{self.topic[:10]}..."