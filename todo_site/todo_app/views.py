from django.shortcuts import render,redirect
from django.contrib import messages
# Create your views here.
from todo_app.forms import TodoForm
from todo_app.models import TodoModel

def index(request):
    items_list = TodoModel.objects.order_by('-date')
    if request.method == 'POST':
        form_ = TodoForm(request.POST)
        if form_.is_valid():
            form_.save()
            return redirect('index')
    form_ = TodoForm()
    page = {
        'form_':form_,
        'list':items_list,
        'title':'TODO LIST',
    }
    return render(request,'index.html',page)

# get item_id to know which one should be deleted!

def remove(request,item_id):
    print('test remove!')
    item = TodoModel.objects.get(id=item_id)
    item.delete()
    messages.info(request,"Item removed!")
    return redirect('index')
