from django.db import models
from markdownx.models import MarkdownxField
from phonenumber_field.modelfields import PhoneNumberField
from markdownx.utils import markdown
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