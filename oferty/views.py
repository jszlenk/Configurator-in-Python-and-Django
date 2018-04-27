from django.shortcuts import render
from .forms import OrderCreateForm
from .tasks import order_created
from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import get_object_or_404
from .models import Oferta
from django.conf import settings
from django.http import HttpResponse
from django.template.loader import render_to_string
import weasyprint

def order_create(request):
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            order_created.delay(order.id)
            return render(request,
                          'oferty/order/utworzony.html',
                          {'order': order})
    else:
        form = OrderCreateForm()
    return render(request,
                  'oferty/order/tworz.html',
                  {'form': form})

@staff_member_required
def admin_order_pdf(request, order_id):
    order = get_object_or_404(Oferta, id=order_id)
    html = render_to_string('oferty/order/pdf.html',
                            {'order': order})
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'filename= "order_{}.pdf"'.format(order.id)
    weasyprint.HTML(string=html).write_pdf(response, stylesheets=[weasyprint.CSS(settings.STATIC_ROOT + 'css/pdf.css')])
    return response
