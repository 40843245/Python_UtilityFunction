# Release Notes
## In version 1
### Release Date:
2023/02/23 20:50 p.m.
### Bugs
There are NO errors.

However, when you try to open Microsoft Application at runtime.

It will open the file explorer then list all applications you want to open.

### Function:
One can open the Microsoft App through Powershell with specified AUMID.

My code will invoke the command of Powershell.

"start shell:appsfolder\ " + " <AUMID>"

### NOTICE

It is only available in Windows. 

NOT in other OS.

There may be slightly different for AUMID in each version of Windows.

Thus, it may be one reason to fail when you execute it.

Check AUMID when troubleshooting.

### Ref
https://stackoverflow.com/questions/43696735/how-can-i-open-a-windows-10-app-with-a-python-script
