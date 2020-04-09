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

# Включение логгирования
logging.basicConfig(level=logging.DEBUG)
LOG = logging.getLogger('simple')

# HTTP путь ресурса, возвращающего редирект
PATH_REDIRECT_TO = f'{config.PERSONAL_AREA_PREFIX}/redirect-to-pp'

routes = web.RouteTableDef()

# Это основная страница кабинета
@routes.get(config.PERSONAL_AREA_PREFIX)
@aiohttp_jinja2.template('main.jinja2')
async def main(request):
    """Handle main example page."""
    return {
        'client_id': config.CLIENT_ID,
        'user_id': config.USER_ID,
        'iframe_src': PATH_REDIRECT_TO,
        'prefix': config.PERSONAL_AREA_PREFIX
    }

# Ресурс, отвечающий за аутентификацию пользователя по ссылке и
# перенаправление на страницу кабинета в PricePlan
@routes.get(PATH_REDIRECT_TO)
async def redirect(request):
    """Return redirect to PricePlan token-authentication resource."""
    # Создаём сессию для служебного пользователя
    async with aiohttp.ClientSession() as session:
        # Отправляем запрос для аутентификации служебного пользователя
        async with session.post(url=f'{config.PP_URL}/api/login',
                                json={'user': config.SERVICE_USERNAME,
                                      'password': config.SERVICE_PASSWORD}):
            # Следующим запросом получаем токен для целевого пользователя
            async with session.get(
                    f'{config.PP_URL}/api/users/{config.USER_ID}/reset_token/'
                    ) as resp:
                user_data = await resp.json()
                # LOG.info(f'Response JSON: {user_data}')

                # Возвращаем броузеру редирект на страницу авторизации
                # целевого пользователя по токену:
                token = user_data['data']['token']
                raise web.HTTPFound(
                    location=f'{config.PP_URL}/auth-key/{token}/')

# Ресурс, необходимый для отдачи iframeResizer.min.js
routes.static(f'{config.PERSONAL_AREA_PREFIX}/js', config.BASE_DIR)

app = web.Application()
aiohttp_jinja2.setup(
    app,
    loader=jinja2.FileSystemLoader(config.BASE_DIR))
app.add_routes(routes)
web.run_app(app)
