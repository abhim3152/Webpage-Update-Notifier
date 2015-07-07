import urllib2
import os,sys

i=1
f=open('/srv/http/link.txt','r')
url=f.read()

#try:
while 1:
	
	pagei=urllib2.urlopen(urllib2.Request(url)).read()
	os.system('sleep 1')
	
	pager=urllib2.urlopen(urllib2.Request(url)).read()
	comm="notify-send 'WEBPAGE UPDATED ("+str(i)+")'"
	if pagei != pager:
		os.system(comm)
		i=i+1
	#elif KeyboardInterrupt:
	#	sys.exit()
#except :
#	os.system("notif-send 'error'")
#	print "error"
