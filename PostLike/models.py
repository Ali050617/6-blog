from django.db import models
from post.models import Post
from userprofile.models import User


class PostLike(models.Model):
    VALUE_CHOICES = [
        ('like', 'Like'),
        ('dislike', 'Dislike'),
    ]

    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="likes")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    value = models.CharField(max_length=10, choices=VALUE_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('post', 'user')

    def __str__(self):
        return f"{self.user.username} - {self.post.title} ({self.value})"