MEPTUBC (More Easy Pscp script for TU Berlin CoMa)
MEPTUBC is a script that will make all the inputs for you !AFTER! you replaced the neccessary filepaths.

Since windows user don't have a built-in-function for SSH and SCP,
I wanted to help all those of you, whom don't want to fiddle around with the windows commando line to upload a file.

Step 1
Download PSCP
Either google PSCP / Putty SCP or visit http://www.chiark.greenend.org.uk/~sgtatham/putty/download.html
This programm is neccessary for everything else.
Save it to a folder and keep the path to it in mind.

You can actually use PSCP by yourself via console and I would recommend you to try it, the documentation is decent.


Step 2
Replace "Replace" with the describe folder path. [Warning the path should always end with an \\]
The first Replace (in line 9) should be replaced with the (full)path to the folder containing the PA's
and should look something like "C:\users\...\Coma_PA\".

The second Replace (in line 14) should be replaced with the (full)path to the folder containing the pscp.exe


Step 3
Run the .bat


For questions or suggestions sent an e-mail to
aabraham.patrick at googlemail.com