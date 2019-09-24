#####################################################################
# Initialisation des variables

$repertoire = 'C:\Users\monne\Desktop\Repo'
$Source = 'C:\Users\monne\Desktop\Repo' + '\' +  'Chapitre_000.docx'
$nombreFichier = 141
$extension = '.docx'

#####################################################################
# Génération du nom du fichier

Function Numero($numeroIncrement) {

    # Composition du numéro sur trois caractères
         if ($numeroIncrement -lt 10) {
            $nomFichier = '00' + $numeroIncrement}
         else {
                if ($numeroIncrement -lt 100) {
                    $nomFichier = '0' + $numeroIncrement
                    }
                else {
                      $nomFichier = $numeroIncrement}
                      }
                          
        $nomFichierComplet = 'Chapitre_' + $nomFichier + $extension   
                       
        return $nomFichierComplet
        }    

#####################################################################
# Duplication des fichiers dans le répertoire cible                                                    

for ($numeroFichier = 1;
     $numeroFichier -le $nombreFichier;
     $numeroFichier++) {
            
          $nomFichierDestination = Numero $numeroFichier 
          $Destination = $repertoire + '\' +  $nomFichierDestination
          
          copy-item $source $Destination
            }
                                             








