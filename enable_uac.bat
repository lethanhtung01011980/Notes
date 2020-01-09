reg add "HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System" /f /v "FilterAdministratorToken" /t REG_DWORD /d 0x00000001 
cls 
ECHO "Your Windows 7 client will reboot in 15 seconds." 
timeout 15 
shutdown -t 0 -r 
