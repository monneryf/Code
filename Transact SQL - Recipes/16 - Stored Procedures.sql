ALTER procedure [dbo].[New_Animal](@Lieu VARCHAR(100)) as

	DECLARE @newName VARCHAR(100);
	DECLARE @NewID INT;

	SELECT @NewID = MAX(idAnimal) FROM [dbo].[Animals];

	SELECT @newName = 
				substring(Nom,CAST(len(Nom)/2 AS INT)+1,len(nom))
				+
				substring(Nom,1,CAST(len(Nom)/2 AS INT))
	
			FROM [dbo].[Animals] 
			WHERE idAnimal=@NewID
			ORDER BY idAnimal DESC;

	INSERT INTO dbo.animals 
				(Nom,Lieu)
				VALUES
				(@newName,@Lieu);

GO

EXEC [dbo].[New_Animal] 'Prairie humide'
GO



