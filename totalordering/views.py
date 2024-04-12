from datetime import datetime, timezone

# from django.views.decorators.csrf import csrf_protect
from django.views.decorators.http import require_http_methods
from django.shortcuts import render
from django.http import HttpResponse

from .service import create_order


@require_http_methods(["GET", "POST"])
# @csrf_protect
def orders(request):
    if request.method == 'GET':
        return render(request, 'orders.html')
    order = create_order(datetime.now(tz=timezone.utc))
    return HttpResponse("{}".format(order.id))
