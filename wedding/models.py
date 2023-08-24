from django.db import models
from markdownx.models import MarkdownxField
from phonenumber_field.modelfields import PhoneNumberField
from markdownx.utils import markdown
import  Wedding_project.settings
# Create your models here.

class wedding(models.Model):
    title = models.CharField(max_length=50, blank=False)
    author = models.CharField(max_length=50, blank=False)
    phone_number = PhoneNumberField(blank=False)
    description = MarkdownxField(blank=False)


    def __str__(self):
        return self.title

    def get_content_markdown(self):
        return markdown(self.content)


class CheongdamDong(models.Model):
    column1 = models.IntegerField(db_column='Column1', blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(max_length=50, blank=True, null=True)
    addr1 = models.CharField(max_length=50, blank=True, null=True)
    tel = models.CharField(max_length=50, blank=True, null=True)
    urls = models.CharField(max_length=64, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cheongdam_dong'

class Gangnam(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)
    addr1 = models.CharField(max_length=50, blank=True, null=True)
    tel = models.CharField(max_length=50, blank=True, null=True)
    urls = models.CharField(max_length=128, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gangnam'

class NonhyeonDong(models.Model):
    column1 = models.IntegerField(db_column='Column1', blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(max_length=50, blank=True, null=True)
    addr1 = models.CharField(max_length=50, blank=True, null=True)
    tel = models.CharField(max_length=50, blank=True, null=True)
    urls = models.CharField(max_length=128, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'nonhyeon_dong'

class SamseongDong(models.Model):
    column1 = models.IntegerField(db_column='Column1', blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(max_length=50, blank=True, null=True)
    addr1 = models.CharField(max_length=50, blank=True, null=True)
    tel = models.CharField(max_length=50, blank=True, null=True)
    urls = models.CharField(max_length=64, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'samseong_dong'

class SinsaDong(models.Model):
    column1 = models.IntegerField(db_column='Column1', blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(max_length=50, blank=True, null=True)
    addr1 = models.CharField(max_length=50, blank=True, null=True)
    tel = models.CharField(max_length=50, blank=True, null=True)
    urls = models.CharField(max_length=128, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sinsa_dong'