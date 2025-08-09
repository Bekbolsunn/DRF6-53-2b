from django.db import models
import uuid

class BaseModel(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, primary_key=True, unique=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True

