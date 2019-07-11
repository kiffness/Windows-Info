$MyPath = "F:\Windows_10_Refresh\Powershell\CouldNotConnect.txt" # read the file in
$MyFile = Get-Content $MyPath
$Utf8NoBomEncoding = New-Object System.Text.UTF8Encoding $False
$MyPathOut = "F:\Windows_10_Refresh\Powershell\CouldNotConnectNoBom.txt" # export it here without BOM
[System.IO.File]::WriteAllLines($MyPathOut, $MyFile, $Utf8NoBomEncoding)
