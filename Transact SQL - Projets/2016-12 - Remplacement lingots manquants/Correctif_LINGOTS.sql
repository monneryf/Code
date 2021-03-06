-- ======================================================================================================
-- REQUETE 01 : LISTE DES LOTS AVEC LINGOTS NON RENSEIGNES
-- ======================================================================================================
WITH 
SQC_ASSEMBLAGE AS
(
	-- SQC : Liste les lots postérieurs au 01/11/2016 pour lesquels le Numero de lingot n'est pas spécifié
	SELECT	DISTINCT 
			L.[IdLot], L.[Lot], 
			CAST(CONVERT (VARCHAR, L.DateHeureEntrTextu, 103) + ' ' + CONVERT (VARCHAR, L.DateHeureEntrTextu, 108) AS DATETIME) AS DateHeureEntrTextu, 
			N.[N°Lingot] AS NumLingot
	FROM	T_LOT L INNER JOIN T_LOT_LINGOT N ON L.IdLot = N.IdLot 
	WHERE   L.DateHeureEntrTextu > CAST('01/11/2016 00:00:01' AS DATETIME)
	AND		N.[N°Lingot] = '0'
)
SELECT S.DateHeureEntrTextu, S.IdLot, S.Lot
FROM   SQC_ASSEMBLAGE AS S 
ORDER BY S.DateHeureEntrTextu ASC

-- ======================================================================================================
-- REQUETE 02 : LISTE DES LOTS ET CORRESPONDANCE ASSEMBLAGE ET LINGOTS
-- ======================================================================================================
WITH 
SQC_ASSEMBLAGE AS
(
	-- SQC : Liste les lots postérieurs au 16/11/2016 pour lesquels le N) de lingot n'est pas spécifié
	SELECT	DISTINCT 
			L.[IdLot], L.[Lot], 
			CAST(CONVERT (VARCHAR, L.DateHeureEntrTextu, 103) + ' ' + CONVERT (VARCHAR, L.DateHeureEntrTextu, 108) AS DATETIME) AS DateHeureEntrTextu, 
			A.[N°Assemblage] AS NumAssemblage,
			N.[N°Lingot] AS NumLingot
	FROM	T_LOT L 
				INNER JOIN T_LOT_ASSEMBLAGE A ON L.IdLot = A.IdLot 
				INNER JOIN T_LOT_LINGOT N ON L.IdLot = N.IdLot 
	WHERE   L.DateHeureEntrTextu > CAST('01/11/2016 00:00:01' AS DATETIME)
	AND		N.[N°Lingot] = '0'
),
CDSN_ASSEMBLAGE AS  
(
	-- CDSN : Liste les assemblages postérieurs au 01/01/2016 
	SELECT	CAST([N°Assemblage] AS VARCHAR) AS NumAssemblage, 
			CAST([N°Lingot1] AS VARCHAR) AS NumLingot
	FROM	[SRV-SQL\CDSN].[CDSN].[cdsn_app].[T_ASSEMBLAGE] 
	WHERE	DateCreat > CAST('01/01/2016 00:00:01' AS DATETIME)
)
SELECT S.DateHeureEntrTextu, S.IdLot, S.Lot, S.NumAssemblage , S.NumLingot  , C.NumAssemblage , C.NumLingot 
FROM   SQC_ASSEMBLAGE AS S INNER JOIN CDSN_ASSEMBLAGE C ON S.NumAssemblage = C.NumAssemblage 
ORDER BY S.DateHeureEntrTextu ASC, S.Lot ASC

-- ======================================================================================================
-- OUVERTURE TRANSACTION
-- ======================================================================================================
BEGIN TRANSACTION T_CORRECTIF;

-- ======================================================================================================
-- REQUETE 03 : SUPPRESSION DES LIGNES DE T_LOT_LINGOT POUR LESQUELLES [N°Lingot] = 0
-- ======================================================================================================
WITH 
SQC_ASSEMBLAGE AS
(
	-- SQC : Liste les lots postérieurs au 01/11/2016 pour lesquels le Numero de lingot n'est pas spécifié
	SELECT	DISTINCT 
			L.[IdLot], L.[Lot], 
			CAST(CONVERT (VARCHAR, L.DateHeureEntrTextu, 103) + ' ' + CONVERT (VARCHAR, L.DateHeureEntrTextu, 108) AS DATETIME) AS DateHeureEntrTextu, 
			N.[N°Lingot] AS NumLingot
	FROM	T_LOT L INNER JOIN T_LOT_LINGOT N ON L.IdLot = N.IdLot 
	WHERE   L.DateHeureEntrTextu > CAST('01/11/2016 00:00:01' AS DATETIME)
	AND		N.[N°Lingot] = '0'
)
DELETE FROM T_LOT_LINGOT
WHERE  IdLot  IN (SELECT IdLot FROM SQC_ASSEMBLAGE)
AND		[N°Lingot] = '0'

-- ======================================================================================================
-- REQUETE 04 : CREATION DES LIGNES DE T_LOT_LINGOT POUR LES LOTS POSTERIEURS AU 01/11/2016
-- ======================================================================================================
WITH 
SQC_ASSEMBLAGE AS
(
	-- SQC : Liste les lots postérieurs au 01/11/2016 avec les assemblages associes
	SELECT	DISTINCT 
			L.[IdLot], L.[Lot], 
			CAST(CONVERT (VARCHAR, L.DateHeureEntrTextu, 103) + ' ' + CONVERT (VARCHAR, L.DateHeureEntrTextu, 108) AS DATETIME) AS DateHeureEntrTextu,
			A.[N°Assemblage] AS NumAssemblage
	FROM	T_LOT L INNER JOIN T_LOT_ASSEMBLAGE A ON L.IdLot = A.IdLot 
	WHERE   L.DateHeureEntrTextu > CAST('01/11/2016 00:00:01' AS DATETIME)
),
CDSN_ASSEMBLAGE AS  
(
	-- SQC : Liste les lots postérieurs au 01/11/2016 avec les assemblages associes
	SELECT	CAST([N°Assemblage] AS VARCHAR) AS NumAssemblage, CAST([N°Lingot1] AS VARCHAR) AS NumLingot
	FROM	[SRV-SQL\CDSN].[CDSN].[cdsn_app].[T_ASSEMBLAGE] 
	WHERE	DateCreat > CAST('01/01/2016 00:00:01' AS DATETIME)
)
INSERT INTO T_LOT_LINGOT (IdLot, [N°Lingot])
SELECT	DISTINCT	
		S.IdLot, C.NumLingot 
FROM	SQC_ASSEMBLAGE S INNER JOIN CDSN_ASSEMBLAGE C ON S.NumAssemblage = C.NumAssemblage
WHERE	NOT EXISTS (SELECT * FROM T_LOT_LINGOT WHERE IdLot = S.IdLot AND [N°Lingot] = C.NumLingot)

-- ======================================================================================================
-- VALIDATION TRANSACTION
-- ======================================================================================================
COMMIT TRANSACTION T_CORRECTIF;

-- ======================================================================================================
-- ANNULATION TRANSACTION
-- ======================================================================================================
ROLLBACK TRANSACTION T_CORRECTIF;
