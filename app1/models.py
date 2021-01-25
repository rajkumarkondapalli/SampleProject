from django.db import models


from django.contrib.auth.models import User

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    caption = models.CharField(max_length=200)
    content = models.CharField(max_length=1000)
    date = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(User,related_name='blog_post')
    dislikes = models.ManyToManyField(User,related_name='blog_post_dislikes')
    def total_likes(self):
        return self.likes.count()

    def __str__(self):
        return str(self.user) + ' '+ str(self.date.date())




class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment = models.CharField(max_length=1000)







