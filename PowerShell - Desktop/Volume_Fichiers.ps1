$PathDrill = 'C:\Users\monne\Documents\_Movies'
$Destination = 'C:\Users\monne\Desktop'
$NameFolder = 'List_Files'
$NameFile = '_File_Lenghts'
$separator = '\'
$extension = '.txt'
$compteur = 0

$PathFolder = $Destination + $separator + $NameFolder
$PathFile = $PathFolder + $separator + $NameFile + $extension

If (-not(Test-Path $PathFolder))
    {
     New-Item -Path $PathFolder -ItemType directory
     }

If (Test-Path $PathFile)
       {
	    Remove-Item $PathFile
        }

function GetVolume
{

    ls -Directory  |
    Add-Member -Force -Passthru -Type ScriptProperty -Name Length -Value {ls $this -Recurse -Force | Measure -Sum Length | Select -Expand Sum } | 
                Sort-Object Length -Descending | 
                            Format-Table    @{label="---------Name-----------------------";Expression={$_.Name}}, 
                                            @{label="---------TotalSize (MB) ------------";expression={[string]::Format('{0:N0}',[Math]::Truncate($_.Length / 1MB))};width=14},
                                            @{label="---------Path-----------------------";Expression={$_.Fullname}} |
                                                out-file -FilePath $PathFile -Append
        }


cd $PathDrill

GetVolume

Get-ChildItem -Path $PathDrill -Directory | ForEach-Object -Begin {Write-Host "Début du traitement..."} -Process {cd $_.FullName; 
                                                                                                                  $compteur=$compteur+1;
                                                                                                                  $PathFile = $PathFolder + $separator + $_.Name + $extension;
                                                                                                                  GetVolume} -End {Write-Host "Fin de traitement"}
                                                                                







