from django.db import models

# Create your models here.

class BaseModel(models.Model):
    """

    """
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Created At')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Last Updated At')
    updated_by = models.IntegerField(blank=True, null=True, verbose_name='Updated by')
    is_deleted = models.BooleanField('Is Deleted', default=False)
    deleted_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        abstract = True
        verbose_name = 'BaseModel'
        verbose_name_plural = 'BaseModels'
        index_together = ["created_at", "updated_at"]