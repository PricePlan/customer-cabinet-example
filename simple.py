"""
Пример логики backend'а для интеграции кабинета клиента PricePlan
в кабинет клиента кастомера посредством iframe.

"""
import logging
import aiohttp
from aiohttp import web
import aiohttp_jinja2
import jinja2

try:
    import config_local as config
except ImportError:
    import config

logging.basicConfig(level=logging.DEBUG)
LOG = logging.getLogger('simple')
routes = web.RouteTableDef()


@routes.get('/')
@aiohttp_jinja2.template('main.jinja2')
async def main(request):
    """Handle main example page."""
    return {
        'client_id': config.CLIENT_ID,
        'user_id': config.USER_ID,
        'iframe_src': '/redirect-to-pp'
    }


@routes.get('/redirect-to-pp')
async def redirect(request):
    """Return redirect to PricePlan token-authentication resource."""
    async with aiohttp.ClientSession() as session:
        async with session.post(url=f'{config.PP_URL}/api/login',
                                json={'user': config.SERVICE_USERNAME,
                                      'password': config.SERVICE_PASSWORD}):

            async with session.get(
                    f'{config.PP_URL}/api/users/{config.USER_ID}/reset_token/'
                    ) as resp:
                user_data = await resp.json()
                # LOG.info(f'Response JSON: {user_data}')

                # Возвращаем броузеру редирект на страницу авторизации
                # пользователя по токену:
                token = user_data['data']['token']
                raise web.HTTPFound(
                    location=f'{config.PP_URL}/auth-key/{token}/')


app = web.Application()
aiohttp_jinja2.setup(
    app,
    loader=jinja2.FileSystemLoader(config.BASE_DIR))
app.add_routes(routes)
web.run_app(app)
