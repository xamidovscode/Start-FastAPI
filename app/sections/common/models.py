from tortoise.models import Model
from tortoise import fields

class Job(Model):
    name = fields.CharField(max_length=255)
    description = fields.TextField()

    def __str__(self):
        return self.name