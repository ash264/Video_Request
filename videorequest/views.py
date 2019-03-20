from django.shortcuts import render,redirect
from .models import Video
from .forms import VideoForm
# Create your views here.
def index(request):
    video=Video.objects.order_by('-id')
    context={'video':video}
    return render(request,'videorequest/index.html',context)


def vrform(request):


    form=VideoForm(request.POST or None)

    if form.is_valid():
        new_req=Video(title=request.POST['reqTitle'],text=request.POST['reqText'])
        new_req.save()
        return redirect('index')

    context = {'form': form }



    return render(request,'videorequest/vrform.html',context)
