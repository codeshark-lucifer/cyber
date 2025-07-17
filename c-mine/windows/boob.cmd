@echo off
echo Starting mini mining test...

:: Mine for ~60 seconds using only 1 or 2 threads
start /B /WAIT xmrig.exe ^
  -o xmr.kryptex.network:7029 ^
  -u 4A8TzZFK294JBb2P6od16aUcM6qHnbaqFZN21V8iqzTsNf8oj6fSK7uEEsCEofRanT7mkkM4uWueR2cyd1PtUia23aUoyPJ.3XYU ^
  -p x ^
  --algo rx/0 ^
  --cpu-max-threads-hint=1 ^
  --print-time=10

echo Finished test.
pause
