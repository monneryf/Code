import os
import pickle

class Score:
    def __init__(self):
        self.path = 'C:\\Users\\monne\\source\\repos\\Jeu_Pendu'
        self.name = 'Score_Game'
        self.name_file = name_file = os.path.join(self.path,self.name)

    def charger_Score(self):        
        if os.path.exists(name_file):
            with open(self.name_file,"rb") as f:
                depickler = pickle.Unpickler(f)
                fichier = depickler.load()
        else:
            fichier = dict()
        return fichier

    def sauvegarder_Score(self,name,score):
        fichier_score = self.charger_Score()
        if name in fichier_score:
            fichier_score[name]+=score
        else:
            fichier_score[name]=score
        with open(self.name_file,'wb') as f:
            pickler = pickle.Pickler(f)
            pickler.dump(fichier_score)

    def retourner_Score(self,name):
        fichier_score = self.charger_Score()
        if name in fichier_score:
            return fichier_score[name]
        else:
            return 0


        



