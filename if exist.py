import os
if os.path.exists("welcome.mp3"):
  os.remove("welcome.mp3")
else:
  print("The file does not exist")
