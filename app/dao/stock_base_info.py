from tortoise import Model, fields


class StockBaseInfo(Model):
    id = fields.BigIntField(pk=True, source_field='id', generated=True)
    name = fields.CharField(100, source_field='name')
    code = fields.CharField(50, unique=True, source_field='code')
    latestPrice = fields.FloatField(source_field='latest_price', null=True)

    def __str__(self):
        return f"I am {self.name}"

    class Meta:
        abstract = False
        table = 'stock_base_info'

    async def insert_stockBaseInfos(stockBaseInfos):
        # goods = [StockBaseInfo(**data) for data in stockBaseInfos]
        await StockBaseInfo.bulk_create(stockBaseInfos)
