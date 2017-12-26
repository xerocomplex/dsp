# Learn command line

Please follow and complete the free online [Bash Scripting Tutorial](https://ryanstutorials.net/bash-scripting-tutorial/) or [Codecademy's Learn the Command Line](https://www.codecademy.com/learn/learn-the-command-line). These are helpful tutorials. You should be able to go through these in a couple of hours.

**Note:** Bash is not installed on a PC. Rather, PC users must install Cygwin. Once Cygwin has been installed, the command line interface witll _emulate_ bash. You can find all information regarding Cygwin [here](https://www.cygwin.com/).

---

### Q1.  Cheat Sheet of Commands  

Here's a list of items with which you should be familiar:  
* show current working directory path
* creating a directory
* deleting a directory
* creating a file using `touch` command
* deleting a file
* renaming a file
* listing hidden files
* copying a file from one directory to another

Make a cheat sheet for yourself: a list of at least **ten** commands and what they do.  (Use the 8 items above and add a couple of your own.)  

> > pwd - print the working directory  
> > mkdir - create a new directory  
> > rmdir - delete a directory, rm -d also works, rm -r will remove directories
> > that are not empty!  
> > touch <filename> - creates a new file  
> > rm - removes a file  
> > mv - rename file, or move file to new file in a new directory   
> > ls -a - lists all files, even those with . prefixes  
> > cp - copy a files  
> > cd - change the working directory  
> > pushd - push the specified directory onto the directory stack  
> > popd - remove the last pushed directory from the stack, change to the prev
> > dir

---

### Q2.  List Files in Unix   

What do the following commands do:  
`ls`  
`ls -a`  
`ls -l`  
`ls -lh`  
`ls -lah`  
`ls -t`  
`ls -Glp`  

> > ls - lists non-hidden files in the current directory
> > ls -a - lists ALL files, including hidden ones
> > ls -l - lists all files in long format, with expanded information
> > ls -lh - same as above, but gives suffixes for file sizes (B, K, M, G, etc)
> > ls -lah - combines -lh with -a options
> > ls -t - sorts by time modified, with most recently modified first
> > ls -Glp - colorized output, long format, shows '/' if file is dir

---

### Q3.  More List Files in Unix  

Explore these other [ls options](http://www.techonthenet.com/unix/basic/ls.php) and pick 5 of your favorites:

> > REPLACE THIS TEXT WITH YOUR RESPONSE

---

### Q4.  Xargs   

What does `xargs` do? Give an example of how to use it.

> > REPLACE THIS TEXT WITH YOUR RESPONSE
