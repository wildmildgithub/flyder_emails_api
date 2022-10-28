from django.db import models
from core.utils import generate_reference

class BaseModel(models.Model):
    reference  = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, auto_now_add=False)
    deleted    = models.BooleanField(default=False)

    def __str__(self):
        self.reference

    class Meta: 
        abstract = True

class CrawledEmailAddress(BaseModel):
    source = models.TextField(default="")
    value = models.CharField(max_length=50)

    def save(self, *args, **kwargs):
        if self.pk is None :
            self.reference = generate_reference(CrawledEmailAddress, 20)
        super(CrawledEmailAddress, self).save(*args, **kwargs)
