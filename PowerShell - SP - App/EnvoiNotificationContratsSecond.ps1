# Script d'envoi automatique de notification lorsque un contrat juridique arrive à échéance

# Auteur : Eric Wyss, pour le compte de la société Photowatt
# Date de création : 24/02/2016
# Date de mise à jour : 29/03/2016
# Version 1.03

$url = "http://intranet.photowatt.local/juridique"
$contrats = "Contrats"
$historique = "Historique Notifications"
$listeDiffusion = "Listes de diffusion"

$smtp = "smtp.photowatt.com"
$from = "intranet@photowatt.com"
$Global:body = ""
$anonUsername = "anonymous"
$anonPassword = ConvertTo-SecureString -String "anonymous" -AsPlainText -Force
$anonCredentials = New-Object System.Management.Automation.PSCredential($anonUsername,$anonPassword)

$timestamp = Get-Date -Format o | foreach {$_ -replace ':', "."}
$LogFile = "C:\Logs\$timestamp.log"

$ver = $host | select version
if ($ver.Version.Major -gt 1) {$Host.Runspace.ThreadOptions = "ReuseThread"}
Add-PsSnapin Microsoft.SharePoint.PowerShell
Set-Location $home

########################################################################################################

Function LogWrite
{
	Param ([string]$logstring)
    $gd = Get-Date
    $logstring = ($gd.ToString() + " : " + $logstring) 
	Add-Content $LogFile $logstring
}

########################################################################################################



function setBody ($dateExpiration, $nom, $objet, $contractant, $TR)
{

    $lineA1 = "Bonjour,"
    $lineB1 = "Le contrat suivant arrive bientôt à échéance :"

    $lineC1 = "- Date expiration : $dateExpiration"
    $lineC2 = "- N° du contrat : $nom"
    $lineC3 = "- Objet du contrat : $objet"
    $lineC4 = "- Contractant(s) : $contractant"

    if ($TR -eq "Oui") {$lineC5 = "Nous vous rappelons qu'il convient de dénoncer le contrat d'ici la date susvisée, à défaut le contrat sera tacitement reconduit.";
                        $lineC6 = "Nous restons à votre disposition pour vous accompagner dans votre démarche.";
                        $groupe2 = "$lineC5`n`n$lineC6"}

if (($TR -eq $null) -or ($TR.Length -eq 0) -or ($TR -eq "Non"))
     			{$lineC5 = "Nous restons à votre disposition pour vous accompagner dans votre démarche de renégociation du contrat.";
                        $groupe2 = "$lineC5"}

    $lineD1 = "Bonne journée."
    $lineE1 = "Cordialement."
    $lineF1 = "L'équipe Juridique"

    $groupe1 = "$lineC1`n$lineC2`n$lineC3`n$lineC4"
    $Global:body = "$lineA1`n`n$lineB1`n`n$groupe1`n`n$groupe2`n`n$lineD1`n`n$lineE1`n`n$lineF1"
}

########################################################################################################

function Convert-StringToDateTime ($DateTimeStr)
{
# Converts from French to US date format (dd/mm/yyyy to mm/dd/yyyy)
$DateTimeParts = $DateTimeStr -split '/'
return $DateTimeParts[1]+'/'+$DateTimeParts[0]+'/'+$DateTimeParts[2]
}

#######################################################################################################

function sendNotification ($document, $firstSecond)
{
  LogWrite ("Debut sendNotification (" + $firstSecond + ") pour " + $document["Nom"])
  
 
  # Récupérer le contenu du champ Notification
  $emails = @();
  $notifColl = $document["Notification"] -as [Microsoft.SharePoint.SPFieldLookupValueCollection]
  foreach ($notif in $notifColl)
  {
      
      #Write-Host "notif =" $notif.LookupValue;
      $ld = $w.lists[$listeDiffusion];
	  foreach ($item in $ld.Items)
	{
    if ($item["Title"] -eq $notif.LookupValue) 
	{ 
        #Write-Host "Elément " $notif.LookupValue " trouvé dans liste de diffusion";
		if (($item["Emails"] -ne $null) -and ($item["Emails"].length -gt 0))
		{
        Write-Host "Emails : " $item["Emails"]
		[string[]]$emails2 = $item["Emails"].Split(';');
		foreach ($em in $emails2) { $emails += $em }
		}
	}
	}
  }
  
  if ($emails.length -eq 0) 
  { 
	LogWrite ("Erreur : Liste destinataires vide pour " + $document["Nom"])
	return 
  }

  ############################ Extraire le nom du contrat
  $NomContrat = $document["Nom"]
  $Point = $NomContrat.LastIndexOf(".")
  $Longueur = $NomContrat.length
  $Supprimer = $Longueur - $Point
  #Write-Host "Nombre de caractere :"  $Longueur
  #Write-Host "Position du point:"  $Point
  #Write-Host "Caractères à supprimer :"  $Supprimer
  
  $IDContrat = ($NomContrat).remove($Point,$Supprimer)

  ############################# Envoyer un email de notification
  Write-Host "Pour " $document.Name " , notification à " $emails.Length " personne(s)"

  if ($firstSecond -eq "First")
  {
	$sub = "Première notification pour contrat " + $IDContrat + " expirant le " + $document["Date expiration"].ToLongDateString() + " - " + $document["Contractant(s) - Vertrag(s)"] + " - " +  $document["Objet du contrat (Agreement's object / Gegenstand des Auftrags)"]
  }
  else
  {
	$sub = "RAPPEL : Deuxième notification pour contrat " + $IDContrat + " expirant le " + $document["Date expiration"].ToLongDateString() + " - " + $document["Contractant(s) - Vertrag(s)"] + " - " +  $document["Objet du contrat (Agreement's object / Gegenstand des Auftrags)"]
  }
  $encoding=[System.Text.Encoding]::UTF8

  ############################ Composer le corps du texte
  #Write-Host "Date expiration :" $document["Date expiration"].ToLongDateString()
  #Write-Host "N° du contrat :" $document["Nom"]
  #Write-Host "Objet du contrat :" $document["Objet du contrat (Agreement's object / Gegenstand des Auftrags)"]


  
  ############################ Envoyer l'email
  setBody $document["Date expiration"].ToLongDateString() $IDContrat $document["Objet du contrat (Agreement's object / Gegenstand des Auftrags)"] $document["Contractant(s) - Vertrag(s)"] $document["TR"] 

  $c1 = $Error.Count
  Write-Host "Envoi email notification " $document.Name " / Niveau : " $firstSecond
  send-MailMessage -SmtpServer $smtp -To $emails -Subject $sub -Body $Global:body -From $from -credential $anonCredentials -Encoding $encoding
  $c2 = $Error.Count

  if ($c1 -eq $c2)
  {
    LogWrite ("OK Envoi email (" + $firstSecond + ") pour " + $document["Nom"])
  }
  else
  {
    LogWrite ("Erreur Envoi email (" + $firstSecond + ") pour " + $document["Nom"])
  }
  
  # Si envoi sans erreur, créer une entrée dans l'historique
  if ($c1 -eq $c2)
  {
	$c3 = $Error.Count
    if ($firstSecond -eq "First")
	{
		$newitem = $historiqueList.AddItem();
        $newitem["Title"] = $document.Name;
        $newitem["Nature"] = "Premiere"
        $newitem["Date Expiration"] = $document["Date expiration"];
        $newitem.Update()
		
		#####################################################################
		# $document["PDF - Lancement"] = "OK"

		# $site = Get-SPSite "http://intranet.photowatt.local"

		# $manager=$site.WorkFlowManager

		# $wfToStart = "Notification Expiration"

		# $association=$doclib.WorkFlowAssociations | where {$_.Name -eq $wfToStart}
		# $association.AllowAsyncManualStart = $true
		# $association.AllowManual = $true

		# $assoc=$doclib.WorkflowAssociations["Notification Expiration"]
		
		# $data=$association.AssociationData

		# $wf=$manager.StartWorkFlow($doc, $association, $data)
		#######################################################################

	}
	else
	{
		$newitem = $historiqueList.AddItem();
        $newitem["Title"] = $document.Name;
        $newitem["Nature"] = "Deuxieme"
        $newitem["Date Expiration"] = $document["Date expiration"];
        $newitem.Update()
	}

	$c4 = $Error.Count
	if ($c3 -ne $c4)
	{
        LogWrite ("Erreur lors de la création d'une entrée dans historique pour " + $document["Nom"] + " (" + $firstSecond + ")")
        LogWrite $Error
	}
    else
    {
        LogWrite ("Succès lors de la création d'une entrée dans historique pour " + $document["Nom"] + " (" + $firstSecond + ")")
    }
    Write-Host "Envoi email de notification sans erreur";
  }

  LogWrite ("Fin sendNotification (" + $firstSecond + ") pour " + $document["Nom"])
}

##########################################################################################

$cc1 = $Error.Count
LogWrite "Debut execution du script EnvoiNotificationContrats"

$w = get-spweb $url 
$doclib = $w.lists[$contrats]
$historiqueList = $w.lists[$historique]
foreach ($doc in $doclib.Items)
{
  
  # Regarder si il s'agit d'un contrat principal
  # Un contrat est principal lorsque la colonne "Contrat Racine" est vide
  $contratRacine = $doc["Contrat Racine"];
  $Actif = $doc["Actifs"];
  if ((($contratRacine -eq $null) -or ($contratRacine.Length -eq 0)) -and ($Actif -eq "Oui"))
{

  # Regarder si le contrat dispose d'une date de notification
  $calcfield = $doc.fields["Date notification"] -as [Microsoft.SharePoint.SPFieldCalculated];
  $frDate = $calcfield.GetFieldValueAsText($doc["Date notification"]);
if (($frDate -ne $null) -and ($frDate.Length -gt 0))
{
  $usDate = Convert-StringToDateTime $frDate
  $NotificationDate = [datetime] $usDate



  # Comparer avec la date du jour dans le cas où il n'y a pas eu de première notification
  # Regarder si la date de notification est passée de 15 jours
  if ((get-date) -ge ($NotificationDate).AddDays(15))
  {

  # Regarder si nous sommes dans le cas d'une première notification sans seconde notification
  $spQuery = New-Object Microsoft.SharePoint.SPQuery 
  $camlQuery = '<Where><Eq><FieldRef Name="Title" /><Value Type="Text">' + $doc.Name + '</Value></Eq></Where>' 
  $spQuery.Query = $camlQuery 
  $spQuery.RowLimit = 100 
  $spListItem = $historiqueList.GetItems($spQuery) 

  $trouve1 = $false
  $trouve2 = $false
  foreach ($d in $spListItem)
  {
    if (($d["Nature"] -eq "Premiere") -and ($d["Date Expiration"] -eq $doc["Date expiration"])) {$trouve1 = $true }
    if (($d["Nature"] -eq "Deuxieme") -and ($d["Date Expiration"] -eq $doc["Date expiration"])) {$trouve2 = $true }
  }

	# Envoyer un email de première notification
  if (($trouve1 -eq $true) -and ($trouve2 -eq $false)) { sendNotification $doc "Second"; 	}
  }
}
}
}

LogWrite "Fin execution du script EnvoiNotificationContrats"
$cc2 = $Error.Count
exit $cc2-$cc1

