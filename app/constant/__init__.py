SUCCESS = '0000'

from json import JSONEncoder

import app.strategy.enter as enter
import app.strategy.keep_increasing as keep_increasing
import app.strategy.low_atr as low_atr
import app.strategy.low_backtrace_increase as low_backtrace_increase
import app.strategy.parking_apron as parking_apron
import app.strategy.backtrace_ma250 as backtrace_ma250
import app.strategy.breakthrough_platform as breakthrough_platform
import app.strategy.climax_limitdown as climax_limitdown
import app.strategy.high_tight_flag as high_tight_flag
import app.strategy.turtle_trade as turtle_trade

TABLE_CN_STOCK_FOREIGN_KEY = {'name': 'cn_stock_foreign_key', 'cn': '股票外键',
                              'columns': ['date',  # 日期
                                          'code',  # 代码
                                          'name'  # 名称
                                          ]}
_tmp_columns = TABLE_CN_STOCK_FOREIGN_KEY['columns'].copy()
TABLE_CN_STOCK_INDICATORS_BUY = {'name': 'cn_stock_indicators_buy', 'cn': '股票指标买入',
                                 'columns': _tmp_columns}
TABLE_CN_ETF_SPOT = {'name': 'cn_etf_spot', 'cn': '每日ETF数据',
                     'columns': ['date',  # 日期
                                 'code',  # 代码
                                 'name',  # 名称
                                 'new_price',  # 最新价
                                 'change_rate',  # 涨跌幅
                                 'ups_downs',  # 涨跌额
                                 'volume',  # 成交量
                                 'deal_amount',  # 成交额
                                 'open_price',  # 开盘价
                                 'high_price',  # 最高价
                                 'low_price',  # 最低价
                                 'pre_close_price',  # 昨收
                                 'turnoverrate',  # 换手率
                                 'total_market_cap',  # 总市值
                                 'free_cap'  # 流通市值
                                 ]}
TABLE_CN_STOCK_STRATEGIES = [
    {'name': 'cn_stock_strategy_enter', 'cn': '放量上涨', 'size': 70, 'func': enter.check_volume,
     'columns': _tmp_columns},
    {'name': 'cn_stock_strategy_keep_increasing', 'cn': '均线多头', 'size': 70, 'func': keep_increasing.check,
     'columns': _tmp_columns},
    {'name': 'cn_stock_strategy_parking_apron', 'cn': '停机坪', 'size': 70, 'func': parking_apron.check,
     'columns': _tmp_columns},
    {'name': 'cn_stock_strategy_backtrace_ma250', 'cn': '回踩年线', 'size': 70, 'func': backtrace_ma250.check,
     'columns': _tmp_columns},
    {'name': 'cn_stock_strategy_breakthrough_platform', 'cn': '突破平台', 'size': 70,
     'func': breakthrough_platform.check,
     'columns': _tmp_columns},
    {'name': 'cn_stock_strategy_low_backtrace_increase', 'cn': '无大幅回撤', 'size': 70,
     'func': low_backtrace_increase.check,
     'columns': _tmp_columns},
    {'name': 'cn_stock_strategy_turtle_trade', 'cn': '海龟交易法则', 'size': 70, 'func': turtle_trade.check_enter,
     'columns': _tmp_columns},
    {'name': 'cn_stock_strategy_high_tight_flag', 'cn': '高而窄的旗形', 'size': 70,
     'func': high_tight_flag.check_high_tight,
     'columns': _tmp_columns},
    {'name': 'cn_stock_strategy_climax_limitdown', 'cn': '放量跌停', 'size': 70, 'func': climax_limitdown.check,
     'columns': _tmp_columns},
    {'name': 'cn_stock_strategy_low_atr', 'cn': '低ATR成长', 'size': 70, 'func': low_atr.check_low_increase,
     'columns': _tmp_columns}
]


class MyEncoder(JSONEncoder):
    def default(self, obj):
        return obj.__dict__


class Result:
    def __init__(self, data, code):
        self.data = data
        self.code = code


def get_field_types(cols):
    data = {}
    for k in cols:
        data[k] = cols[k]['type']
    return data


RATE_FIELDS_COUNT = 100  # N日收益率字段数目，即N值

TABLE_CN_STOCK_SPOT = {'name': 'cn_stock_spot', 'cn': '每日股票数据',
                       'columns': ['date',  # 日期
                                   'code',  # 代码
                                   'name',  # 日期
                                   'new_price',  # 最新价
                                   'change_rate',  # 涨跌幅
                                   'ups_downs',  # 涨跌额
                                   'volume',  # 成交量
                                   'deal_amount',  # 成交额
                                   'amplitude',  # 振幅
                                   'volume_ratio',  # 量比
                                   'turnoverrate',  # 换手率
                                   'open_price',  # 今开
                                   'high_price',  # 最高
                                   'low_price',  # 最低
                                   'pre_close_price',  # 昨收
                                   'speed_increase',  # 涨速
                                   'speed_increase_5',  # 5分钟涨跌
                                   'speed_increase_60',  # 60日涨跌幅
                                   'speed_increase_all',  # 年初至今涨跌幅
                                   'dtsyl',  # 市盈率动
                                   'pe9',  # 市盈率TTM
                                   'pe',  # 市盈率静
                                   'pbnewmrq',  # 市净率
                                   'basic_eps',  # 每股收益
                                   'bvps',  # 每股净资产
                                   'per_capital_reserve',  # 每股公积金
                                   'per_unassign_profit',  # 每股未分配利润
                                   'roe_weight',  # 加权净资产收益率
                                   'sale_gpr',  # 毛利率
                                   'debt_asset_ratio',  # 资产负债率
                                   'total_operate_income',  # 营业收入
                                   'toi_yoy_ratio',  # 营业收入同比增长
                                   'parent_netprofit',  # 归属净利润
                                   'netprofit_yoy_ratio',  # 归属净利润同比增长
                                   'report_date',  # 报告期
                                   'total_shares',  # 总股本
                                   'free_shares',  # 已流通股份
                                   'total_market_cap',  # 总市值
                                   'free_cap',  # 流通市值
                                   'industry',  # 所处行业
                                   'listing_date']  # 上市时间
                       }

TABLE_CN_STOCK_SPOT_BUY = {'name': 'cn_stock_spot_buy', 'cn': '基本面选股',
                           'columns': TABLE_CN_STOCK_SPOT['columns'].copy()}

CN_STOCK_FUND_FLOW = ({'name': 'stock_individual_fund_flow_rank', 'cn': '今日',
                       'columns': ['code',  # 代码
                                   'name',  # 名称
                                   'new_price',  # 最新价
                                   'change_rate',  # 涨跌幅
                                   'fund_amount',  # 今日主力净流入-净额
                                   'fund_rate',  # 今日主力净流入-净占比
                                   'fund_amount_super',  # 今日超大单净流入-净额
                                   'fund_rate_super',  # 今日超大单净流入-净占比
                                   'fund_amount_large',  # 今日大单净流入-净额
                                   'fund_rate_large',  # 今日大单净流入-净占比
                                   'fund_amount_medium',  # 今日中单净流入-净额
                                   'fund_rate_medium',  # 今日中单净流入-净占比
                                   'fund_amount_small',  # 今日小单净流入-净额
                                   'fund_rate_small']},  # 今日小单净流入-净占比
                      {'name': 'stock_individual_fund_flow_rank', 'cn': '3日',
                       'columns': ['code',  # 代码
                                   'name',  # 名称
                                   'new_price',  # 最新价
                                   'change_rate_3',  # 3日涨跌幅
                                   'fund_amount_3',  # 3日主力净流入-净额
                                   'fund_rate_3',  # 3日主力净流入-净占比
                                   'fund_amount_super_3'  # 3日超大单净流入-净额
                                   'fund_rate_super_3',  # 3日超大单净流入-净占比
                                   'fund_amount_large_3',  # 3日大单净流入-净额
                                   'fund_rate_large_3',  # 3日大单净流入-净占比
                                   'fund_amount_medium_3',  # 3日中单净流入-净额
                                   'fund_rate_medium_3',  # 3日中单净流入-净占比
                                   'fund_amount_small_3',  # 3日小单净流入-净额
                                   'fund_rate_small_3']},  # 3日小单净流入-净占比
                      {'name': 'stock_individual_fund_flow_rank', 'cn': '5日',
                       'columns': ['code',  # 代码
                                   'name',  # 名称
                                   'new_price',  # 最新价
                                   'change_rate_5',  # 5日涨跌幅
                                   'fund_amount_5',  # 5日主力净流入-净额
                                   'fund_rate_5',  # 5日主力净流入-净占比
                                   'fund_amount_super_5',  # 5日超大单净流入-净额
                                   'fund_rate_super_5',  # 5日超大单净流入-净占比
                                   'fund_amount_large_5',  # 5日大单净流入-净额
                                   'fund_rate_large_5',  # 5日大单净流入-净占比
                                   'fund_amount_medium_5',  # 5日中单净流入-净额
                                   'fund_rate_medium_5',  # 5日中单净流入-净占比
                                   'fund_amount_small_5',  # 5日小单净流入-净额
                                   'fund_rate_small_5']},  # 5日小单净流入-净占比
                      {'name': 'stock_individual_fund_flow_rank', 'cn': '10日',
                       'columns': ['code',  # 代码
                                   'name',  # 名称
                                   'new_price',  # 最新价
                                   'change_rate_10',  # 10日涨跌幅
                                   'fund_amount_10',  # 10日主力净流入-净额
                                   'fund_rate_10',  # 10日主力净流入-净占比
                                   'fund_amount_super_10',  # 10日超大单净流入-净额
                                   'fund_rate_super_10',  # 10日超大单净流入-净占比
                                   'fund_amount_large_10',  # 10日大单净流入-净额
                                   'fund_rate_large_10',  # 10日大单净流入-净占比
                                   'fund_amount_medium_10',  # 10日中单净流入-净额
                                   'fund_rate_medium_10',  # 10日中单净流入-净占比
                                   'fund_amount_small_10',  # 10日小单净流入-净额
                                   'fund_rate_small_10'  # 10日小单净流入-净占比
                                   ]
                       })

TABLE_CN_STOCK_FUND_FLOW = {'name': 'cn_stock_fund_flow', 'cn': '股票资金流向',
                            'columns': ['date'  # 所处行业
                                        ]}
for cf in CN_STOCK_FUND_FLOW:
    TABLE_CN_STOCK_FUND_FLOW['columns'].append(cf['columns'].copy())

TABLE_CN_STOCK_TOP = {'name': 'cn_stock_top', 'cn': '股票龙虎榜',
                      'columns': ['date',  # 日期
                                  'code',  # 代码
                                  'name',  # 名称
                                  'ranking_times',  # 上榜次数
                                  'sum_buy',  # 累积购买额
                                  'sum_sell',  # 累积卖出额
                                  'net_amount',  # 净额
                                  'buy_seat',  # 买入席位数
                                  'sell_seat'  # 卖出席位数
                                  ]}

TABLE_CN_STOCK_BLOCKTRADE = {'name': 'cn_stock_blocktrade', 'cn': '股票大宗交易',
                             'columns': ['date',  # 日期
                                         'code',  # 代码
                                         'name',  # 名称
                                         'new_price',  # 收盘价
                                         'change_rate',  # 涨跌幅
                                         'average_price',  # 成交均价
                                         'overflow_rate',  # 折溢率
                                         'trade_number',  # 成交笔数
                                         'sum_volume',  # 成交总量
                                         'sum_turnover',  # 成交总额
                                         'turnover_market_rate'  # 成交占比流通市值
                                         ]}

CN_STOCK_HIST_DATA = {'name': 'fund_etf_hist_em', 'cn': '基金某时间段的日行情数据库',
                      'columns': ['date',  # 日期
                                  'open',  # 开盘
                                  'close',  # 收盘
                                  'high',  # 最高
                                  'low',  # 最低
                                  'volume',  # 成交量
                                  'amount',  # 成交额
                                  'amplitude',  # 振幅
                                  'quote_change',  # 涨跌幅
                                  'ups_downs',  # 涨跌额
                                  'turnover'  # 换手率
                                  ]}

TABLE_CN_STOCK_FOREIGN_KEY = {'name': 'cn_stock_foreign_key', 'cn': '股票外键',
                              'columns': ['date',
                                          'code',
                                          'name']}

TABLE_CN_STOCK_BACKTEST_DATA = {'name': 'cn_stock_backtest_data', 'cn': '股票回归测试数据',
                                'columns': ['rate_%s' % i for i in range(1, RATE_FIELDS_COUNT + 1, 1)  # %s日收益率
                                            ]}

STOCK_STATS_DATA = {'name': 'calculate_indicator', 'cn': '股票统计/指标计算助手库',
                    'columns': ['close',  # 价格
                                'macd',  # dif
                                'macds',  # macd
                                'macdh',  # histogram
                                'kdjk',  # kdjk
                                'kdjd',  # kdjd
                                'kdjj',  # kdjj
                                'boll_ub',  # boll上轨
                                'boll',  # boll
                                'boll_lb',  # boll下轨
                                'trix',  # trix
                                'trix_20_sma',  # trma
                                'tema',  # tema
                                'cr',  # cr
                                'cr-ma1',  # cr-ma1
                                'cr-ma2',  # cr-ma2
                                'cr-ma3',  # cr-ma3
                                'rsi_6',  # rsi_6
                                'rsi_12',  # rsi_12
                                'rsi',  # rsi
                                'rsi_24',  # rsi_24
                                'vr',  # vr
                                'vr_6_sma',  # mavr
                                'roc',  # roc
                                'rocma',  # rocma
                                'rocema',  # rocema
                                'pdi',  # pdi
                                'mdi',  # mdi
                                'dx',  # dx
                                'adx',  # adx
                                'adxr',  # adxr
                                'wr_6',  # wr_6
                                'wr_10',  # wr_10
                                'wr_14',  # wr_14
                                'cci',  # cci
                                'cci_84',  # cci_84
                                'tr',  # tr
                                'atr',  # atr
                                'dma',  # dma
                                'dma_10_sma',  # ama
                                'obv',  # obv
                                'sar',  # sar
                                'psy',  # psy
                                'psyma',  # psyma
                                'br',  # br
                                'ar',  # ar
                                'emv',  # emv
                                'emva',  # emva
                                'bias',  # bias
                                'mfi',  # mfi
                                'mfisma',  # mfisma
                                'vwma',  # vwma
                                'mvwma',  # mvwma
                                'ppo',  # ppo
                                'ppos',  # ppos
                                'ppoh',  # ppoh
                                'wt1',  # wt1
                                'wt2',  # wt2
                                'supertrend_ub',  # supertrend_ub
                                'supertrend',  # supertrend
                                'supertrend_lb',  # supertrend_lb
                                'dpo',  # dpo
                                'madpo',  # madpo
                                'vhf',  # vhf
                                'rvi',  # rvi
                                'rvis',  # rvis
                                'fi',  # fi
                                'force_2',  # force_2
                                'force_13',  # force_13
                                'ene_ue',  # ene上轨
                                'ene',  # ene
                                'ene_le',  # ene下轨
                                'stochrsi_k',  # stochrsi_k
                                'stochrsi_d'  # stochrsi_d
                                ]}

TABLE_CN_STOCK_INDICATORS = {'name': 'cn_stock_indicators', 'cn': '股票指标数据',
                             'columns': TABLE_CN_STOCK_FOREIGN_KEY['columns'].copy()}
TABLE_CN_STOCK_INDICATORS['columns'].append(STOCK_STATS_DATA['columns'])

_tmp_columns = TABLE_CN_STOCK_FOREIGN_KEY['columns'].copy()
_tmp_columns.append(TABLE_CN_STOCK_BACKTEST_DATA['columns'])

TABLE_CN_STOCK_INDICATORS_BUY = {'name': 'cn_stock_indicators_buy', 'cn': '股票指标买入',
                                 'columns': _tmp_columns}

TABLE_CN_STOCK_INDICATORS_SELL = {'name': 'cn_stock_indicators_sell', 'cn': '股票指标卖出',
                                  'columns': _tmp_columns}

TABLE_CN_STOCK_STRATEGIES = [
    {'name': 'cn_stock_strategy_enter', 'cn': '放量上涨', 'size': 70, 'func': enter.check_volume,
     'columns': _tmp_columns},
    {'name': 'cn_stock_strategy_keep_increasing', 'cn': '均线多头', 'size': 70, 'func': keep_increasing.check,
     'columns': _tmp_columns},
    {'name': 'cn_stock_strategy_parking_apron', 'cn': '停机坪', 'size': 70, 'func': parking_apron.check,
     'columns': _tmp_columns},
    {'name': 'cn_stock_strategy_backtrace_ma250', 'cn': '回踩年线', 'size': 70, 'func': backtrace_ma250.check,
     'columns': _tmp_columns},
    {'name': 'cn_stock_strategy_breakthrough_platform', 'cn': '突破平台', 'size': 70,
     'func': breakthrough_platform.check,
     'columns': _tmp_columns},
    {'name': 'cn_stock_strategy_low_backtrace_increase', 'cn': '无大幅回撤', 'size': 70,
     'func': low_backtrace_increase.check,
     'columns': _tmp_columns},
    {'name': 'cn_stock_strategy_turtle_trade', 'cn': '海龟交易法则', 'size': 70, 'func': turtle_trade.check_enter,
     'columns': _tmp_columns},
    {'name': 'cn_stock_strategy_high_tight_flag', 'cn': '高而窄的旗形', 'size': 70,
     'func': high_tight_flag.check_high_tight,
     'columns': _tmp_columns},
    {'name': 'cn_stock_strategy_climax_limitdown', 'cn': '放量跌停', 'size': 70, 'func': climax_limitdown.check,
     'columns': _tmp_columns},
    {'name': 'cn_stock_strategy_low_atr', 'cn': '低ATR成长', 'size': 70, 'func': low_atr.check_low_increase,
     'columns': _tmp_columns}
]

STOCK_KLINE_PATTERN_DATA = {'name': 'cn_stock_pattern_recognitions', 'cn': 'K线形态',
                            'columns': [
                                'tow_crows',  # 两只乌鸦
                                'upside_gap_two_crows',  # 向上跳空的两只乌鸦
                                'three_black_crows',  # 三只乌鸦
                                'identical_three_crows',  # 三胞胎乌鸦
                                'three_line_strike',  # 三线打击
                                'dark_cloud_cover',  # 乌云压顶
                                'evening_doji_star',  # 十字暮星
                                'doji_Star',  # 十字星
                                'hanging_man',  # 上吊线
                                'hikkake_pattern',  # 陷阱
                                'modified_hikkake_pattern',  # 修正陷阱
                                'in_neck_pattern',  # 颈内线
                                'on_neck_pattern',  # 颈上线
                                'thrusting_pattern',  # 插入
                                'shooting_star',  # 射击之星
                                'stalled_pattern',  # 停顿形态
                                'advance_block',  # 大敌当前
                                'high_wave_candle',  # 风高浪大线
                                'engulfing_pattern',  # 吞噬模式
                                'abandoned_baby',  # 弃婴
                                'closing_marubozu',  # 收盘缺影线
                                'doji',  # 十字
                                'up_down_gap',  # 向上/下跳空并列阳线
                                'long_legged_doji',  # 长脚十字
                                'rickshaw_man',  # 黄包车夫
                                'marubozu',  # 光头光脚/缺影线
                                'three_inside_up_down',  # 三内部上涨和下跌
                                'three_outside_up_down',  # 三外部上涨和下跌
                                'three_stars_in_the_south',  # 南方三星
                                'three_white_soldiers',  # 三个白兵
                                'belt_hold',  # 捉腰带线
                                'breakaway',  # 脱离
                                'concealing_baby_swallow',  # 藏婴吞没
                                'counterattack',  # 反击线
                                'dragonfly_doji',  # 蜻蜓十字/T形十字
                                'evening_star',  # 暮星
                                'gravestone_doji',  # 墓碑十字/倒T十字
                                'hammer',  # 锤头
                                'harami_pattern',  # 母子线
                                'harami_cross_pattern',  # 十字孕线
                                'homing_pigeon',  # 家鸽
                                'inverted_hammer',  # 倒锤头
                                'kicking',  # 反冲形态
                                'kicking_bull_bear',  # 由较长缺影线决定的反冲形态
                                'ladder_bottom',  # 梯底
                                'long_line_candle',  # 长蜡烛
                                'matching_low',  # 相同低价
                                'mat_hold',  # 铺垫
                                'morning_doji_star',  # 十字晨星
                                'morning_star',  # 晨星
                                'piercing_pattern',  # 刺透形态
                                'rising_falling_three',  # 上升/下降三法
                                'separating_lines',  # 分离线
                                'short_line_candle',  # 短蜡烛
                                'spinning_top',  # 纺锤
                                'stick_sandwich',  # 条形三明治
                                'takuri',  # 探水竿
                                'tasuki_gap',  # 跳空并列阴阳线
                                'tristar_pattern',  # 三星
                                'unique_3_river',  # 奇特三河床
                                'upside_downside_gap'  # 上升/下降跳空三法
                            ]}

TABLE_CN_STOCK_KLINE_PATTERN = {'name': 'cn_stock_pattern', 'cn': '股票K线形态',
                                'columns': TABLE_CN_STOCK_FOREIGN_KEY['columns'].copy()}
TABLE_CN_STOCK_KLINE_PATTERN['columns'].append(STOCK_KLINE_PATTERN_DATA['columns'])


def get_field_cn(key, table):
    f = table.get('columns').get(key)
    if f is None:
        return key
    return f.get('cn')


def get_field_cns(cols):
    data = []
    for k in cols:
        data.append(cols[k]['cn'])
    return data


def get_field_types(cols):
    data = {}
    for k in cols:
        data[k] = cols[k]['type']
    return data
