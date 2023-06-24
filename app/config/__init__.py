from sanic import Sanic, response
from sanic.exceptions import NotFound
from sanic.log import logger
from sanic.request import Request as _Request
from tortoise.contrib.sanic import register_tortoise

from app.config.config import Config
from app.view import akshareBp, userApi, stockApi


class Request(_Request):
    user = None


app = Sanic("sanic-app", request_class=Request)
register_tortoise(
    app, db_url="mysql://root:@Cl9rLemOtSn$5iq@127.0.0.1:3306/stock",
    modules={"models": ["app.dao.user", "app.dao.stock_base_info"]},
    generate_schemas=False
)
app.config.update_config(config)
app.config.RESPONSE_TIMEOUT = 6000
logger.info(f'>>> Current env:{Config.SANIC_ENV} DEBUG:{Config.DEBUG}')
app.static('/static', 'dist-pro/static', name="static")
app.static('/assets', 'dist-pro/assets', name="assets")
app.static('/favicon.ico', 'dist-pro/favicon.ico', name="favicon")
app.static('/logo.png', 'dist-pro/logo.png', name="logo")
app.blueprint(akshareBp)
app.blueprint(userApi)
app.blueprint(stockApi)


@app.exception(NotFound)
async def ignore_404s(request, exception):
    return response.text("404. Oops, That page couldn't found.")


async def server_error_handler(request, exception):
    return response.text('Oops, Sanic Server Error! Please contact the blog owner',
                         status=500)


# serve index.html, built by Vue-CLI


@app.route('/')
async def handle_request(request):
    return await response.file('dist-pro/index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=Config.DEBUG)
