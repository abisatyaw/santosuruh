from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from  .models import ChatGroup
from .forms import ChatmessageCreateForm
@login_required
# Create your views here.
def chat_view(request):
    chat_group = get_object_or_404(ChatGroup, group_name="pubchat")
    chat_messages = chat_group.chat_messages.all()

    form = ChatmessageCreateForm()
    if request.method == 'POST':
        form = ChatmessageCreateForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.group = chat_group
            message.author = request.user 
            message.save()
            return redirect('chat')
    return render(request, "chat.html", {'chat_messages': chat_messages, 'form': form})