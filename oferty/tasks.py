from celery import task
from django.shortcuts import get_object_or_404
from oferty.models import Oferta
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives
from django.conf import settings
import weasyprint
from weasyprint import default_url_fetcher, HTML
from io import BytesIO

@task
def order_created(order_id):
    order = Oferta.objects.get(id=order_id)
    subject = 'Do wyceny zamówienie nr {}'.format(order.id)
    html_content = '<p><strong>Hallo, {}!</p></strong><br><p><strong></strong></p>' \
                   '<br> {}.'.format(order.imię, order.id)
    email = EmailMultiAlternatives(subject,
                                   html_content,
                                   'admin@app.com',
                                   [order.email])

    html = render_to_string('oferty/order/pdf.html', {'order': order})
    out = BytesIO()
    stylesheets = [weasyprint.CSS(settings.STATIC_ROOT + 'css/pdf.css')]

    weasyprint.HTML(string=html).write_pdf(out, stylesheets=stylesheets)
    email.attach('oferta_{}.pdf'.format(order.id),
                 out.getvalue(),
                 'application/pdf')

    email.attach_alternative(html_content, "text/html")
    email.send()
