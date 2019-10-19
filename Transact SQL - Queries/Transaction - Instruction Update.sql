BEGIN Transaction
	DECLARE @Nb_Row INT;
	SELECT @Nb_Row = COUNT(*) FROM dbo.Movies WHERE [Family]='';
	print('Nombre de ligne inititale ' + convert(VARCHAR(50),@Nb_Row));

	UPDATE dbo.Movies
		SET Family='Foreign'
		WHERE Family='';

	IF @@ROWCOUNT = @Nb_Row 
		BEGIN
			PRINT('Nombre de lignes modifiées ' + convert(VARCHAR(50),@@ROWCOUNT))
			COMMIT;
		END
	ELSE
		BEGIN
			PRINT('Nombre de lignes modifiées incorrectes - Transaction annulée !!!')
			ROLLBACK;
		END

GO


