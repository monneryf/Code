ALTER PROCEDURE COMPTEUR(@Reptile VARCHAR(50)) AS
	
	DECLARE @Nombre INT
	DECLARE @Name VARCHAR(250)
	DECLARE @Phrase VARCHAR(250)
	DECLARE CURS cursor forward_only
	FOR
		SELECT C1.Nom
			FROM [dbo].[Animals] AS C1,
				 [dbo].[Animals] AS C2;

	SET @Nombre = 0;

	OPEN CURS
	 FETCH CURS INTO @Name
	 WHILE(@@FETCH_STATUS=0)
		BEGIN
			IF @Name = @Reptile BEGIN SELECT @Nombre = @Nombre+1 END
			FETCH CURS INTO @Name
		END
	CLOSE CURS;
	DEALLOCATE CURS;
	
	SELECT @Phrase = 'Le nombre occurrence de ' + @Reptile + ' est de : ' + CAST(@Nombre AS VARCHAR(50))
	PRINT @Phrase

GO

EXEC COMPTEUR 'Crocodile';

GO




