## 0x01. Shell, permissions
Answers to exercises from 0x01 Shell, permissions

0. My name is Betty
  Create a script that changes your user ID to betty.
  * You should use exactly 8 characters for your command (+1 character for the new line)
  * You can assume that the user betty will exist when we will run your script
1. Who am I
  Write a script that prints the effective userid of the current user.
2. Empty!
  Write a script that creates an empty file called hello.
3. Groups
  Write a script that prints all the groups the current user is part of.
4. New owner
  Write a script that changes the owner of the file hello to the user betty.
5. Execute
Write a script that adds execute permission to the owner of the file hello.
  * The file hello will be in the working directory
6. Multiple permissions
Write a script that adds execute permission to the owner and the group owner, and read permission to other users, to the file hello.
  * The file hello will be in the working directory
7. Everybody!
Write a script that adds execution permission to the owner, the group owner and the other users, to the file hello
  * The file hello will be in the working directory
  * You are not allowed to use commas for this script
8. James Bond
Write a script that sets the permission to the file hello as follows:
  * Owner: no permission at all
  * Group: no permission at all
  * Other users: all the permissions
  * The file hello will be in the working directory You are not allowed to use commas for this script
9. John Doe
Write a script that sets the mode of the file hello to this:
`-rwxr-x-wx 1 julien julien 23 Sep 20 14:25 hello`
  * The file hello will be in the working directory
  * You are not allowed to use commas for this script
10. Look in the mirror
Write a script that sets the mode of the file hello the same as olleh’s mode.
  * The file hello will be in the working directory
  * The file olleh will be in the working directory
11. Directories
Create a script that adds execute permission to all subdirectories of the current directory for the owner, the group owner and all other users. Regular files should not be changed.
12. More directories
Create a script that creates a directory called dir_holberton with permissions 751 in the working directory.
13. Change group
Write a script that changes the group owner to holberton for the file hello
  * The file hello will be in the working directory
14. Owner and group
Write a script that changes the owner to betty and the group owner to holberton for all the files and directories in the working directory.
15. Symbolic links
Write a script that changes the owner and the group owner of the file _hello to betty and holberton respectively.
  * The file _hello is in the working directory
  * The file _hello is a symbolic link
16. If only
Write a script that changes the owner of the file hello to betty only if it is owned by the user guillaume.
  * The file hello will be in the working directory
17. Star Wars
Write a script that will play the StarWars IV episode in the terminal.
18. RTFM
Create a man that looks exactly like this one and passes all checks.
'''
ubuntu@ip-172-31-63-244:/tmp/man$ wc 101-man_holberton
 16  89 608 101-man_holberton
ubuntu@ip-172-31-63-244:/tmp/man$ man ./101-man_holberton
'''
