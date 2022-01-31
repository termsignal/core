# Linux Kernel


## Fundamental Architecture of GNU Linux 

![The fundamental architecture of the GNU/Linux operating system](https://developer.ibm.com/developer/default/articles/l-linux-kernel/images/figure2.jpg)

![One architectural perspective of the Linux kernel](https://developer.ibm.com/developer/default/articles/l-linux-kernel/images/figure3.jpg)

## Properties of a Linux Kernel

### System Call Interface

A thing layer that provides the means to perform function calls from user space to kernel

SCI is Architecture Dependent 

### Process Management

Component responsible for the execution of processes.

`Threads` are `Processes` and represent an individual virtualization of the processor.(thread code, data, stack, and CPU registers)

The Kernel Provides an API  through SCE to create a new process. (fork, exec, POSIX functions), stop a process(kill, exit), and communicate and synchronize between them (signal, or POSIX)


Also,process management is the need to share teh CPU between the active threads. The kernel inplements a novel scheduling algorithm that operate in contatnt time, regardless of the nymber of vying for the CPU. THis is called the 0(1) scheduler denoted by the fact thats the BigO notation. This scheduler accepts multiple processors.


### Memory Management

Given the way hardware manages virtual memory, memory is managed in what are called `pages` 4kb in size for the most part. Linux allows the means to manange the available memory, as well as the hardware mechanisms for the physical and virutal mappings.

Linux provides abstractions over the 4k buffers such as the slab allocator. This scheme uses 4kb buffers as its base, but then allocates structures from within, keeping track of which pages are full, partually used, and empty, this allows the scheme to dynamically grow and shrink based on the needs of the greater system. 

Memory can be moved to the hard disk if it is exhausted.

### Virtual File System

This component provides an interface for file systems. The VFS provides switching layer betweek the SCI and the file systems that supported by the kernel.

### Network Stack

The network stack follows a layered architecture modeled after the protocols themselves.

The network stack, by design, follows a layered architecture modeled after the protocols themselves. Recall that the Internet Protocol (IP) is the core network layer protocol that sits below the transport protocol (most commonly the Transmission Control Protocol, or TCP). Above TCP is the sockets layer, which is invoked through the SCI.

The sockets layer is the standard API to the networking subsystem and provides a user interface to a variety of networking protocols. From raw frame access to IP protocol data units (PDUs) and up to TCP and the User Datagram Protocol (UDP), the sockets layer provides a standardized way to manage connections and move data between endpoints. You can find the networking sources in the kernel at ./linux/ne

TCP/IP


### Device Drivers

The vast majority of the source code in the Linux kernel exists in device drivers that make a particular hardware device usable. The Linux source tree provides a drivers subdirectory that is further divided by the various devices that are supported, such as Bluetooth, I2C, serial, and so on. You can find the device driver sources in ./linux/drivers.

### Architecture Dependent Code

While much of Linux is independent of the architecture on which it runs, there are elements that must consider the architecture for normal operation and for efficiency. The ./linux/arch subdirectory defines the architecture-dependent portion of the kernel source contained in a number of subdirectories that are specific to the architecture (collectively forming the BSP). For a typical desktop, the i386 directory is used. Each architecture subdirectory contains a number of other subdirectories that focus on a particular aspect of the kernel, such as boot, kernel, memory management, and others. You can find the architecture-dependent code in ./linux/arch.
