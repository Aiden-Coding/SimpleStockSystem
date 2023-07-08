from tortoise import Model, fields


class User(Model):
    id = fields.IntField(pk=True, source_field='id', generated=True)
    name = fields.CharField(50, source_field='name', unique=True)
    sex = fields.BooleanField(source_field='sex')
    password = fields.CharField(50, source_field='password')

    def __str__(self):
        return f"I am {self.name}"

    class Meta:
        abstract = False
        table = 'user'
