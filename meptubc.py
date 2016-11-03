from os import system, listdir, path, stat
def pause():
    input(" Press Enter to exit . . .")
    exit()
    
print("")
if path.isfile("%s\\conf.ini" % path.dirname(path.abspath(__file__))):
    conf = open("%s\\conf.ini" % path.dirname(path.abspath(__file__)), "r")
    conf_read = conf.read().split("\n")
    

    if len(conf_read) < 2 or not conf_read[0] or not conf_read[1]:
        print(" There was an unexpected ERROR during the setup, please run setup.py again!")
        pause()
        
    else:
        path_to_filefolder	= conf_read[0]
        path_to_pscp		= conf_read[1]
    
        if "pscp.exe" in listdir(path_to_pscp):

            print(" Windows scp-script for unixpool@tu-berlin\n")
            print(" Enter Filename\n  Example PA01.py\n")
            obj = input(" >: ")
            print("\n Enter Account\n  Example co1-042\n")
            acc = input(" >: ")
            
            print("\n        After the file was uploaded,\n        the file can be found in your accounts home-folder.\n")

            if obj in listdir(path_to_filefolder):
                system("%spscp.exe %s%s %s@unixpool.math.tu-berlin.de:." % (path_to_pscp,path_to_filefolder,obj,acc))
            
            else:
                print(" ERROR") 
                print(" %s was not found at %s!" % (obj,path_to_filefolder))
                print(" If you want an other filefolder rerun setup.py")
                pause()
                
        else:
            print(" ERROR")
            print(" pscp.exe was not found in %s !" % path_to_pscp)
            print(" Either move pscp.exe to %s or run setup.py again!" % path_to_pscp)
            pause()
            
else:
    print(" Please run setup.py")
    pause()
    

#Made by Patrick A.
#If you have questions, suggestions or found typos send me an email:
#   meptubc@gmail.com