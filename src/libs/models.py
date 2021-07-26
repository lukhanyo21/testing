
from django.db import models

# Create your models here.

class BaseManager(models.Manager):
    def get_queryset(self):
        return super(BaseManager, self).get_queryset().filter(deleted=False)

class BaseModel(models.Model):
    """
    An abstract base class model that provides self updating
    "created", "modified" and "deleted" fields.
    """
    created = models.DateTimeField(auto_now_add=True, null=True)
    modified = models.DateTimeField(auto_now=True)
    deleted = models.BooleanField(default=False, db_index=True)

    objects = BaseManager()

    class Meta:
        abstract = True
        default_permissions = []
