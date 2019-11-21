# Déclaration des variables

#$Path = 'E:\Videos\_Movies'
$Path = 'C:\Users\monne\Documents\_Movies\Series'
$Destination = 'C:\Users\monne\Desktop\Directory'

Copy-Item -Filter *.srt -Path $Path -destination $Destination -Recurse



