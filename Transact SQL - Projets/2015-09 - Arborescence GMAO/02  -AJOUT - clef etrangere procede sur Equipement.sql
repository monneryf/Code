-- ajout d'une clef étrangères manquante

ALTER TABLE [dbo].[Equipement]
   ADD CONSTRAINT [FK_Equipement_Procede]
   FOREIGN KEY ([idProcede])
   REFERENCES [dbo].[Procede] ([idProcede]);
