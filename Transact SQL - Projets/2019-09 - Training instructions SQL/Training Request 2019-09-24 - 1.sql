USE TEST
GO

SELECT * 
FROM dbo.Maires;
GO

SELECT (DATEDIFF(day,Date_de_naissance,getdate()))/365.25 AS Age
FROM dbo.Maires;
GO

UPDATE Maires SET Age = (DATEDIFF(day,Date_de_naissance,getdate()))/365.25
FROM dbo.Maires;

SELECT [Nom_de_l_�lu],[Age] FROM [dbo].[Maires]
ORDER BY Age ASC;
GO

UPDATE Maires SET Age_Categorie = 
						CASE
							WHEN Age >= 0 AND Age < 35 THEN '1 - Moins de 35 ans'
							WHEN Age >= 35 AND Age < 50 THEN '2 - Entre 35 et 50 ans'
							WHEN Age >= 50 AND Age < 70 THEN '3 - Entre 50 et 70 ans'
							WHEN Age >= 70 THEN '4 - Plus de 70 ans'
							END
FROM dbo.Maires;
GO

SELECT Age_Categorie,Count(Age_Categorie)
	FROM Maires
	GROUP BY Age_categorie
	ORDER BY Age_Categorie ASC
GO

SELECT [Libell�_de_d�partement__Maires_],Count([Libell�_de_d�partement__Maires_]) AS Nombre
	FROM [dbo].[Maires]
	GROUP BY [Libell�_de_d�partement__Maires_]
	ORDER BY Nombre DESC;
GO

select * FROM Maires
GO

SELECT [Code_profession],[Libell�_de_la_profession],COUNT([Libell�_de_la_profession]) As Nbre
FROM Maires
GROUP BY [Code_profession],[Libell�_de_la_profession]
ORDER BY Nbre DESC
GO

ALTER FUNCTION dbo.Calculate_Age(@Date_Naissance DATETIME2) Returns Decimal
AS BEGIN
	DECLARE @Age Decimal;
	SELECT @Age = Datediff(day,@Date_Naissance,getdate())/365.25;
	return(@Age)
	END;

GO

SELECT TOP 5 dbo.Calculate_Age([Date_de_naissance]) FROM [dbo].[Maires];
GO

ALTER TABLE Hierarchie
   ADD CONSTRAINT PK_PersonID PRIMARY KEY CLUSTERED (PersonID);

WITH Organigramme AS (
	SELECT H.* FROM [dbo].[Hierarchie] AS H WHERE H.[ParendID] IS NULL
	UNION ALL
	SELECT G.* FROM [dbo].[Hierarchie] as G INNER JOIN Organigramme AS O ON G.[ParendID] = O.[PersonID]
	) 
SELECT * FROM Organigramme;

GO

SELECT [Age_Categorie],[Libell�_de_la_profession],COUNT(*)
FROM [dbo].[Maires]
GROUP BY [Age_Categorie],[Libell�_de_la_profession]
WITH ROLLUP;
GO

SELECT [Age_Categorie],[Libell�_de_la_profession],COUNT(*)
FROM [dbo].[Maires]
GROUP BY [Age_Categorie],[Libell�_de_la_profession]
WITH CUBE;
GO

SELECT [Libell�_de_la_profession],
ntile(5) OVER (PARTITION BY [Libell�_de_la_profession] 
		 ORDER BY [Libell�_de_la_profession]) as Ensemble
FROM [dbo].[Maires]


select EtatRealisation,[H19] as "Equ1",[HC21] as "Equ2",[JK26] as "Equ3"
FROM Realisation
Pivot (sum(TpsArret) FOR Libelle in ([H19],[HC21],[JK26])) as pvt;
go

SELECT [Libell�_de_d�partement__Maires_],
[1 - Moins de 35 ans] as "Age1",
[2 - Entre 35 et 50 ans] As "Age2",
[3 - Entre 50 et 70 ans] As "Age3",
[4 - Plus de 70 ans] As "Age4"
  
  FROM [dbo].[Maires]
  Pivot(count([Age_Categorie]) FOR [Age_Categorie] IN ([1 - Moins de 35 ans],
										 [2 - Entre 35 et 50 ans],
										 [3 - Entre 50 et 70 ans],
										 [4 - Plus de 70 ans])) AS PVT;
GO

SELECT distinct([Age_Categorie]) FROM [dbo].[Maires]

BEGIN Transaction 
	UPDATE [dbo].[Maires]
	SET [Libell�_de_d�partement__Maires_] = 'RHONE'
	WHERE [Code_du_d�partement__Maire_]='69';
	IF @@ROWCOUNT = 1 
		BEGIN
			PRINT @@ROWCOUNT
			PRINT'Nombre de ligne �gal � 1'
			PRINT'Transaction valid�e'
			COMMIT;
		END
	ELSE 
		BEGIN
			PRINT @@ROWCOUNT
			PRINT'Nombre de ligne sup�rieur � 1'
			PRINT'Transaction annul�e'
			ROLLBACK;
		END
GO

CREATE FUNCTION MAIRE_DEPARTEMENT(@Departement Varchar(50)) 
	RETURNS TABLE
	AS
		RETURN (SELECT * FROM [dbo].[Maires] WHERE [Code_du_d�partement__Maire_] = @Departement)
	GO

SELECT * FROM [dbo].[MAIRE_DEPARTEMENT]('01')
GO

 SELECT * FROM [dbo].[Good_Position]()
 GO

 SELECT * FROM [dbo].[Maires]
EXCEPT 
SELECT * FROM [dbo].[Maires] WHERE [Code_du_d�partement__Maire_] != '01'
GO

SELECT [Nom_de_l_�lu],
	   [Code_du_d�partement__Maire_],
	    ROW_NUMBER() OVER(PARTITION BY [Code_du_d�partement__Maire_] ORDER BY [Code_du_d�partement__Maire_])

FROM [dbo].[Maires]
GO

SELECT 
	   [Code_du_d�partement__Maire_],
       [Nom_de_l_�lu],
	   [Pr�nom_de_l_�lu],
	   LAG([Nom_de_l_�lu],1) OVER (PARTITION BY [Code_du_d�partement__Maire_] 
							 ORDER BY [Code_du_d�partement__Maire_],
							          [Nom_de_l_�lu]) 
																	as precedent,
	   LEAD([Nom_de_l_�lu],1) OVER (PARTITION BY [Code_du_d�partement__Maire_] 
							 ORDER BY [Code_du_d�partement__Maire_],
							          [Nom_de_l_�lu]) 
																	as suivant
FROM
	   [dbo].[Maires]

ORDER BY
		[Code_du_d�partement__Maire_],
		[Nom_de_l_�lu]


SELECT 

	[Code_du_d�partement__Maire_],
	[Nom_de_l_�lu],
	[Pr�nom_de_l_�lu],

	COUNT([Code_du_d�partement__Maire_]) OVER( PARTITION BY [Code_du_d�partement__Maire_]
										 ORDER BY [Code_du_d�partement__Maire_]) AS Nbre_commune

FROM
	[dbo].[Maires]
ORDER BY
	[Nom_de_l_�lu]

----------------------------------------------
'INSTRUCTION DEPRECATED AFTER SQL SERVER 2012'
----------------------------------------------

	SELECT
	[Nom_de_l_�lu],
	[Pr�nom_de_l_�lu],
	[Libell�_de_la_commune]
FROM 
	[dbo].[Maires]

ORDER BY [Code_du_d�partement__Maire_]

COMPUTE COUNT([Libell�_de_d�partement__Maires_]) BY [Code_du_d�partement__Maire_];

GO




