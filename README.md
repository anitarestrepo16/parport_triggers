# parport_triggers

## Instructions for use

Note: The parallel port cable should be attached to the first ("Digital I/O 1") slot in the back of the 8-slot Bionex and the trigger cable ("TRIGGER INPUT") should not be plugged in. The Biolab setting for Trigger Modes should be set to "OFF".

Can find parallel port address with `/dev/parport*`

On the linux computer in the eyetracking room, this should give you /dev/parport3 (because the parallel port is installed in the third PCI slot), in which case in Python, 

```
from parallel.parallelppdev import Parallel
p = Parallel(3)
```
or 
```
from psychopy.parallel import ParallelPort
p = ParallelPort(3)
```

Then you can set the pins as in the pyparallel documentation.

For instance
```
p.setData(255)
```
will set all the pins to high and 
```
p.setData(0)
```
will set them to low.

If you get this error
```
OSError: [Errno 6] No such device or address
```
then exit python and type
```
sudo modprobe -r lp
```
into terminal. This tells the linux machine to "learn" some type of linux kernel module to interact with the parallel port. Clearly not super clear on what exactly this does but apparently can be run from any working directory.

If get the error
```
[Errno 13] Permission denied
```
when trying to set `p = ParallelPort(address)` need to exit iPython and run the following command to give permissions to the port:  
```
sudo chmod 777 /dev/parport3
```
replacing /dev/parport3 with the relevant port address. 

happy triggering!
