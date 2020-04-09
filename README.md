# customer-cabinet-example

## Пример интеграции кабинета клиента PricePlan с кабинетом клиента *aaS сервиса

Пример создан для облегчения понимания типового механизма интеграции.

### Установка и запуск

Работоспособность данного примера проверялась на версиях Python 3.7 и 3.8.

Склонируйте проект командой:

```(bash)
$ git clone https://github.com/linskiy/customer-cabinet-example.git
```

Перейдите в директорию проекта:

```(bash)
$ cd customer-cabinet-example
```

Если у вас установлен [virtualenvwrapper](https://virtualenvwrapper.readthedocs.io/en/latest/), воспользуйтесь им для создания нового окружения.

Или создайте и активируйте окружение Python командами:

```(bash)
$ python3 -m venv .venv
$ . .venv/bin/activate
```

Установите зависимости:

```(bash)
(.venv) $ pip install -r requirements.txt
```

Отредактируйте файл `config.py`, заполнив соответствующие значения вашими
данными.

Запустите приложение:

```(bash)
(.venv) $ python simple.py
DEBUG:asyncio:Using selector: EpollSelector
======== Running on http://0.0.0.0:8080 ========
(Press CTRL+C to quit)
```

Откройте в броузере http://127.0.0.1:8080/pa, если вы не меняли значение
PERSONAL_AREA_PREFIX в `config.py`. Если установили своё значение, используйте
его вместо **/pa**.

Если вы видите в iframe сообщение:

**Your host is not included in available domains. Please, check your account settings.**

Убедитесь, что в вашем PricePlan в настройках (Интеграции -> Кабинет клиента ->
Настройки) в поле «Доступные домены» присутствует 127.0.0.1, а в «Разрешённый
для доступа через iframe исходный URL (или *)» — http://127.0.0.1. Или просто
введите * (asterisk) в оба поля.

Пожалуйста, ознакомьтесь с комментариями в коде проекта.