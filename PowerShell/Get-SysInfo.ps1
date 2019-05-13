Param(
[string]$Computer
)

$Connection = Test-Connection $Computer -Count 1 -Quiet

Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
if ($Connection -eq "True"){
    $ComputerOS = (Get-WmiObject Win32_OperatingSystem -ComputerName $Computer).Version
    $Logged_User = (Get-WmiObject -Class win32_computersystem -ComputerName $Computer).UserName
    $CPU = Get-WmiObject -ClassName Win32_Processor -ComputerName $Computer
    $MEM = Get-WmiObject -ClassName Win32_PhysicalMemoryArray -ComputerName $Computer
    $MEM_AMOUNT = Get-WmiObject -ClassName Win32_PhysicalMemory -ComputerName $Computer
    $DIMM = $MEM_AMOUNT = Get-WmiObject CIM_PHYSICALMEMORY -ComputerName $Computer

    switch -Wildcard ($ComputerOS){
      "6.1.7600" {$OS = "Windows 7"; break}
      "6.1.7601" {$OS = "Windows 7 SP1"; break}
      "6.2.9200" {$OS = "Windows 8"; break}
      "6.3.9600" {$OS = "Windows 8.1"; break}
      "10.0.*" {$OS = "Windows 10"; break}
      default {$OS = "Unknown Operating System"; break}
    }
@"
$($Computer)
$($Logged_User)
$($OS)
$($CPU.Name)
$($MEM_Amount.Capacity)
$($MEM.MemoryDevices)
"@ | Out-File -FilePath 'F:\Windows_10_Refresh\Powershell\SysConfig.txt' -Encoding ascii -Force
}
else {
    Write-Host -ForegroundColor Red @"
Computer is not reachable or does not exist
"@
}