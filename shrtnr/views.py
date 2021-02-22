from django.http import Http404
from django.shortcuts import render, redirect
from shrtnr.models import Shrt
from shrtnr.forms import ShrtForm
# Create your views here.


def shrtnr(request):
    form = ShrtForm()
    shrt = None
    if request.method == "POST":
        form = ShrtForm(request.POST)
        if form.is_valid():
            shrt = Shrt(url=form.cleaned_data["url"])
            shrt.save()
    return render(request, 'shrt.html', {'form': form, 'shrt': shrt})


def shrtnr_record(request, shrt):
    if request.method == "GET":
        try:
            rec = Shrt.objects.get(shrt=shrt)
        except Shrt.DoesNotExist:
            raise Http404(shrt)
        return redirect(rec.url)
    else:
        raise Http404(shrt)
