# Déclaration des variables
$Path = 'C:\Users\monne\Documents\_Movies\2019-08-25'
$Destination = 'C:\Users\monne\Desktop\'
$Extension = '.txt'

$Name = 'List_Files'

$File = $Destination + '\' + $Name + $Extension

# Suppression de l'ancien fichier en cas de nouvelle exécution
If (Test-Path $File)
    {Remove-Item $File}

# Listing du contenu du répertoire
Get-ChildItem -Path $Path -File -Include *.avi,*.mkv,*.mp4,*.mpg,*.wmv -Recurse  | Where-Object { $_.length -gt 100000000 } | Format-Table -Property @{Label='-------------------------- Nom fichier --------------------------- ';Expression={$_.Name}} |  out-file -FilePath $File




