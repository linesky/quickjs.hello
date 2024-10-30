code="class "
last=0
ttrue=True
files=input("file data name? ")
last=files.find(".")
if last<0:
    last=len(files)+1
code="# class \nclass "+files[:last]+":\n    def _init_(self):\n        self.value=0\n"
try:
    f1=open(files,"r")
    code=f1.read()
    f1.close()
except:
    aa=0
while ttrue:
    lines=input("functions separete by ,? ")
    lines=lines.strip()
    if lines=="":
        ttrue=False
    else:
        sp=lines.split(",")
        s1=""
        m=0
        for c in range(len(sp)):
            
            
            s1="    #"+sp[c]+"\n"
            s4=s1+"    def "+sp[c]+"(self):\n        self.value=0\n"
            
            code=code+s4

        print(code)
try:
    f1=open(files,"w")
    f1.write(code)
    f1.close()
except:
    print("error on write file")
            
            
        
         
    
