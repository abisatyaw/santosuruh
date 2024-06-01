
from django.contrib import messages
from django.shortcuts import render, redirect
from django.urls import reverse
from allauth.account.views import LoginView
from django.http import HttpResponseRedirect
from django.http import JsonResponse
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
    return render(request, 'home.html')


class CustomLoginView(LoginView):
    def form_invalid(self, form):
        flag = True  # Or set it to False based on your logic

        # Store the flag value in the session
        self.request.session['flag'] = flag

        # Redirect to the template where the flag is used
        return redirect('base')

# Create your views here.
