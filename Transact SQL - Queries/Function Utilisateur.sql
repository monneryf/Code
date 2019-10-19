CREATE FUNCTION dbo.Numerator(@Numero INT,@Gabarit INT)
	RETURNS VARCHAR(10)
	BEGIN
		DECLARE @Chiffre VARCHAR(10)
		SET @Chiffre = CONVERT(VARCHAR(10),@Numero)

		WHILE(LEN(@Chiffre)<@Gabarit)
			BEGIN
				SET @Chiffre = CONCAT('0',@Chiffre)
			END

		RETURN @Chiffre
	END

