# Déploiement vers l'extranet - Partie 1
# Ce script s'exécute sur le serveur SharePoint Intranet

Add-PSSnapin Microsoft.SharePoint.PowerShell -ErrorAction SilentlyContinue 

$siteURLsource = "http://intranet.photowatt.local"
$partage = "\\SRV-SP-SQL-EXT\Data" 

$c1 = $Error.Count

cd "FileSystem::\\SRV-SP-SQL-EXT\Data"
del *.export.log

# Exporter une partie des listes du site racine
# =============================================
# http://intranet.photowatt.local/Accueil%20%20News%20%20Images/Forms/Thumbnails.aspx
Export-SPWeb http://intranet.photowatt.local -ItemUrl /Accueil%20%20News%20%20Images -Path ($partage + "\LST-AccueilNewsImages.bak") -Force

# http://intranet.photowatt.local/Lists/Accueil%20%20News%20Texte/AllItems.aspx
Export-SPWeb http://intranet.photowatt.local -ItemUrl /Lists/Accueil%20%20News%20Texte -Path ($partage + "\LST-AccueilNewsTexte.bak") -Force

# http://intranet.photowatt.local/PublishingImages/Forms/Thumbnails.aspx
Export-SPWeb http://intranet.photowatt.local -ItemUrl /PublishingImages -Path ($partage + "\LST-Images.bak") -Force

# http://intranet.photowatt.local/SitePages/Forms/AllPages.aspx
Export-SPWeb http://intranet.photowatt.local -ItemUrl /SitePages -Path ($partage + "\LST-PagesSite.bak") -Force


# Exporter une partie des listes du site Communication
# ====================================================
# http://intranet.photowatt.local/Communication/EDF%20Communication/Forms/AllItems.aspx
Export-SPWeb http://intranet.photowatt.local/Communication -ItemUrl /Communication/EDF%20Communication -Path ($partage + "\LST-COMM-EDFComm.bak") -Force

# http://intranet.photowatt.local/Communication/Notes%20de%20service/Forms/AllItems.aspx
Export-SPWeb http://intranet.photowatt.local/Communication -ItemUrl /Communication/Notes%20de%20service -Path ($partage + "\LST-COMM-NotesService.bak") -Force

# http://intranet.photowatt.local/Communication/News%20PhotoWatt/Forms/AllItems.aspx
Export-SPWeb http://intranet.photowatt.local/Communication -ItemUrl /Communication/News%20PhotoWatt -Path ($partage + "\LST-COMM-NewsPhotowatt.bak") -Force

# http://intranet.photowatt.local/Communication/Revue%20de%20presse/Forms/AllItems.aspx
Export-SPWeb http://intranet.photowatt.local/Communication -ItemUrl /Communication/Revue%20de%20presse -Path ($partage + "\LST-COMM-RevuePresse.bak") -Force



# Exporter une partie des listes du site EDF Communication
# ========================================================
# http://intranet.photowatt.local/Communication/EDF/Communication%20EDF/Forms/AllItems.aspx
Export-SPWeb http://intranet.photowatt.local/Communication/EDF -ItemUrl /Communication/EDF/Communication%20EDF -Path ($partage + "\LST-COMM-EDF-CommEDF.bak") -Force

# http://intranet.photowatt.local/Communication/EDF/INFO%20FLASH%20EDF%20EN/Forms/AllItems.aspx
Export-SPWeb http://intranet.photowatt.local/Communication/EDF -ItemUrl /Communication/EDF/INFO%20FLASH%20EDF%20EN -Path ($partage + "\LST-COMM-EDF-InfoFlashEDF.bak") -Force

# http://intranet.photowatt.local/Communication/EDF/SitePages/Forms/AllPages.aspx
Export-SPWeb http://intranet.photowatt.local/Communication/EDF -ItemUrl /Communication/EDF/SitePages -Path ($partage + "\LST-COMM-EDF-SitePages.bak") -Force

# http://intranet.photowatt.local/Communication/EDF/VIGILANCE%20MAG/Forms/AllItems.aspx
Export-SPWeb http://intranet.photowatt.local/Communication/EDF -ItemUrl /Communication/EDF/VIGILANCE%20MAG -Path ($partage + "\LST-COMM-EDF-VigilanceMag.bak") -Force

# http://intranet.photowatt.local/Communication/EDF/VIVRE%20EDF%20hebdo/Forms/AllItems.aspx
Export-SPWeb http://intranet.photowatt.local/Communication/EDF -ItemUrl /Communication/EDF/VIVRE%20EDF%20hebdo -Path ($partage + "\LST-COMM-EDF-VivreEDFHebo.bak") -Force

# http://intranet.photowatt.local/Communication/EDF/VIVRE%20EDF%20MAG/Forms/AllItems.aspx
Export-SPWeb http://intranet.photowatt.local/Communication/EDF -ItemUrl /Communication/EDF/VIVRE%20EDF%20MAG -Path ($partage + "\LST-COMM-EDF-VivreEDFMag.bak") -Force


# Exporter le site CE et ses sous-sites
# =====================================
Export-SPWeb http://intranet.photowatt.local/CE -Path ($partage + "\SITE-CE.bak") -Force

# Exporter le site Challenge 10 000 pas et ses sous-sites
# =======================================================
#Export-SPWeb http://intranet.photowatt.local/Be_walk -Path ($partage + "\SITE-Be_walk.bak") -IncludeUserSecurity -Force
Export-SPWeb http://intranet.photowatt.local/Be_walk -Path ($partage + "\SITE-Be_walk.bak") -Force


$c2 = $Error.Count


exit $c2-$c1