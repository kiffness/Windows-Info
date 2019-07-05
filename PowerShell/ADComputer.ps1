Get-AdComputer -Filter {Enabled -eq $False} | Sort name | Select -ExpandProperty Name | Out-File F:\Windows_10_Refresh\Powershell\DisabledComputer.txt -Encoding utf8

$MyPath = "F:\Windows_10_Refresh\Powershell\DisabledComputer.txt" # read the file in
$MyFile = Get-Content $MyPath
$Utf8NoBomEncoding = New-Object System.Text.UTF8Encoding $False
$MyPathOut = "F:\Windows_10_Refresh\Powershell\DisabledAccountNoBOM.txt" # export it here without BOM
[System.IO.File]::WriteAllLines($MyPathOut, $MyFile, $Utf8NoBomEncoding)
