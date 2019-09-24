$path = "E:\Videos\Movies"
$destination = "E:\OneDrive\Divers\Listes\0 - Liste Globale\Liste Movies Chosen Few"
$nameFile_A = "Global"
$nameFile_B = "French"
$nameFile_C = "Last"
#$nameFile_D = "Average - 2018 - 3"
#$nameFile_E = "Blockbuster - 2019"
#$nameFile_F = "Foreign - 2018 - 3"
#$nameFile_G = "Good_2018 - 6"
#$nameFile_H = "Good_French_2018 - 4"
#$nameFile_I = "Seen"
#$nameFile_J = "Average - French - 2019"

#$nameFiles = $nameFile_A,$nameFile_B,$nameFile_D,$nameFile_E,$nameFile_F,$nameFile_G,$nameFile_H,$nameFile_I,$nameFile_J
$nameFiles = $nameFile_A,$nameFile_B,$nameFile_C

foreach ($nameFile in $nameFiles) {
    
    $File = $destination + "\" + $nameFile + '.txt'
    $pathFile = $path + '\' + $nameFile

    Get-ChildItem -Path $pathFile -File -Include *.avi,*.mkv,*.mp4,*.mpg,*.wmv -Recurse  | 
                                    Where-Object { $_.length -gt 100000000 } | 
                                    Format-Table -Property @{Label='-------------------------- Nom fichier --------------------------- ';Expression={$_.Name}} |  
                                    out-file -FilePath $File
                                    }






