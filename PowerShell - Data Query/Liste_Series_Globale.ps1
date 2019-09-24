$Path = 'F:\Series'
$Destination = 'C:\Users\monne\Desktop\'

$File = $Destination + '\Liste Series Global.txt'

If (Test-Path $File)
    {Remove-Item $File}

If (-Not(Test-Path $File))
    {out-file -FilePath $File}

foreach ($Repertoire in Get-ChildItem -Path $Path -Director)
{    
    $Directory = $Path + '\' + $Repertoire

     Get-ChildItem -Path $Directory -File -Include *.avi,*.mkv,*.mp4,*.mpg,*.wmv -Recurse  | Where-Object { $_.length -gt 50000000 } | Format-Table -Property @{Label='-------------------------- Titre Episode --------------------------- ';Expression={$_.Name}}, @{Label='---------- Serie ---------- ';Expression={$Repertoire}}|  out-file -FilePath $File -Append
}






    




     