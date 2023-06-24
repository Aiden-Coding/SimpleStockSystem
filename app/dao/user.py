from tortoise import Model, fields


class User(Model):
    id = fields.IntField(pk=True, source_field='id', generated=True)
    name = fields.CharField(50)

    def __str__(self):
        return f"I am {self.name}"

    class Meta:
        abstract = False
        table = 'user'
