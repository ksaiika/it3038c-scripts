function getIP {
    (Get-NetIPAddress).ipv4address | Select-String "*192"
    }
write-host(getIP)

$IP=GetIP
*
Write-Host("This machine's IP is $IP")