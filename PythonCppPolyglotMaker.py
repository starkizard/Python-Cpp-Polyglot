import sys;if0,end,pyc= "#if 0\n", "#endif\n",'""" "'
try: ofname,py,cpp = sys.argv[1:4]
except: print("Input Error\nUsage:\npython3 "+sys.argv[0]+" <Output file> <Input py file> <Input cpp file>");exit(1)
with open(ofname,"w") as of, open(py,"r") as if1, open(cpp,"r") as if2:of.writelines([if0]+if1.readlines()+["\n"+end+if0+pyc+"\n"+end]+if2.readlines()+["\n"+if0+pyc[::-1]+"\n"+end]);print("Success! "+ str(of.tell()) +" bytes written to "+ofname)