# UAC_bypass_System_shell
Bypass UAC to get system shell

User has to be in Administrators group for successfull execution.

The executable downloads UAC_bypass.dll, nc.exe and initial.mof files on the host and runs as Administrator bypassing UAC to get the shell. 

Need attacker to listen using nc -lvnp port
