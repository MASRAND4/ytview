import webbrowser,time
url = input ("link :")
duration = input("enter duration : ")
for i in range (15):
  webbrowser.open_new(url)
  time.sleep(int(duration))
#https://youtu.be/NAWNtWRwqv8