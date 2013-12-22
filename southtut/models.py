from django.db import models

class Knight(models.Model):
    name = models.CharField(max_length = 100, unique = True)
    of_the_round_table = models.BooleanField()
    dances_whenever_able = models.BooleanField(default = False)
    sh = models.IntegerField(null = False)

class Group(models.Model):
    name = models.CharField(max_length = 100)
    facebook_page_id = models.CharField(max_length = 255)

