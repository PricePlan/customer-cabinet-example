"""
Настройки. Отредактируйте файл, подставив ваши данные.

"""
import os

# Наименование поддомена на priceplan.pro
CUSTOMER = <yourname>

# Логин и пароль пользователя с ролью «Менеджер»,
# необходимо предварительно создать в <yourname>.priceplan.pro
SERVICE_USERNAME = <service_username>
SERVICE_PASSWORD = <service_password>

# В данном примере имеется подключить кабинет только одного клиента,
# уже существующего в <yourname>.priceplan.pro.
# При этом ключевым идентификатором выступает USER_ID, т.е. id экземпляра
# пользователя, привязанного к объекту клиента c id = CLIENT_ID.
# Хорошая практика — сохранить идентификаторы пользователей клиентов на вашей
# стороне в персистентном хранилище.
CLIENT_ID = <cid>
USER_ID = <uid>

# Путь к основной странице кабинета. И префикс для остальных ресурсов.
PERSONAL_AREA_PREFIX = '/pa'

PP_DOMAIN = 'priceplan.pro'
PP_URL = f'https://{CUSTOMER}-lk.{PP_DOMAIN}'

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
