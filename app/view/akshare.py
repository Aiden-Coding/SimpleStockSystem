from sanic import Blueprint, response

from app.constant import Result, SUCCESS, MyEncoder
from app.service.stock import insert_of_null_stock,update_cn_ths_stock_block

akshareBp = Blueprint('akshare', url_prefix='/akshare')


@akshareBp.route('/insert_of_null_stock')
async def bp_root(request):
    await insert_of_null_stock()
    ret = Result("ok", SUCCESS)
    return response.text(MyEncoder().encode(ret))

@akshareBp.route('/update_cn_ths_stock_block')
async def update_cn_ths_stock(request):
    await update_cn_ths_stock_block()
    ret = Result("ok", SUCCESS)
    return response.text(MyEncoder().encode(ret))
