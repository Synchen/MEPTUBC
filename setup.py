from os import path

conf = open(path.dirname(path.abspath(__file__))+"\\conf.ini", "w")

print("\n Before continuing with the setup!"," Please make sure you downloaded Putty scp [pscp.exe]"," Either google for Putty/Pscp or visit","   http://www.chiark.greenend.org.uk/~sgtatham/putty/download.html\n", sep="\n")
print(" Please enter path to filefolder containing the files to upload!","   Example: C:\\Users\\Nyancat\\Documents\\Uploadable",sep ="\n")
ptf = input(" >: ")
while not path.isdir(ptf):
    print(" %s is not a correct folder!"% ptf)
    print(" Please input correct folder!")
    ptf = input(" >: ")
if not ptf.endswith("\\"):
    ptf = ptf + "\\"

    
print(" Please enter path to filefolder containing pscp.exe","   Example: C:\\Users\\Nyancat\\Putty\\",sep="\n")
ptp = input(" >: ")
while not path.isdir(ptp):
    print(" %s is not a correct folder!"% ptp)
    print(" Please input correct folder!")
    ptp = input(" >: ")
if not ptp.endswith("\\"):
    ptp = ptp + "\\"
    
print(ptf,ptp, sep = "\n", end = "", file = conf)

#Made by Patrick A.
#If you have questions, suggestions or found typos send me an email:
#   meptubc@gmail.com