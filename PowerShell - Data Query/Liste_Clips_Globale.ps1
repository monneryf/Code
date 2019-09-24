$Path = 'E:\Videos\Videos\Clips'
$Destination = 'C:\Users\monne\Desktop\Liste Clips'

foreach ($Repertoire in Get-ChildItem -Path $Path -Director)
{
    $File = $Destination + '\' +$Repertoire + '.txt'
    $Directory = $Path + '\' + $Repertoire

    If (Test-Path $File)
        {Remove-Item $File}

     Get-ChildItem -Path $Directory -File -Include *.* -Recurse  | Where-Object { $_.length -gt -1 } | Format-Table -Property @{Label='-------------------------- Nom fichier --------------------------- ';Expression={$_.Name}} |  out-file -FilePath $File
}






    




     