# Configurator-in-Python-and-Django

![Python](https://img.shields.io/badge/Python-3.4-blue.svg)
![Django](https://img.shields.io/badge/Django-1.11-blue.svg)
![Crispy forms](https://img.shields.io/badge/Crispy_forms-1.61-blue.svg)
![WeasyPrint](https://img.shields.io/badge/WeasyPrint-0.36-blue.svg)
![RabbitMQ](https://img.shields.io/badge/RabbitMQ-3.7-blue.svg)
![Celery](https://img.shields.io/badge/Celery-4.02-blue.svg)

Creating a car design, configuration and automatic ordering of your own Mercedes transport vehicle.

### Main functionality

- Application management through the content management system (CMS)
- Configuring the advanced specification of the car according to individual needs
- Generating order specifications in a PDF file and adding it to send orders by email
- Automatically ordering and sending an email to customers
- Saving and editing orders and saving generated files to the database

### Technology

Web application based on the **Django Framework** on Backend.

>Django is a high-level Python Web framework that encourages rapid development and clean, pragmatic design. Built by experienced developers, it takes care of much of the hassle of Web development, so you can focus on writing your app without needing to reinvent the wheel. It’s free and open source.
>
>**Source:** [www.djangoproject.com](https://www.djangoproject.com)

Configurator uses **Crispy forms** and **Bootstrap** library on Frontend.

>Django crispy forms is a Django application that lets you easily build, customize and reuse forms using your favorite CSS framework, without writing template code and without having to take care of annoying details. Django crispy forms provides you with a crispy filter and crispy tag that will let you control the rendering behavior of your Django forms in a very elegant and DRY way. Have full control without writing custom form templates. All this without breaking the standard way of doing things in Django, so it plays nice with any other form application.
>
>**Source:** [http://django-crispy-forms.readthedocs.io](http://django-crispy-forms.readthedocs.io/en/latest/index.html)

Message broker is **RabbitMQ** and distributed task queue is **Celery**.

>RabbitMQ is the most widely deployed open source message broker. RabbitMQ is lightweight and easy to deploy on premises and in the cloud. It supports multiple messaging protocols. RabbitMQ can be deployed in distributed and federated configurations to meet high-scale, high-availability requirements.
>
>**Source:** [www.rabbitmq.com](https://www.rabbitmq.com/)

>Celery is an asynchronous task queue/job queue based on distributed message passing. It is focused on real-time operation, but supports scheduling as well. The execution units, called tasks, are executed concurrently on a single or more worker servers using multiprocessing, Eventlet, or gevent. Tasks can execute asynchronously (in the background) or synchronously (wait until ready).
>
>**Source:** [www.celeryproject.org](http://www.celeryproject.org/)

**WeasyPrint** converting HTML/CSS documents to PDF format.

>WeasyPrint is a visual rendering engine for HTML and CSS that can export to PDF. It aims to support web standards for printing. WeasyPrint is free software made available under a BSD license.
>
>**Source:** [www.weasyprint.org](http://weasyprint.org/)

Otherwise: HTML5, CSS3, jQuery, PostgreSQL, SQLite

### Instalation

Dependencies are installed using the command:

```python
pip install -U -r requirements.txt
```

To properly send an e-mail with a pdf file, complete the lines with the appropriate data in the settings.py file

```
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'email'
EMAIL_HOST_PASSWORD = 'pass'
```

Automatic database creation.

First of all, in the event of a change, we must prepare a migration for the previously created new model. From the main project level, issue the following command.

```python
python manage.py makemigrations app
```

We will now synchronize the database with the new model. Issue the following command to apply existing migrations.

```python
python manage.py migrate
```

To manage the administration site, we need a superuser, so from the shell level, issue the following command.

```python
python manage.py creatinguperuser
```

Run applications in the console with the command:

```python
python manage.py runserver
```

RabbitMQ required.

After installation, launch RabbitMQ using the following command issued in the shell.

```
RabbitMQ-server
```

Go to the next shell and start the Celery worker thread using the following command.

```
celery -A app worker -l info
```

### Summation

*Python is a programming language that lets you work quickly and integrate systems more effectively.<br>
Django makes it easier to build better Web apps more quickly and with less code.<br>
PyPI helps you find and install the required software.<br>
The plugs are easy to install and configure.*