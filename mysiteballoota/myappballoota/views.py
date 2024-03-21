from django.shortcuts import render

#from django.http import HttpResponse

#def index(request):
#    return HttpResponse("Hello World!")
from .forms import CreateBookForm
from .models import Book
from django.http import HttpResponseRedirect


# Create your views here.
def home(request):
    if request.method == 'POST':
        form = CreateBookForm(request.POST)
        if form.is_valid():
            formdata = form.cleaned_data
            title = formdata['title']
            author = formdata['author']
            date = formdata['date']
            Book.objects.create(title=title, author=author, date=date)
            return HttpResponseRedirect('/success')
    else:
        form = CreateBookForm()
    return render(request, 'myappballoota/createbook.html', {'form': form})


def success(request):
    return render(request, 'myappballoota/success.html')
