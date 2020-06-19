from django.db import models
# Create your models here.


class Channel(models.Model):
    channel_name = models.TextField(unique=False)
    channel_id = models.TextField(unique=True)

    def __str__(self):
        return self.channel_name


class Videos(models.Model):
    title = models.TextField(unique=False)
    accessed_date = models.DateTimeField(auto_now_add=True)
    likes = models.IntegerField()
    dislikes = models.IntegerField()
    channel = models.ForeignKey(Channel, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Author(models.Model):
    name = models.TextField(unique=True)

    def __str__(self):
        return self.name


class Comments(models.Model):
    video = models.ForeignKey(Videos, on_delete=models.CASCADE)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    comment = models.TextField(unique=False)

    def __str__(self):
        return self.comment
