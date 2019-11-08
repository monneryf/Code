# Déclaration des variables
$Path = 'E:\Videos'
$Destination = 'C:\Users\monne\Desktop\Subtitles'

#Copy-Item -Filter *.txt -Path $Path -destination $Destination

set-location $Path
Get-ChildItem *.srt -Recurse | Copy-Item -Destination $Destination

