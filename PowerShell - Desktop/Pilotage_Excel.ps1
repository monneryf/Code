# Déclaration des variables
 $Path = "c:\users\monne\Desktop\Sites\"
 $Name1 = "Site_1.xlsx"

$excel = new-object -comobject Excel.Application

#Start-Sleep -s 3

$excel.DisplayAlerts = $false
$excel.ScreenUpdating = $false
$excel.Visible = $false
$excel.UserControl = $false
$excel.Interactive = $false

$missing = [System.Reflection.Missing]::Value

echo $("Listing des fichiers")

$CSVs = @()

foreach ($fichier in Get-ChildItem -Path $Path )
        {$CSVs += ,$fichier
        }

echo($CSVs)

if (-Not $null -eq $CSVs) {
    for ($i=0; $i -lt $CSVs.Count; $i++){
        $chemin = $Path + $CSVs[$i]
        $csv = Get-Item $chemin
        $message = "Fichier n° " + $i + " - Nom : " + $csv.basename
        echo $($message)
        }}

echo $("Traitement de fichier : c:\Users\monne\Desktop\Site\Site_1.xlsx")

$excelWorkbook = $excel.workbooks.Open($Path + $Name1)
#Start-Sleep -s 2

#$excelWorkbook.RefreshAll()
#Start-Sleep -s 2

# On va parcourir les propriétés du document Excel pour prendre la date de dernière sauvegarde et la rentrer dans notre table
$binding = "System.Reflection.BindingFlags" -as [type]
Foreach($property in $excelworkbook.BuiltInDocumentProperties)
{$pn = [System.__ComObject].invokemember("name",$binding::GetProperty,$null,$property,$null)
 
 if ($pn -eq 'Last save time'){
 $LastRefresh = [System.__ComObject].invokemember("value",$binding::GetProperty,$null,$property,$null)
 Echo ("Date de dernière sauvegarde : " + $LastRefresh)
 }}

 #$worksheet = $workbook.worksheets.Item($i + 1)

$NewFilePath = [System.IO.Path]::ChangeExtension($excelWorkbook.Fullname,".txt")
$excelWorkbook.SaveAs($NewFilepath, 42)   # xlUnicodeText

echo "Fermeture du classeur"
$excelworkbook.Close()
 
$excel.Application.quit()


