# Why is the server so slow?

## Running out of CPU, RAM and DISK I/O

### System Load

```
$ uptime
13:35:03 up 103 days, 8 min, 5 users, load average: 2.03, 20.17, 15.09
```

The three numbers after load average—2.03, 20.17, and 15.09—represent the
1-, 5-, and 15-minute load averages on the machine, respectively. A system
load average is equal to the average number of processes in a runnable or
uninterruptible state. Runnable processes are either currently using the
CPU or waiting to do so, and uninterruptible processes are waiting for I/O.

```
$ uptime
05:11:52 up 20 days, 55 min, 2 users, load average: 17.29, 0.12, 0.01
```

In this case, both the 5- and 15-minute load averages are low, but the
1-minute load average is high, so I know that this spike in load is relatively
recent. Often in this circumstance I will run uptime multiple times in a row
(or use a tool like top, which I will discuss in a moment) to see whether the
load is continuing to climb or is on its way back down.

What is a high load average?

We need to dive deeper to see whats really happening. Sometimes programs are just running and not finished yet.

### `top` Command

```
$ top

top - 00:40:08 up 5 days, 12:01,  0 users,  load average: 0.09, 0.06, 0.02
Tasks:  25 total,   1 running,  24 sleeping,   0 stopped,   0 zombie
%Cpu(s):  0.2 us,  0.7 sy,  0.0 ni, 99.1 id,  0.0 wa,  0.0 hi,  0.0 si,  0.0 st
MiB Mem :   6705.1 total,   1677.3 free,   1279.0 used,   3748.7 buff/cache
MiB Swap:   4096.0 total,   4096.0 free,      0.0 used.   4776.3 avail Mem 

  PID USER      PR  NI    VIRT    RES    SHR S  %CPU  %MEM     TIME+ COMMAND                                                                                                                                        
  269 vscode    20   0   11.1g 270720  40352 S   0.3   3.9  54:09.45 node                                                                                                                                           
59143 vscode    20   0  679820  37628  29036 S   0.3   0.5   0:06.13 node                                                                                                                                           
    1 root      20   0     996      4      0 S   0.0   0.0   0:15.35 docker-init                                                                                                                                    
    9 root      20   0    2612   1612   1516 S   0.0   0.0   1:58.79 sh                                                                                                                                             
   11 root      20   0    2612    596    528 S   0.0   0.0   0:00.01 sh                                                                                                                                             
   19 vscode    20   0    2612   1660   1512 S   0.0   0.0   0:03.89 sh                                                                                                                                             
   43 root      20   0    2612    600    532 S   0.0   0.0   0:00.02 sh                                                                                                                                             
   57 vscode    20   0  611944  31028  25588 S   0.0   0.5   0:01.40 node                                                                                                                                           
  137 vscode    20   0    2612    596    532 S   0.0   0.0   0:00.00 sh 

```

```
NAME
     top -- display sorted information about processes

SYNOPSIS
     top [-a | -d | -e | -c mode]
         [-F | -f]
         [-h]
         [-i interval]
         [-l samples]
         [-ncols columns]
         [-o key | -O skey]
         [-R | -r]
         [-S]
         [-s delay-secs]
         [-n nprocs]
         [-stats keys]
         [-pid processid]
         [-user username]
         [-U username]
         [-u]

DESCRIPTION
     The top program periodically displays a sorted list of system processes.
     The default sorting key is pid, but other keys can be used instead.  Var-
     ious output options are available.

OPTIONS
     Command line option specifications are processed from left to right.
     Options can be specified more than once.  If conflicting options are
     specified, later specifications override earlier ones.  This makes it
     viable to create a shell alias for top with preferred defaults specified,
     then override those preferred defaults as desired on the command line.

     -a      Equivalent to -c a.

     -c mode
             Set event counting mode to mode.  The supported modes are

             a       Accumulative mode.  Count events cumulatively, starting
                     at the launch of top.  Calculate CPU usage and CPU time
                     since the launch of top.

             d       Delta mode.  Count events relative to the previous sam-
                     ple.  Calculate CPU usage since the previous sample.
                     This mode by default disables the memory object map
                     reporting.  The memory object map reporting may be re-
                     enabled with the -r option or the interactive r command.

             e       Absolute mode.  Count events using absolute counters.

             n       Non-event mode (default).  Calculate CPU usage since the
                     previous sample.

     -d      Equivalent to -c d.

     -e      Equivalent to -c e.

     -F      Do not calculate statistics on shared libraries, also known as
             frameworks.

     -f      Calculate statistics on shared libraries, also known as frame-
             works (default).

     -h      Print command line usage information and exit.

     -i interval
             Update framework (-f) info every interval samples; see the
             PERFORMANCE/ACCURACY TRADEOFF section for more details.

     -l samples
             Use logging mode and display samples samples, even if standard
             output is a terminal.  0 is treated as infinity.  Rather than
             redisplaying, output is periodically printed in raw form.  Note
             that the first sample displayed will have an invalid %CPU dis-
             played for each process, as it is calculated using the delta
             between samples.

     -ncols columns
             Display columns when using logging mode.  The default is infi-
             nite.  The number must be > 0 or an error will occur.

     -n nprocs
             Only display up to nprocs processes.

     -O skey
             Use skey as a secondary key when ordering the process display.
             See -o for key names (pid is the default).

     -o key  Order the process display by sorting on key in descending order.
             A + or - can be prefixed to the key name to specify ascending or
             descending order, respectively.  The supported keys are:

             pid     Process ID


```

With `top` you want to examine what resources are deminished.

* CPU
* RAM
* Disk I/O

#### CPU Load

We get some extra information related to the CPUs

```
Cpu(s): 11.4%us, 29.6%sy, 0.0%ni, 58.3%id, 0.7%wa, 0.0%hi, 0.0%si, 0.0%st
```

```
us: user CPU time
This is the percentage of CPU time spent running users’ processes that
aren’t niced. (Nicing is a process that allows you to change its priority
in relation to other processes.)

sy: system CPU time
This is the percentage of CPU time spent running the kernel and kernel processes.

ni: nice CPU time
If you have user processes that have been niced, this metric will tell you
the percentage of CPU time spent running them.

id: CPU idle time
This is one of the metrics that you want to be high. It represents the
percentage of CPU time that is spent idle. If you have a sluggish system
but this number is high, you know the cause isn’t high CPU load.

wa: I/O wait
This number represents the percentage of CPU time that is spent waiting for I/O. It is a particularly valuable metric when you are tracking
down the cause of a sluggish system, because if this value is low, you
can pretty safely rule out disk or network I/O as the cause.

hi: hardware interrupts
This is the percentage of CPU time spent servicing hardware interrupts.

si: software interrupts
This is the percentage of CPU time spent servicing software interrupts.

st: steal time
If you are running virtual machines, this metric will tell you the percentage of CPU time that was stolen from you for other tasks.
```

In the previous example, you can see that the system is over 50% idle,
which matches a load of 1.70 on a four-CPU system. When you diagnose
a slow system, one of the fi rst values you should look at is I/O wait so
you can rule out disk I/O. If I/O wait is low, then you can look at the idle
percentage. If I/O wait is high, then the next step is to diagnose what is
causing high disk I/O, which I will cover momentarily. If I/O wait and idle
times are low, then you will likely see a high user time percentage, so you
must diagnose what is causing high user time. If the I/O wait is low and the
idle percentage is high, you then know any sluggishness is not because of
CPU resources, and you will have to start troubleshooting elsewhere. This
might mean looking for network problems, or in the case of a web server,
looking at slow queries to MySQL, for instance.

```
 PID USER PR NI VIRT RES SHR S %CPU %MEM TIME+ COMMAND
 9463 mysql 16 0 686m 111m 3328 S 53 5.5 569:17.64 mysqld
18749 nagios 1 0 140m 134m 1868 S 12 6.6 1345:01 nagios2db_status
24636 nagios 17 0 34660 10m 712 S 8 0.5 1195:15 nagios
22442 nagios 24 0 6048 2024 1452 S 8 0.1 0:00.04 check_time.pl 
```

If you see high user CPU time but low I/O wait times, you
simply need to identify which processes on the system are consuming the
most CPU. By default, top will sort all of the processes by their CPU usage

In this example, the mysqld process is consuming 53% of the CPU and the
nagios2db_status process is consuming 12%. Note that this is the percentage
of a single CPU, so if you have a four-CPU machine, you could possibly
see more than one process consuming 99% CPU

#### Out of Memory Issues

`$ free` or `top`

```
Mem: 1024176k total, 997408k used, 26768k free, 85520k buffers
Swap: 1004052k total, 4360k used, 999692k free, 286040k cached
```

```
MiB Mem :   6705.1 total,   1558.4 free,   1292.0 used,   3854.6 buff/cache
MiB Swap:   4096.0 total,   4096.0 free,      0.0 used.   4764.7 avail Mem 
```

To find out how much RAM is really being used by processes, you must
subtract the file cache from the used RAM. In the example code you just looked at, out of the 997,408k RAM that is used, 286,040k is being used by the Linux file cache, so that means that only 711,368k is actually being
used.

```
 PID USER PR NI VIRT RES SHR S %CPU %MEM TIME+ COMMAND
18749 nagios 16 0 140m 134m 1868 S 12 6.6 1345:01 nagios2db_status
 9463 mysql 16 0 686m 111m 3328 S 53 5.5 569:17 mysqld
24636 nagios 17 0 34660 10m 712 S 8 0.5 1195:15 nagios
22442 nagios 24 0 6048 2024 1452 S 8 0.1 0:00.04 check_time.pl 
```

Look at the %MEM column and see if the top processes are consuming a
majority of the RAM. If you do fi nd the processes that are causing high
RAM usage, you can decide to kill them, or, depending on the program,
you might need to perform specifi c troubleshooting to fi nd out what is
making that process use so much RAM.

The Linux kernel also has an out-of-memory (OOM) killer that can kick
in if the system runs dangerously low on RAM. When a system is almost
out of RAM, the OOM killer will start killing processes. In some cases this
might be the process that is consuming all of the RAM, but this isn’t guaranteed. It’s possible the OOM killer could end up killing programs like sshd or other processes instead of the real culprit. In many cases, the system is
unstable enough after one of these events that you fi nd you have to reboot
it to ensure that all of the system processes are running. If the OOM killer
does kick in, you will see lines like the following in your `/var/log/syslog`

```
1228419127.32453_1704.hostname:2,S:Out of Memory: Killed process 21389 (java).
1228419127.32453_1710.hostname:2,S:Out of Memory: Killed process 21389 (java).
```


### High I/O Wait

When you see high I/O wait, one of the fi rst things you should check is
whether the machine is using a lot of swap. Since a hard drive is much
slower than RAM, when a system runs out of RAM and starts using swap,
the performance of almost any machine suffers.

### `iostat` Command

```

$ sudo iostat
Linux 4.19.121-linuxkit (440b23e5ad57)  02/10/2022      _x86_64_        (3 CPU)

avg-cpu:  %user   %nice %system %iowait  %steal   %idle
           0.29    0.00    0.56    0.01    0.00   99.14

Device             tps    kB_read/s    kB_wrtn/s    kB_dscd/s    kB_read    kB_wrtn    kB_dscd
vda               0.67         4.00         6.90         0.00    1907471    3291976          0

```

Output Definitions

**tps**
This lists the transfers per second to the device. “Transfers” is another
way to say I/O requests sent to the device.

**Blk_read/s**
This is the number of blocks read from the device per second.

**Blk_wrtn/s**
This is the number of blocks written to the device per second.

**Blk_read**
In this column is the total number of blocks read from the device.

**Blk_wrtn**
In this column is the total number of blocks written to the device.


When you have a system under heavy I/O load, the fi rst step is to look at
each of the partitions and identify which partition is getting the heaviest I/O load. Say, for instance, that you have a database server and the
database itself is stored on `/dev/sda3`. If you see that the bulk of the I/O
is coming from there, you have a good clue that the database is likely
consuming the I/O.


### `iotop` Command

```
$ sudo iotop
Total DISK READ: 189.52 K/s | Total DISK WRITE: 0.00 B/s
 TID PRIO USER DISK READ DISK WRITE SWAPIN IO> COMMAND
 8169 be/4 root 189.52 K/s 0.00 B/s 0.00 % 0.00 % rsync --server --se
 4243 be/4 kyle 0.00 B/s 3.79 K/s 0.00 % 0.00 % cli /usr/lib/gnome-
 4244 be/4 kyle 0.00 B/s 3.79 K/s 0.00 % 0.00 % cli /usr/lib/gnome-
 1 be/4 root 0.00 B/s 0.00 B/s 0.00 % 0.00 % init
```

In this case, you can see that there is an rsync process tying up your read I/O.

### View CPU Stats

By default sar outputs the CPU statistics for the current day

```
$ sar
Linux 2.6.24-22-server (kickseed) 01/07/2012
. . .
07:44:20 PM CPU %user %nice %system %iowait %steal %idle
07:45:01 PM all 0.00 0.00 0.54 0.51 0.00 98.95
07:55:01 PM all 0.54 0.00 1.66 1.26 0.00 96.54
08:05:01 PM all 0.20 0.00 0.72 1.08 0.00 98.00
08:15:01 PM all 0.49 0.00 1.12 0.62 0.00 97.77
08:25:01 PM all 0.49 0.00 2.15 1.21 0.00 96.16
08:35:01 PM all 0.22 0.00 0.98 0.58 0.00 98.23
08:45:01 PM all 0.23 0.00 0.75 0.54 0.00 98.47
08:55:01 PM all 0.20 0.00 0.78 0.50 0.00 98.52
09:01:18 PM all 0.19 0.00 0.72 0.37 0.00 98.71
09:05:01 PM all 0.24 0.00 1.10 0.54 0.00 98.12
Average: all 0.32 0.00 1.12 0.78 0.00 97.78
```

### View Memory

```
$ sar -r
Linux 2.6.24-22-server (kickseed) 01/07/2012
07:44:20 PM kbmemfree kbmemused %memused kbbuffers kbcached kbswpfree kbswpused %swpused kbswpcad
07:45:01 PM 322064 193384 37.52 16056 142900 88316 0 0.00 0
07:55:01 PM 318484 196964 38.21 17152 144672 88316 0 0.00 0
08:05:01 PM 318228 197220 38.26 17648 144700 88316 0 0.00 0
08:15:01 PM 297669 217780 42.25 18384 154408 88316 0 0.00 0
08:25:01 PM 284152 231296 44.87 20072 173724 88316 0 0.00 0
08:35:01 PM 283096 232352 45.08 20612 173756 88316 0 0.00 0
08:45:01 PM 283284 232164 45.04 21116 173780 88316 0 0.00 0
08:55:01 PM 282556 232892 45.18 21624 173804 88316 0 0.00 0
09:01:18 PM 276632 238816 46.33 21964 173896 88316 0 0.00 0
09:05:01 PM 281876 233572 45.31 22188 173900 88316 0 0.00 0
Average: 294804 220644 42.81 19682 162954 88316 0 0.00 0
```

Here you can see how much free and used memory you have as well as
view statistics about swap and the fi le cache similar to what you would
see in either `top` or `free` output. The difference here is that you can go
back in time.


### Disk Statistics

```
$ sar -b
Linux 2.6.24-22-server (kickseed) 01/07/2012
07:44:20 PM tps rtps wtps bread/s bwrtn/s
07:45:01 PM 8.03 0.00 8.03 0.00 106.61
07:55:01 PM 8.78 0.14 8.64 3.35 127.59
08:05:01 PM 7.16 0.00 7.16 0.00 61.14
08:15:01 PM 8.17 0.14 8.03 5.82 139.02
08:25:01 PM 9.50 0.06 9.44 4.09 212.62
08:35:01 PM 8.27 0.00 8.27 0.01 74.66
08:45:01 PM 8.04 0.00 8.04 0.00 71.51
08:55:01 PM 7.64 0.00 7.64 0.00 66.46
09:01:18 PM 7.11 0.00 7.11 0.36 63.73
09:05:01 PM 7.61 0.00 7.61 0.00 72.11
Average: 8.11 0.04 8.06 1.67 102.52
```

Here you can see the number of total transactions per second (tps) plus
how many of those transactions were reads and writes (rtps and wtps,
respectively). The bread/s column doesn’t measure bread I/O, instead it tells
you the average number of bytes read per second. Similarly, the bwrtn/s tells
you average bytes written per second.


#### `sar` command

Time range:

```
$ sar -s 20:00:00 -e 20:30:00
Linux 2.6.24-22-server (kickseed) 01/07/2012
08:05:01 PM CPU %user %nice %system %iowait %steal %idle
08:15:01 PM all 0.49 0.00 1.12 0.62 0.00 97.77
08:25:01 PM all 0.49 0.00 2.15 1.21 0.00 96.16
Average: all 0.49 0.00 1.63 0.91 0.00 96.96
```

If you want to pull data from a day other than today, just use the -f option
followed by the full path to the particular statistics fi le stored under
`/var/log/sysstat` or /`var/log/sa.` For instance, to pull data from the statistics
on the sixth of the month you would type
`$ sar -f /var/log/sysstat/sa06`
You can combine any of the other `sar` options as normal to pull out specifi c
types of statistics.
