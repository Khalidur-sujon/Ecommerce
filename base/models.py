from django.db import models
import uuid

class BaseModel(models.Model):
    uid = models.CharField(primary_key=True, max_length=200, editable=False, default=uuid.uuid4)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True