def internet_checker():
	import urllib.request
	try:
		urllib.request.urlopen('http://google.com') 
		return True
	except:
		return False
	


def speed_warning():
	import time
	print("Functions requiring internet connection may take a while. Please do not interact with your device until the process is finished.")
	time.sleep(4)
	print("Starting in:")
	print("3")
	time.sleep(0.5)
	print("2")
	time.sleep(0.5)
	print("1")
	time.sleep(0.5)
	
	

#def translate():
