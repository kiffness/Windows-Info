Import-Module activedirectory

Get-ADComputer -Filter * -Properties * | Select-Object Name,OperatingSystem,LastLogonDate | Export-Csv F:\Windows_10_Refresh\Powershell\All-Windows.csv -NoTypeInformation -Encoding UTF8