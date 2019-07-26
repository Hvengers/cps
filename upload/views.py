from django.http import HttpResponse    #통신위함
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render

#@csrf_exempt

def upload(req):
    if req.method == 'POST':
        #print("통신 되긴하는데 좀,,,,")
        if 'file' in req.FILES:
            file = req.FILES['file']
            filename = file._name
            file_loc='blog/static/image'
            fp = open('%s/%s' % (file_loc, 'inner.jpg') , 'wb')
            for chunk in file.chunks():
                fp.write(chunk)
            #print(fp)
            fp.close()
            transfer_file='image/'+filename
            return render(req, 'blog/post_list.html',{})
    #return render(req, 'blog/post_list.html',{'taxiNumber':req.GET['taxiNumber'], 'taxiDriver':req.GET['taxiDriver']})

#    elif req.method == 'GET':
#        file_loc='blog/static/info'
#        fp = open('%s/%s' % (file_loc,'info.txt') , 'w')
        #a=req.GET.get['taxiNumber']+'\n'
        #b=req.GET.get['taxiDriver']+'\n'
        #fp.write(a)
        #fp.write(b)
#        fp.write(req.GET['taxiNumber'])
#        fp.write(req.GET['taxiDriver'])
#        fp.close()
#        render(req, 'blog/post_list.html',{'taxiNumber':req.GET.get['taxiNumber'], 'taxiDriver':req.GET.get['taxiDriver']})

    else :
        file_loc='blog/static/info'
        fp=open("%s/%s" %(file_loc,'info.txt'),'r')
        taxiNumber=fp.readline()
        taxiDriver=fp.readline()
        fp.close()

    return render(req,'blog/post_list.html',{'taxiNumber':taxiNumber, 'taxiDriver':taxiDriver})
