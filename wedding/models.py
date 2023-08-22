from django.db import models
from markdownx.models import MarkdownxField
from phonenumber_field.modelfields import PhoneNumberField
from markdownx.utils import markdown
# Create your models here.

class wedding(models.Model):
    title = models.CharField(max_length=50,  blank=False)
    author = models.CharField(max_length=50, blank=False)
    phone_number = PhoneNumberField(blank=False)
    image = models.CharField(max_length=200)
    description = MarkdownxField(blank=False)
    file_upload = models.FileField(upload_to="blog/files/%Y/%m/%d/", blank=True)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.title