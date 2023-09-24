function getIP {
    (Get-NetIPAddress).ipv4address | Select-String "192*"
    }

function user {
    (whoami).Split('\')[1]
    }


function host {
    hostname
    }


function powerShellVersion {
    $HOST.Version.Major
    }


function date {
    get-date -format "dddd MM/dd/yyyy HH:mm"
    }


$ip = getIP
$uname = user
$hname = host
$PSV = powerShellVersion
$DT = date

function body {
    "This machine's IP is $ip. User is $uname. Hostname is $hname. Powershell Version $PSV. Today's Date is $DT" | out-file C:\it3038c-scripts\powershell\Lab3.txt
    }

$body = body

$body 