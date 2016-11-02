from os import system, listdir, path, stat

if path.isfile(path.dirname(path.abspath(__file__))+"\\conf.ini"):
	conf = open(path.dirname(path.abspath(__file__))+"\\conf.ini", "r")
	conf_read = conf.read().split("\n")

	if len(conf_read) < 2:
		input("There was an unexpected ERROR during the setup, please run setup.py again!")
		system("pause")
		
	else:
		path_to_filefolder	= conf_read[0]
		path_to_pscp		= conf_read[1]
	
		if "pscp.exe" in listdir(path_to_pscp):

			print("Windows scp-script for unixpool@tu-berlin")
			print("Enter Filename\n  Example PA01.py")
			obj = input()
			print("Enter Account\n  Example co1-042")
			acc = input()

			if obj in listdir(path_to_filefolder):
				system("%spscp.exe %s%s %s@unixpool.math.tu-berlin.de:." %(path_to_pscp,path_to_filefolder,obj,acc))
			
			else:
				print(obj + " was not found at " + path_to_filefolder + "!")
				print("If you want an other filefolder rerun setup.py")
				system("pause")
				
		else:
			print("pscp.exe was not found in " + path_to_pscp + "!")
			print("Either move pscp.exe to " + path_to_pscp + " or run setup.py again!")
			system("pause")
			
else:
	print("Please run setup.py")
	system("pause")