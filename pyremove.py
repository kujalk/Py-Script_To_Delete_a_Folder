"""
This script is used to remove certain folder structure
Developer - kujalk
Date - 29/12/2017
Version - 1
"""

import os
import time
import shutil

#Function for log time
def timestamp (message):
	#a-> append, w-> write, r->read
	f=open(log,'a')
	f.write('\n' + time.strftime('%d/%m/%Y %H:%M:%S')+" <<Info>> : " + message)
	f.close()
	
	
reply = input ("\nDid you use your Privilege Account to run this script\n  If yes press 'y' if not press 'n'\n : ")

if (reply=="y" or reply=="Y"):
	log = input ("Provide a location for log Eg - [D:\Log.txt] : ")
	timestamp ("Starting Work")
	
	
	path="E:\Training\Files"
	os.chdir(path)
	
	
	#Loading the user profiles
	profiles = next(os.walk('.'))[1]
	
	for userprofile in profiles:
		#Moving to user profile
		path1=path+"/"+userprofile
		os.chdir(path1)
		
		
		if (os.path.exists("Software/Purpose")):
			#Moving inside the user profile
			os.chdir("Software/Purpose")
			
			
			#Getting subdirectories under the current user profile
			subfol = next(os.walk('.'))[1]
			tot=len(subfol)
			
			if (tot ==0):
				timestamp ("No any subfolders under for "+userprofile)
				
			else:
				for subf in subfol:
					path2=path1+"/Software/Purpose/"+subf
					os.chdir(path2)
					
					
					if(os.path.exists("cache")):
						#Remove folder
						shutil.rmtree("cache")
						timestamp ("cache folder is removed from "+userprofile+"/Software/Purpose/"+subf)
							
					else:
						timestamp ("cache folder is not found for "+userprofile+"/Software/Purpose/"+subf)
					
			
		else:
			timestamp ("Software/Purpose is not available for "+userprofile+" profile")
			
	
	os.chdir(path)
	timestamp ("Everything Finished")
	
	
else:
	print ("Please right click the powershell windows and run as different user \n Terminating !!!!")
	quit()