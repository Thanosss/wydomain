'''
Mst=>Exploit=>fuck=>Class
'''
from   socket    import *
from   MstColor  import *
from   os        import listdir,getcwd
import urllib
import urllib2
import cookielib
import re,sys,hashlib
import MultipartPostHandler


class fuck:
    ''' all plugins function :)'''
    def checkport(self,host,port):
        '''check host's port !open?::return 1 or 0'''
        try:
            s=socket(AF_INET,SOCK_STREAM)
            s.settimeout(5)
            s.connect((host,int(port)))
            s.close()
            return 1
        except:
            return 0
    def urlget(self,url):
        '''url open=>get'''
        return urllib.urlopen(url)
    
    def urlpost(self,url,value):
        '''url post'''
        data    = urllib.urlencode(value)
        headers = { 'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11' }
        res     = urllib2.Request(url,data,headers)
        try:
            ok  = urllib2.urlopen(res)
            return ok
        except:
            return 0
    def urlupload(self,url,value):
        '''url upload file'''
        cookies = cookielib.CookieJar()
        opener  = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookies),
                                MultipartPostHandler.MultipartPostHandler)
        opener.open(url, value)
    def urltoip(self,url):
        '''url to ip'''
        return gethostbyname(url)

    def writelog(self,logname,log):
        '''write log to file'''
        fp = open('output/%s.log'%logname,'a')
        fp.write(log)
        fp.close()
    
    def find(self,r,t):
        '''re find'''
        return re.findall(r,t)
    
    def topayload(self,PAYLOAD,arr):
        '''load payload'''
        if PAYLOAD.upper() != "FALSE" and len(PAYLOAD)>0:
            color.cprint("[*] Start Payload ..",YELLOW)
            code=open("plugins/payload/"+PAYLOAD+".py").read()
            exec(code)
            exec("global mstpayload")
            payload=mstpayload(arr)
            code=open("libs/MstPayload.py").read()
            exec(code)
            payload.start()


if __name__ == '__main__':
    print __doc__
