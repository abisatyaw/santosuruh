from django.shortcuts import render
from django.http import HttpResponseRedirect
# from .models import Event

class HTTPResponseHXRedirect(HttpResponseRedirect):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self["HX-Redirect"] = self["Location"]

def chat_redirect(request, event_id: int):
    # event = get_object_or_404(Event, id=event_id)
    return HTTPResponseHXRedirect(redirect_to="/chat/")

# Create your views here.
def base_view(request):
    return render(request, 'index.html')
def login_view(request):
    return render(request, "login.html")
def test_view(request):
    return render(request, "test.html")
