with open("test2.txt","ab") as f2:
  with open("test3.txt","ab") as f3:
    f3.write(f2.read())
