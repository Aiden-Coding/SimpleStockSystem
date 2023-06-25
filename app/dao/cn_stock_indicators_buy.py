from tortoise import Model, fields


class cn_stock_indicators_buy(Model):
    id = fields.BigIntField(pk=True, source_field='id', generated=True, description='id')
    name = fields.CharField(100, source_field='name', description='名称')
    code = fields.CharField(50, unique=True, source_field='code', description='代码')
    date = fields.DateField(source_field='date', null=True, description='日期')
    rate_1 = fields.FloatField(source_field='rate_1', null=True, description='1日收益率')
    rate_2 = fields.FloatField(source_field='rate_2', null=True, description='1日收益率')
    rate_3 = fields.FloatField(source_field='rate_3', null=True, description='1日收益率')
    rate_4 = fields.FloatField(source_field='rate_4', null=True, description='1日收益率')
    rate_5 = fields.FloatField(source_field='rate_5', null=True, description='1日收益率')
    rate_6 = fields.FloatField(source_field='rate_6', null=True, description='1日收益率')
    rate_7 = fields.FloatField(source_field='rate_7', null=True, description='1日收益率')
    rate_8 = fields.FloatField(source_field='rate_8', null=True, description='1日收益率')
    rate_9 = fields.FloatField(source_field='rate_9', null=True, description='1日收益率')
    rate_10 = fields.FloatField(source_field='rate_10', null=True, description='1日收益率')
    rate_11 = fields.FloatField(source_field='rate_11', null=True, description='1日收益率')
    rate_12 = fields.FloatField(source_field='rate_12', null=True, description='1日收益率')
    rate_13 = fields.FloatField(source_field='rate_13', null=True, description='1日收益率')
    rate_14 = fields.FloatField(source_field='rate_14', null=True, description='1日收益率')
    rate_15 = fields.FloatField(source_field='rate_15', null=True, description='1日收益率')
    rate_16 = fields.FloatField(source_field='rate_16', null=True, description='1日收益率')
    rate_17 = fields.FloatField(source_field='rate_17', null=True, description='1日收益率')
    rate_18 = fields.FloatField(source_field='rate_18', null=True, description='1日收益率')
    rate_19 = fields.FloatField(source_field='rate_19', null=True, description='1日收益率')
    rate_20 = fields.FloatField(source_field='rate_20', null=True, description='1日收益率')
    rate_21 = fields.FloatField(source_field='rate_21', null=True, description='1日收益率')
    rate_22 = fields.FloatField(source_field='rate_22', null=True, description='1日收益率')
    rate_23 = fields.FloatField(source_field='rate_23', null=True, description='1日收益率')
    rate_24 = fields.FloatField(source_field='rate_24', null=True, description='1日收益率')
    rate_25 = fields.FloatField(source_field='rate_25', null=True, description='1日收益率')
    rate_26 = fields.FloatField(source_field='rate_26', null=True, description='1日收益率')
    rate_27 = fields.FloatField(source_field='rate_27', null=True, description='1日收益率')
    rate_28 = fields.FloatField(source_field='rate_28', null=True, description='1日收益率')
    rate_29 = fields.FloatField(source_field='rate_29', null=True, description='1日收益率')
    rate_30 = fields.FloatField(source_field='rate_30', null=True, description='1日收益率')
    rate_31 = fields.FloatField(source_field='rate_31', null=True, description='1日收益率')
    rate_32 = fields.FloatField(source_field='rate_32', null=True, description='1日收益率')
    rate_33 = fields.FloatField(source_field='rate_33', null=True, description='1日收益率')
    rate_34 = fields.FloatField(source_field='rate_34', null=True, description='1日收益率')
    rate_35 = fields.FloatField(source_field='rate_35', null=True, description='1日收益率')
    rate_36 = fields.FloatField(source_field='rate_36', null=True, description='1日收益率')
    rate_37 = fields.FloatField(source_field='rate_37', null=True, description='1日收益率')
    rate_38 = fields.FloatField(source_field='rate_38', null=True, description='1日收益率')
    rate_39 = fields.FloatField(source_field='rate_39', null=True, description='1日收益率')
    rate_40 = fields.FloatField(source_field='rate_40', null=True, description='1日收益率')
    rate_41 = fields.FloatField(source_field='rate_41', null=True, description='1日收益率')
    rate_42 = fields.FloatField(source_field='rate_42', null=True, description='1日收益率')
    rate_43 = fields.FloatField(source_field='rate_43', null=True, description='1日收益率')
    rate_44 = fields.FloatField(source_field='rate_44', null=True, description='1日收益率')
    rate_45 = fields.FloatField(source_field='rate_45', null=True, description='1日收益率')
    rate_46 = fields.FloatField(source_field='rate_46', null=True, description='1日收益率')
    rate_47 = fields.FloatField(source_field='rate_47', null=True, description='1日收益率')
    rate_48 = fields.FloatField(source_field='rate_48', null=True, description='1日收益率')
    rate_49 = fields.FloatField(source_field='rate_49', null=True, description='1日收益率')
    rate_50 = fields.FloatField(source_field='rate_50', null=True, description='1日收益率')
    rate_51 = fields.FloatField(source_field='rate_51', null=True, description='1日收益率')
    rate_52 = fields.FloatField(source_field='rate_52', null=True, description='1日收益率')
    rate_53 = fields.FloatField(source_field='rate_53', null=True, description='1日收益率')
    rate_54 = fields.FloatField(source_field='rate_54', null=True, description='1日收益率')
    rate_55 = fields.FloatField(source_field='rate_55', null=True, description='1日收益率')
    rate_56 = fields.FloatField(source_field='rate_56', null=True, description='1日收益率')
    rate_57 = fields.FloatField(source_field='rate_57', null=True, description='1日收益率')
    rate_58 = fields.FloatField(source_field='rate_58', null=True, description='1日收益率')
    rate_59 = fields.FloatField(source_field='rate_59', null=True, description='1日收益率')
    rate_60 = fields.FloatField(source_field='rate_60', null=True, description='1日收益率')
    rate_61 = fields.FloatField(source_field='rate_61', null=True, description='1日收益率')
    rate_62 = fields.FloatField(source_field='rate_62', null=True, description='1日收益率')
    rate_63 = fields.FloatField(source_field='rate_63', null=True, description='1日收益率')
    rate_64 = fields.FloatField(source_field='rate_64', null=True, description='1日收益率')
    rate_65 = fields.FloatField(source_field='rate_65', null=True, description='1日收益率')
    rate_66 = fields.FloatField(source_field='rate_66', null=True, description='1日收益率')
    rate_67 = fields.FloatField(source_field='rate_67', null=True, description='1日收益率')
    rate_68 = fields.FloatField(source_field='rate_68', null=True, description='1日收益率')
    rate_69 = fields.FloatField(source_field='rate_69', null=True, description='1日收益率')
    rate_70 = fields.FloatField(source_field='rate_70', null=True, description='1日收益率')
    rate_71 = fields.FloatField(source_field='rate_71', null=True, description='1日收益率')
    rate_72 = fields.FloatField(source_field='rate_72', null=True, description='1日收益率')
    rate_73 = fields.FloatField(source_field='rate_73', null=True, description='1日收益率')
    rate_74 = fields.FloatField(source_field='rate_74', null=True, description='1日收益率')
    rate_75 = fields.FloatField(source_field='rate_75', null=True, description='1日收益率')
    rate_76 = fields.FloatField(source_field='rate_76', null=True, description='1日收益率')
    rate_77 = fields.FloatField(source_field='rate_77', null=True, description='1日收益率')
    rate_78 = fields.FloatField(source_field='rate_78', null=True, description='1日收益率')
    rate_79 = fields.FloatField(source_field='rate_79', null=True, description='1日收益率')
    rate_80 = fields.FloatField(source_field='rate_80', null=True, description='1日收益率')
    rate_81 = fields.FloatField(source_field='rate_81', null=True, description='1日收益率')
    rate_82 = fields.FloatField(source_field='rate_82', null=True, description='1日收益率')
    rate_83 = fields.FloatField(source_field='rate_83', null=True, description='1日收益率')
    rate_84 = fields.FloatField(source_field='rate_84', null=True, description='1日收益率')
    rate_85 = fields.FloatField(source_field='rate_85', null=True, description='1日收益率')
    rate_86 = fields.FloatField(source_field='rate_86', null=True, description='1日收益率')
    rate_87 = fields.FloatField(source_field='rate_87', null=True, description='1日收益率')
    rate_88 = fields.FloatField(source_field='rate_88', null=True, description='1日收益率')
    rate_89 = fields.FloatField(source_field='rate_89', null=True, description='1日收益率')
    rate_90 = fields.FloatField(source_field='rate_90', null=True, description='1日收益率')
    rate_91 = fields.FloatField(source_field='rate_91', null=True, description='1日收益率')
    rate_92 = fields.FloatField(source_field='rate_92', null=True, description='1日收益率')
    rate_93 = fields.FloatField(source_field='rate_93', null=True, description='1日收益率')
    rate_94 = fields.FloatField(source_field='rate_94', null=True, description='1日收益率')
    rate_95 = fields.FloatField(source_field='rate_95', null=True, description='1日收益率')
    rate_96 = fields.FloatField(source_field='rate_96', null=True, description='1日收益率')
    rate_97 = fields.FloatField(source_field='rate_97', null=True, description='1日收益率')
    rate_98 = fields.FloatField(source_field='rate_98', null=True, description='1日收益率')
    rate_99 = fields.FloatField(source_field='rate_99', null=True, description='1日收益率')
    rate_100 = fields.FloatField(source_field='rate_100', null=True, description='1日收益率')

    def __str__(self):
        return f"I am {self.name}"

    class Meta:
        abstract = False
        table = 'cn_stock_indicators_buy'
        indexes = ["code"]  # 索引
        table_description = '股票指标买入'
