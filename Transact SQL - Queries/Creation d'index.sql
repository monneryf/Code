-- V�rification des processus les plus co�teux
USE MASTER;
EXEC sp_who2;
GO

USE Test;
GO

-- Cr�ation d'index
CREATE INDEX IDX_Movies_Family ON dbo.Movies(Family);
GO
CREATE INDEX IDX_Movies_Category ON dbo.Movies(Category)
GO
CREATE INDEX IDX_Movies_Country ON dbo.Movies(Country)
GO

-- V�rification donn�es
SELECT COUNT(*) FROM dbo.Movies 
WHERE Family = '';
GO

