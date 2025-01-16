# parport_triggers

## Setting Up

**Bionex:**
The parallel port cable should be attached to the first ("Digital I/O 1") slot in the back of the 8-slot Bionex and the trigger cable ("TRIGGER INPUT") should not be plugged in. 

**Biolab:**
The Biolab setting for Trigger Modes should be set to "OFF".

**Stimulus computer (linux machine):**
Make sure there's an actual parallel port card installed in the back of the computer tower.

Find the parallel port addess by typing `/dev/parport*` into the terminal (it should be something like /dev/parport0) and note this down.

Two commands need to be run on the terminal to allow communication with the parallel port:

The first command is:
```
sudo modprobe -r lp
```
This tells the linux machine to "learn" some type of linux kernel module to interact with the parallel port. Clearly not super clear on what exactly this does but apparently can be run from any working directory. The terminal will ask for the account password to make changes.

If you don't run this, you might get the following error:
```
OSError: [Errno 6] No such device or address
```

The second command is:
```
sudo chmod 777 /dev/parport0
```
replacing /dev/parport0 with the relevant port address to give the computer permission to access the port.

Otherwise you might run into this error:
```
[Errno 13] Permission denied
```

## Instructions for use of the Triggerer Class
Note: see the docstrings in the script for more detailed information.

First initialize an instance of the Triggerer class in the script you will be running your experiment on:
```
my_triggerer = Triggerer(0)
```
Replacing the 0 with the actual parallel port address number.

Then you need to set the trigger labels with whatever you want your flags to be:
```
my_triggerer.set_trigger_labels(['flag1', 'flag2, 'flag3'])
```
Note that you can have up to 127 different flag labels (but no more). 

In order for the triggers to be reported by Mindware with the names you want ('flag1', 'flag2') instead of random numbers, you need to upload a .txt file into the Biolab "Synchronous Events (Digital I/O 1)" tab. Event Mode should be set to Summary. 

To autogenerate the .txt file that you need to upload to BioLab, you can open an instance of ipython in a terminal window (make sure you're CD'ed into the directory with the triggerer.py script) and use the following commands:
```
# repeat the creation of the class instance and setting of labels just as you do in your experiment script above
my_triggerer = Triggerer(0)
my_triggerer.set_trigger_labels(['flag1', 'flag2'])

# generate the txt file
my_triggerer.create_txt_file('my_filename')
```
This will save the txt file into your current working directory. You can then take this file and upload it to BioLab on the computer you will be using for physio data acquisition.

Once you've done this and uploaded the txt file to Biolab, you should be ready to send triggers and receive them in the Biolab acquisition window. Any time in the script that you want to send a trigger use:
```
my_triggerer.send_trigger('flag1')
```
inputting the appropriate flag name.

Importantly, you have to remember to manually start the physio data acquisition by clicking on the "Start" button in the top left corner of the Biolab window as **the acquisition will not be triggered to start automatically**!

Any questions or problems contact Anita Restrepo (ar277@uchicago.edu). 

Happy Triggering!
