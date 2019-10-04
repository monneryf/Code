SELECT DISTINCT
	SOUNDEX([Nom]) AS Hash_Nom,
	SOUNDEX('Alli') AS Hash_Alli,
	[Nom]

FROM [dbo].[Animals] 

WHERE SOUNDEX([Nom]) >= SOUNDEX('Alligator');


