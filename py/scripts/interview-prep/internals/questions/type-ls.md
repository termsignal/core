# What happens when you type ls into the terminal?

## Overview

### Type Command in `ls -l`

`$ ls -l`

### The Shell reads the command from the standard input

The getline() function reads the entered line as one string from standard input

`getline(&buffer,&size,stdin);`

The getline() function is prototyped in the stdio.h header file. Here are the three arguements

* `&buffer` - The address of the first character position where the input string will be stored. its not the base address of the buffer, but of the first character in the buffer. This pointer type causes massive confusion.
* `&size` is the address of the virable that holds the size of the input buffer, another pointer
* `stdin` ins the input file handle. So you could use getline() to read a line of text form a file, but when stdin is specified, standard input is read.

After reading the line and storing it in the buffer, the getline returns an int/ssize)t which is equal to

1. The number of characters read, on success, without including the terminating null byte of the string

or

2. -1, on failure to read a line including end of file conditions

### Breakdown commands into tokens

A string tokenization function is called which splits the command into tokens. In our shell we used a function caled `strtok()` which took the line to tokenize and the delimeter to define the token boundaries.

For example

`$ ls -la /`

We have the name of the binary `ls` and its arguments

The command could aslo be

`$ ls      -la    /`

We are going to write a function that will store our command without the spaces in a charr** which will give

`[ls][-la][/]`

### Check for shell expansion

After the command has been split into tokens or words expanded or resolved.

There are 8 expansions.

* Brace Expansion
* Tilde Expansion
* Shell parameter and variable expansion
* Command Subsitution
* Arithmetic Expansion
* Process Substitution
* Word splitting
* File name expansion

### Check for alias

An alias allows a string to be substituted for a word when it is used as the first word of a simple command. The shell maintains list of aliases and unalias built-in commands. 

```
franky: ~> alias
alias ..='cd ..'
alias ...='cd ../..'
alias ....='cd ../../..'
alias PAGER='less -r'
alias Txterm='export TERM=xterm'
alias XARGS='xargs -r'
alias cdrecord='cdrecord -dev 0,0,0 -speed=8'
alias e='vi'
alias egrep='grep -E'
alias ewformat='fdformat -n /dev/fd0u1743; ewfsck'
alias fgrep='grep -F'
alias ftp='ncftp -d15'
alias h='history 10'
alias fformat='fdformat /dev/fd0H1440'
alias j='jobs -l'
alias ksane='setterm -reset'
alias ls='ls -F --color=auto'
alias m='less'
alias md='mkdir'
alias od='od -Ax -ta -txC'
alias p='pstree -p'
alias ping='ping -vc1'
alias sb='ssh blubber'
alias sl='ls'
alias ss='ssh octarine'
alias tar='gtar'
alias tmp='cd /tmp'
alias unaliasall='unalias -a'
alias vi='eval `resize`;vi'
alias vt100='export TERM=vt100'
alias which='type'
alias xt='xterm -bg black -fg white &'

franky ~>
```

### Is the command a builtin command?


### Find the location of the executable program.

### Search for paths defined in $PATH

### What if the program is not found?
