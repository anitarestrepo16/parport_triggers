# parport_triggers

## Instructions for use

Can find parallel port address with `/dev/parport*`

On this system, this should give you /dev/parport3, in which case in Python, 

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
into terminal


happy triggering!
