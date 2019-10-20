def scan():
    try:
        can = input('请输出IP的前三个段和.例: <192.168.1.> :')
        absq = open('ip.txt','w')
        for i in range(199,250):
            absq.write(can+(str(i))+"\n")
    except:
            print('[-]生成失败请检查1.txt文件是否存在')
            
scan()
print('[+]ok')   
#接下来获取到ip.txt的内容开始查端口
import socket
socket.setdefaulttimeout(1)

print('[*]finding')
def find():
    n=open('ip.txt','r')
    for g in n.readlines():
        gv=g.strip('\r').strip('\n')
        s=socket.socket()
        try:
            #端口在这设置 
            s.connect((gv,3389))
            print('this netword open port 3389:'+gv)
        except:
         pass



find()
print('[*]end')




