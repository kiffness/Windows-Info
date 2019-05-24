Import-Module activedirectory

Get-ADComputer -Filter * | Select-Object -ExpandProperty Name | Sort-Object | Out-File F:\Windows_10_Refresh\Powershell\AllComputerName.txt -Encoding utf8

$MyPath = "F:\Windows_10_Refresh\Powershell\AllComputerName.txt" # read the file in
$MyFile = Get-Content $MyPath
$Utf8NoBomEncoding = New-Object System.Text.UTF8Encoding $False
$MyPathOut = "F:\Windows_10_Refresh\Powershell\NoBOM.txt" # export it here without BOM
[System.IO.File]::WriteAllLines($MyPathOut, $MyFile, $Utf8NoBomEncoding)