from django.http import HttpResponse, JsonResponse    #통신위함
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
import shutil
import os



@csrf_exempt

#글롭로벌 변변숨변수만변수만들변수만들엇변수만들어서 true일일때 값 본보냊보내죽보내주기

def upload(req):

 #   flag_safe=0
    '''safe한 경우 처리 플래그'''
    if 'safe' in req.POST:
        flag_safe=1




    else: #'refresh' in req.POST:
        flag_safe=0


#    if req.method == 'POST':
#    for afile in req.FILES.getlist('files'):
#        File(file=afile, files=test).save()
    '''safe한 경우에는 기본이미지 띄우고 변수안넘겨줌'''
    if flag_safe ==1:
        #print("hi")
        '''temp로 평소에 띄울 사진 유지시켜놔야됨'''
        file_loc="C:/Users/jineok/Desktop/djangogirls/revised_server/blog/static/image/"
        src=file_loc+'inner_temp.jpg'
        dest=file_loc+'inner.jpg'
        shutil.copy(src,dest)
        src=file_loc+'crime_temp.jpg'
        dest=file_loc+'crime.jpg'
        shutil.copy(src,dest)

        '''앱에서 받은 정보 초기화'''
        file_loc= 'blog/static/info'
        fp_taxi = open('%s/%s' % (file_loc,'taxi_info.txt') , 'w+',encoding='UTF8')
        fp_crime = open('%s/%s' % (file_loc,'crime_info.txt') , 'w+',encoding='UTF8')
        fp_pay = open('%s/%s' % (file_loc,'pay_info.txt') , 'w+',encoding='UTF8')

        #정보 초기화
        fp_taxi.write(' ')
        fp_crime.write(' ')
        fp_pay.write(' ')

        fp_taxi.close()
        fp_crime.close()
        fp_pay.close()

        f = open('%s/%s' % (file_loc,'safe_info.txt') , 'w',encoding='UTF8')
        data = "safe"
        f.write(data)
        f.close

        return render(req, 'blog/post_list.html',{})

        '''refresh하면 정상적으로 작동'''
    else:
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
            elif filename == 'criminalPhoto.jpg':
                fp = open('%s/%s' % (file_loc, 'crime.jpg') , 'wb')

            for chunk in file.chunks():
                fp.write(chunk)

            fp.close()

        file_loc='blog/static/info'
        fp_taxi = open('%s/%s' % (file_loc,'taxi_info.txt') , 'r+',encoding='UTF8')
        fp_crime = open('%s/%s' % (file_loc,'crime_info.txt') , 'r+',encoding='UTF8')
        fp_pay = open('%s/%s' % (file_loc,'pay_info.txt') , 'r+',encoding='UTF8')
        # w+로 읽기전에 열면 파일 내용 지워 버림. r+가 적당. 모두 파일 스트림 시작에 위치
        f = open('%s/%s' % (file_loc,'safe_info.txt') , 'w',encoding='UTF8')
        data = ""
        f.write(data)
        f.close

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
            criminalBirth=req.POST['criminalBirth']
            criminalGender=req.POST['criminalGender']
            criminalHeight=req.POST['criminalHeight']
            criminalAddress=req.POST['criminalAddress']
            fp_crime.write(criminalCode)
            fp_crime.write('\n')
            fp_crime.write(criminalName)
            fp_crime.write('\n')
            fp_crime.write(criminalBirth)
            fp_crime.write('\n')
            fp_crime.write(criminalGender)
            fp_crime.write('\n')
            fp_crime.write(criminalHeight)
            fp_crime.write('\n')
            fp_crime.write(criminalAddress)
            fp_crime.write('\n')
        else:
            criminalCode=fp_crime.readline()
            criminalName=fp_crime.readline()
            criminalBirth=fp_crime.readline()
            criminalGender=fp_crime.readline()
            criminalHeight=fp_crime.readline()
            criminalAddress=fp_crime.readline()
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

        data_dic['taxiNumber']=taxiNumber
        data_dic['taxiDriver']=taxiDriver
        data_dic['taxiGPS']=taxiGPS
        data_dic['taxiReportCode']=taxiReportCode
        data_dic['criminalCode']=criminalCode
        data_dic['criminalName']=criminalName
        data_dic['criminalBirth']=criminalBirth
        data_dic['criminalGender']=criminalGender
        data_dic['criminalHeight']=criminalHeight
        data_dic['criminalAddress']=criminalAddress
        data_dic['payCode']=payCode
        data_dic['payInfo']=payInfo
        data_dic['paySum']=paySum


        return render(req, 'blog/post_list.html',data_dic)
