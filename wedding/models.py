from django.db import models
from markdownx.models import MarkdownxField
from phonenumber_field.modelfields import PhoneNumberField
from markdownx.utils import markdown
# Create your models here.

class wedding(models.Model):
    title = models.CharField(max_length=50,  blank=False)
    author = models.CharField(max_length=50, blank=False)
    phone_number = PhoneNumberField(blank=False)
    description = MarkdownxField(blank=False)
    file_upload = models.FileField(upload_to="blog/files/%Y/%m/%d/", blank=True)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.title

    def get_content_markdown(self):
        # Post 데이터의 content 필드에 저장되어 있는 텍스트를 마크다운 문법을 적용해 HTML로 만듦
        return markdown(self.content)