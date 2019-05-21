#!/usr/bin/python
#-*- coding:UTF-8 -*-

from collections import OrderedDict
from multiprocessing import Pool
import socket
import time
import sys  

#reload(sys)  
#sys.setdefaultencoding("utf-8")

target_host = "140.116.245.151"
target_port = 9998

def seg(sentence):
    # create socket
    # AF_INET 代表使用標準 IPv4 位址或主機名稱
    # SOCK_STREAM 代表這會是一個 TCP client
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # client 建立連線
    client.connect((target_host, target_port))
    # 傳送資料給 target
    data = "seg@@" + sentence
    client.send(data.encode("utf-8"))
    
    # 回收結果信息
    data = bytes()
    while True:
        request = client.recv(8)
        if request:
            data += request
            begin = time.time()
        else:
            break

    WSResult = []
    response = data
    if(response is not None or response != ''):
        response = response.decode('utf-8').split()
        for resp in response:
            resp = resp.strip()
            resp = resp[0:len(resp)-1]
            temp = resp.split('(')
            word = temp[0]
            pos = temp[1]
            WSResult.append((word,pos))

    return WSResult

'''
sentence = input("Input sentence:")
result = seg(sentence)
print(result)
'''

fullstring = []

catbuffer = ""
fulltmp = ""

i=0

def segmentfull(sentence):
	global fulltmp  #為了要在function裡面使用外面宣告的參數，在function內要用global宣告
	for i in range(len(sentence)):
		#fulltmp += sentence[i][0]
		print("current is:" + fulltmp + "\n")
		if sentence[i][1] == "PERIODCATEGORY":
			fullstring.append(fulltmp)
			fulltmp = ""
		elif sentence[i][1] == "COMMACATEGORY":
			fullstring.append(fulltmp)
			fulltmp = ""
		elif sentence[i][1] == "QUESTIONCATEGORY":
			fullstring.append(fulltmp)
			fulltmp = ""
		else:
			fulltmp += sentence[i][0]
			if i == (len(sentence) - 1):
				fullstring.append(fulltmp)
		
		
	
def getresult(result):
	print("The result is:\n")
	print(result)
	segmentfull(result)
	print("Full Event:")
	print(fullstring)
def deleteresult():
	Role = ""
	Time = ""
	Object = ""
	Place = ""
	fullstring = ""
	simplestring = ""

check = 1
while check==1:			
	sentence = input("Input sentence:")
	if(sentence == "結束"):
		deleteresult()
		break
	else:
		result = seg(sentence)
		getresult(result)
		deleteresult()	
'''
print(result)
print("Name:")
segment(result,"Nb",Name)
print(Name)
print("Time:")
segment(result,"Nd",Time)
print(Time)
print("Object:")
segment(result,"Na",Object)
print(Object)
print("Place:")
segment(result,"Nc",Place)
print(Place)

segmentfull(result)
print("Full Event:")
print(fullstring)
print("Simple Event:")
print(simplestring)
'''
'''
d = {'Nh':[],'Nc':[],'VCL':[],'simple_event':[],'complete_event':[]}

for i in range(len(result)):
	if result[i][1] == "Nh":
		d['Nh'].append(result[i][0])
	elif result[i][1] == "Nc":
		d['Nc'].append(result[i][0])
	elif result[i][1] == "VCL":
		d['VCL'].append(result[i][0])

Nh = d.get('Nh')	#從d中提取key為Nh的value
Nc = d.get('Nc')	#從d中提取key為Nc的value
VCL = d.get('VCL')	#從d中提取key為VCL的value

x = "{"				#x is the output string,the operation below is to fit the format

x = x + 'Nh:{'
for i in range(len(Nh)):
	x = x + "'" + Nh[i] + "'"
	if i+1 < len(Nh):
		x = x + ","
x = x + '}'

x = x + 'Nc:{'
for i in range(len(Nc)):
	x = x + "'" + Nc[i] + "'"
	if i+1 < len(Nc):
		x = x + ","
x = x + '}'

x = x + 'VCL:{'
for i in range(len(VCL)):
	x = x + "'" + VCL[i] + "'"
	if i+1 < len(VCL):
		x = x + ","
x = x + '}'

x = x + '}'

#for i in range(len(Nh)):
#	Nh[i]=unicode.encode(Nh[i],'big5')
#for i in range(len(Nc)):
#	Nc[i]=unicode.encode(Nc[i],'big5')
#for i in range(len(VCL)):
#	VCL[i]=unicode.encode(VCL[i],'big5')

#print (x)
'''



