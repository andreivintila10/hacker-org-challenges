@echo off
FOR /L %%i IN (1,1,65535) DO (
  telnet -f C:\Users\andrei\Desktop\Hacker\Don't_Blink_[Web]\output.txt http://www.hacker.org/challenge/misc/one.php %%i
)
pause