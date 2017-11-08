from django.db import models


class Post(models.Model):

    class Meta:
        managed = True
        db_table = 'Posts'

    post_title = models.CharField(max_length = 100)
    post_content = models.TextField()


class Comment(models.Model):

    class Meta:
        managed = True
        db_table = 'Comments'

    comment_content = models.TextField(max_length=250)
    comment_post = models.ForeignKey(Post)


class User(models.Model):

    class Meta:
        managed = True
        db_table = 'Users'

    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length = 20)
    email = models.EmailField(unique = True)