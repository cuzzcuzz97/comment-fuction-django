from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField(blank=True, null=True,)
    slug = models.SlugField(max_length=64)

    def __str__(self):
        return self.title

class Comment(models.Model):
    username = models.CharField(max_length=64,null=False, blank=False, default="Andanh")
    description = models.TextField(max_length=500,)
    commented_at = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.username} : {self.post} {self.description}"

class Reply(models.Model):
    target = models.ForeignKey(Comment, on_delete=models.CASCADE)
    username = models.CharField(max_length=64,null=False, blank=False, default="Andanh")
    description = models.TextField(max_length=500,)
    commented_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.username} : {self.target.post}"