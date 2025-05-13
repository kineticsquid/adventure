https://ics.uci.edu/~pattis/common/handouts/macmingweclipse/allexperimental/mac-gdb-install.html
- `brew install gdb`
- Created certificate on System keychain
- Whacked process `taskgated` from Activity Monitor
- Didn't restart automatically, had to restart OSX
- `taskgated-helper` started and eventually `taskgated` was running again. Took about 5 minutes.
- `codesign -s gdbcert /usr/local/bin/gdb`
- `gdb --version` to verify


to build: 
    - Select file
    - Command Line: Tasks: Run Build Task
to debug: 
    - Select c source file
    - Run > Start debugging


