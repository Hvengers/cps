from django.http import HttpResponse    #통신위함
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render

@csrf_exempt

def upload(req):

    flag_safe=0
    '''safe한 경우 처리 플래그'''
    if 'safe' in req.GET:
        flag_safe=1
    if 'unsafe' in req.GET:
        flag_safe=0
        #return render(req, 'blog/post_list.html',{})

#    if req.method == 'POST':
    '''이미지 파일처리'''
    if 'file' in req.FILES:
        file = req.FILES['file']
        filename = file._name
        file_loc='blog/static/image'
        #fp = open('%s/%s' % (file_loc, 'inner.jpg') , 'wb')
        #print(filename)
        '''실내인지 범죄자인지 사진 구분'''
        if filename == 'taxiInternalPhoto.jpg':
            fp = open('%s/%s' % (file_loc, 'inner.jpg') , 'wb')
            #print("done")
        elif filename == 'CriminalPhoto.jpg':
            fp = open('%s/%s' % (file_loc, 'crime.jpg') , 'wb')

        for chunk in file.chunks():
            fp.write(chunk)

        fp.close()
#        transfer_file='image/'+filename

#    elif req.method == 'GET':
    file_loc='blog/static/info'
    fp_taxi = open('%s/%s' % (file_loc,'taxi_info.txt') , 'r+',encoding='UTF8')
    fp_crime = open('%s/%s' % (file_loc,'crime_info.txt') , 'r+',encoding='UTF8')
    fp_pay = open('%s/%s' % (file_loc,'pay_info.txt') , 'r+',encoding='UTF8')
    # w+로 열면 파일 내용 지워 버림. r+가 적당. 모두 파일 스트림 시작에 위칠


    '''template으로 보낼 딕셔너리 초기화'''
    data_dic={}
    '''택시 정보'''
    if 'taxiNumber' in req.POST:     #하나만 들어오진 않고, 무조건 다 들어오니 하나만 체크하면 됨.
        taxiNumber=req.POST['taxiNumber']
        taxiDriver=req.POST['taxiDriver']
        taxiGPS=req.POST['taxiGPS']
        taxiReportCode=req.POST['taxiReportCode']

        #print("always get")
        fp_taxi.write(taxiNumber)
        fp_taxi.write('\n')
        fp_taxi.write(taxiDriver)
        fp_taxi.write('\n')
        fp_taxi.write(taxiGPS)
        fp_taxi.write('\n')
        fp_taxi.write(taxiReportCode)
        fp_taxi.write('\n')
    else:
        #print("not always get")
        taxiNumber=fp_taxi.readline()
        taxiDriver=fp_taxi.readline()
        taxiGPS=fp_taxi.readline()
        taxiReportCode=fp_taxi.readline()

    '''범죄자 정보'''
    if 'criminalCode' in req.POST:
        criminalCode=req.POST['criminalCode']
        criminalName=req.POST['criminalName']
        fp_crime.write(criminalCode)
        fp_crime.write('\n')
        fp_crime.write(criminalName)
        fp_crime.write('\n')
    else:
        #flag_crime=1
        criminalCode=fp_crime.readline()
        criminalName=fp_crime.readline()
    '''결제 정보'''
    if 'payCode' in req.POST:
        payCode=req.POST['payCode']
        payInfo=req.POST['payInfo']
        paySum=req.POST['paySum']

        fp_pay.write(payCode)
        fp_pay.write('\n')
        fp_pay.write(payInfo)
        fp_pay.write('\n')
        fp_pay.write(paySum)
        fp_pay.write('\n')
    else:
        payCode=fp_pay.readline()
        payInfo=fp_pay.readline()
        paySum=fp_pay.readline()

    fp_taxi.close()
    fp_crime.close()
    fp_pay.close()

    '''safa하지 않을 경우(unsafe)에 딕셔너리에 추가하여 넘겨줘야함'''
    if flag_safe==0:
        data_dic['taxiNumber']=taxiNumber
        data_dic['taxiDriver']=taxiDriver
        data_dic['taxiGPS']=taxiGPS
        data_dic['taxiReportCode']=taxiReportCode
        data_dic['criminalCode']=criminalCode
        data_dic['criminalName']=criminalName
        data_dic['payCode']=payCode
        data_dic['payInfo']=payInfo
        data_dic['paySum']=paySum

        '''safe일 경우'''
    else:
        data_dic={}

    return render(req, 'blog/post_list.html',data_dic)

    #return render(req,'blog/post_list.html',{})
    #return render(req,'blog/post_list.html',{'taxiNumber':taxiNumber, 'taxiDriver':taxiDriver})
