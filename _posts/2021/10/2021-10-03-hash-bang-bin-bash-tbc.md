---
title: "hash bang/bin/bash (tbc)"
date: "2021-10-03"
categories: 
  - "linux-cli"
---

- Some basic commands:
    - exit: exit to the current status
    - env: environment variable
    - echo "$shell": show what shell you're currently using
    - bash: use bash, use 'exit' to go back
    - clear: clear things in your cmd window
    - reset: The **reset command** under a [BSD](https://bash.cyberciti.biz/guide/BSD)/[Linux](https://bash.cyberciti.biz/guide/Linux)/[UNIX](https://bash.cyberciti.biz/guide/UNIX) operating system is used to restore a console to a normal state. This is useful after a program dies leaving a terminal in an abnormal state.
- Some basic command related to directory
    - cd
    - cd {directory}
    - pwd : current directory
    - mkdir {directory}: create directory
    - mkdir -p {directory}: recursively create directory
    - pushd {directory}:
    - popd : pop up the directory, could use with popd +n (n is the number of the directory in the directory list)
    - dirs -v : list the directory stack
    - cd -: change between 2 different directory
    - cd -{N}: change to the Nth directory.

When the script fails, it is a very distinctive behavior to record the processed content, but it is inconvenient to destroy the execution. The existence of the trap command in Bash is probably to solve this problem. It can attract the termination signal of the script and solve this problem in the way you want.

- trap [-lp] [[arg] signal_spec ...]
    - -l print signal name and corresponding number
    - -p show any trap command that is related to each signal
    - arg：command to execute when getting signal
    - signal_spec：signal name or number
    - 'trap' could be used d for the actions that need to be taken when the corresponding signal is obtained, and it can be used to perform clean-up work when the program is interrupted

[![](https://zhengliangliang.files.wordpress.com/2021/09/screenshot-2021-09-29-at-21.44.02.png?w=1024)](https://zhengliangliang.files.wordpress.com/2021/09/screenshot-2021-09-29-at-21.44.02.png)

Example of trap:

- 做数字比较用 `(())`，做字符比较用 `[[]]`
- Golden Rules:
    
- The golden rule on quoting is very simple:
    - If there is whitespace or a symbol in your argument, you **must** quote it.
    - If there isn't, quotes are usually optional, but you can still quote it to be safe.
- `${}` acts as a kind of quoting for variables.
- `$()` acts as a kind of quoting for commands but they're running in their own context.

- processes use file descriptors to connect to streams. Each process will generally have three standard file descriptors: standard input (FD 0), standard output (FD 1) and standard error (FD 2).
    - Redirecting standard output is done using the `>` operator.
    - Redirecting stnadard error id done using >2 operator
- syntax `2>&1` means 'Make FD `2` write(`>`) to where FD(`&`) `1` is currently writing'
- File redirecting:
    - placeholder
- Some useful variables in bash:
    - `**$@**` refers to all of a shell script’s command-line arguments.
    - **$*** refers to all the shell script's command-line arguments, it could be the same as $@ if not without "", with quoting, all of the arguments are viewed separately but $* will be one batch of data. means $@ need to run n times if there are n arguments using for loop, but $* only need to for once to get all the arguments.
    - **$$** refers to the process id of the shell
    - **$!** refers to **shebang**, the part after the #! tells Unix what program to use to run it.
    - **!!** refers to your previous shell command , called **bang-bang**
    - **$#** refers to the number of arguments passed to the shell
    - **$0** refers to the filename of the filename of the script
    - **${BASH_SOURCE[0]}** contains the (potentially relative) path of the containing script in _all_ invocation scenarios, notably also when the script is _sourced_, which is not true for `$0`.
        - Difference between $0 and ${BASH_SOURCE[0]}: [here](https://www.junmajinlong.com/shell/bash_source/)
    - **$1** to $n refers to each argument added to the shell script, $1 is the first one, and $n is the nth one.

My personal shell script template: [here](https://github.com/ZhengLiangliang1996/BashPractice/blob/master/BashPractice/template.sh)

[![](https://zhengliangliang.files.wordpress.com/2021/10/screenshot-2021-10-04-at-22.08.48.png?w=906)](https://zhengliangliang.files.wordpress.com/2021/10/screenshot-2021-10-04-at-22.08.48.png)
