from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    photo = models.ImageField(upload_to='post/photos/',blank=True,null=True)
    video = models.FileField(upload_to='post/videos/',blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title

class Main(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    def __str__(self):
            return self.post.title