from sanic import Blueprint, response

from app.constant import Result, SUCCESS, MyEncoder
from app.service.stock import insert_of_null_stock

akshareBp = Blueprint('akshare', url_prefix='/akshare')


@akshareBp.route('/insert_of_null_stock')
async def bp_root(request):
    await insert_of_null_stock()
    ret = Result("ok", SUCCESS)
    return response.text(MyEncoder().encode(ret))
