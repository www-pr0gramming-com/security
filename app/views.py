from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.sessions.models import Session


from django.contrib.auth.decorators import login_required
from django.views import generic

from django.contrib.auth.mixins import LoginRequiredMixin

from .mixins import CartSessionRequiredMixin


# @login_required
def home(request):
    # print(request.session)
    # print(request.session.keys())

    # request.session.set_test_cookie()
    if request.method == "POST":

        request.session["test"] = "1234"
        request.session["cart_id"] = 493950719057103

        # session = Session.objects.get(pk="3ed5bnovhvga1w3pznysui0uumu2g7sp")
        # print(session)

        # print(session.session_key)
        # print(session.session_data)
        # print(session.expire_date)

        # print(session.get_decoded())

        # test = request.session["test"]
        # print(test)

        # if request.session.test_cookie_worked():
        #     request.session.delete_test_cookie()
        #     return HttpResponse("ok")

        # else:
        #     return HttpResponse("not ok")

    return render(request, "home.html")


def session_requiring_view(request, cart_id):
    # if request.session.get("cart_id", None) is not None:

    if int(cart_id) == 1398157013:
        return HttpResponse("cart is here")
    else:
        return HttpResponse("cart is not here")


class LoginRequireHomeView(CartSessionRequiredMixin, generic.TemplateView):
    template_name = "home.html"
