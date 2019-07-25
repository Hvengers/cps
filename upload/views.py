from django.http import HttpResponse    #통신위함
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render

@csrf_exempt

def upload(req):
    if req.method == 'POST':
        if 'file' in req.FILES:
            file = req.FILES['file']
            filename = file._name
            file_loc='blog/static/image'
            fp = open('%s/%s' % (file_loc, filename) , 'wb')
            for chunk in file.chunks():
                fp.write(chunk)
            #print(fp)
            fp.close()
            transfer_file='image/'+filename
    return render(req, 'blog/post_list.html',{'filename':transfer_file})
    #return render(req, 'blog/post_list.html',{'taxiNumber':req.GET['taxiNumber'], 'taxiDriver':req.GET['taxiDriver']})
    #return HttpResponse('Failed to Upload File')
