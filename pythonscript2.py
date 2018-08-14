def helloWorld():
	
	f= open("log.txt", "a+")
	for i in range(5):
		f.write("Hello my friends")
	f.close()


