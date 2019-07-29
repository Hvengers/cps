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
            fp = open('%s/%s' % (file_loc, 'inner.jpg') , 'wb')
            for chunk in file.chunks():
                fp.write(chunk)
            #print(fp)
            fp.close()
            transfer_file='image/'+filename
            return render(req, 'blog/post_list.html',{})

    elif req.method == 'GET':
        file_loc='blog/static/info'
        fp = open('%s/%s' % (file_loc,'info.txt') , 'r+')
        # w+로 열면 파일 내용 지워 버림. r+가 적당. 모두 파일 스트림 시작에 위칠
        #a=req.GET.get['taxiNumber']+'\n'
        #b=req.GET.get['taxiDriver']+'\n'
        #fp.write(a)
        #fp.write(b)
        if 'taxiNumber' in req.GET:     #하나만 들어오진 않고, 무조건 다 들어오니 하나만 체크하면 됨.
            taxiNumber=req.GET['taxiNumber']
            taxiDriver=req.GET['taxiDriver']
            #print("always get")
            fp.write(taxiNumber)
            fp.write('\n')
            fp.write(taxiDriver)
            fp.write('\n')
        else:
            #print("not always get")
            taxiNumber=fp.readline()
            taxiDriver=fp.readline()

        fp.close()

        return render(req, 'blog/post_list.html',{'taxiNumber':taxiNumber, 'taxiDriver':taxiDriver})


#그냥 보내도 GET으로 받아짐. 필요없음 기본적으로 GET.
#    else :
#        file_loc='blog/static/info'
#        fp=open("%s/%s" % (file_loc,'info.txt'),'r')
#        taxiNumber=fp.readline()
#        taxiDriver=fp.readline()
#        print(taxiNumber)
        #print("%s , %s" %(taxiNumber,taxiDriver))
#        fp.close()
    return render(req,'blog/post_list.html',{})
    #return render(req,'blog/post_list.html',{'taxiNumber':taxiNumber, 'taxiDriver':taxiDriver})
