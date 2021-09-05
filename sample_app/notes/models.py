# related name : filter using reverse relation:
SearchKeyword.objects.filter(match_keyword__comment_id=1)
from django.db import models

class SearchKeyword(models.Model):
    keyword_id = models.AutoField(primary_key=True)
    keyword = models.CharField(unique=True, max_length=255)

class PostComments(models.Model):
    comment_id = models.AutoField(primary_key=True)
    fk_keyword = models.ForeignKey('SearchKeyword', related_name='match_keyword',on_delete=models.CASCADE, db_column='FK_keyword_id')  



