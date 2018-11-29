from django.db import models

class Member(models.Model):
    user_id = models.CharField(max_length=20, primary_key=True)
    user_pw = models.CharField(max_length=20)
    user_name = models.CharField(max_length=20)
    c_date = models.DateTimeField()