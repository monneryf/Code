-- Vérification des processus les plus coûteux
USE MASTER;
EXEC sp_who2;
GO

USE Test;
GO

-- Création d'index
CREATE INDEX IDX_Movies_Family ON dbo.Movies(Family);
GO
CREATE INDEX IDX_Movies_Category ON dbo.Movies(Category)
GO
CREATE INDEX IDX_Movies_Country ON dbo.Movies(Country)
GO

-- Vérification données
SELECT COUNT(*) FROM dbo.Movies 
WHERE Family = '';
GO

