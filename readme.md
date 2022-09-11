# Платежная система

___
**FrameWork Django** (https://www.djangoproject.com/)

**Payment Stripe API** (https://stripe.com/docs/api)
___
Проект в python anywhere (http://sargisandreasyan.pythonanywhere.com/)
___

## О приложении

Проект реализует продажу товаров и их хранение

### Проект имеет 2 метода

> GET /buy/{id} с помощю которого можно покупать товар

> GET /item/{id} с помощю которого можно посмотреть информацию о товаре

> GET /order с помощю этого метода можно покупать несколько item одновременно

## Установка

    Clone git repo
    git clone https://github.com/SargisAndreasyan/Rishat

### Установка frameworks

    pip install -r requirements.txt

### Запуск приложения

    cd rishat_pr
    python manage.py runserver


