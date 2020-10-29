from django.db import models

class Users_Input(models.Model):
  users_input = models.TextField(max_length=300)