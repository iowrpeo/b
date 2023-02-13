with open("test2.txt","ab") as f2:
  with open("test3.txt","ab") as f3:
    for i in f2.readlines():
      f2.write(i)
