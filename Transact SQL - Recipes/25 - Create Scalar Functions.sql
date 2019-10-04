Use Test;
GO

CREATE FUNCTION dbo.Maximum (@Nombre1 INT,@Nombre2 INT)
RETURNS INT
AS
	BEGIN
		DECLARE @Maxi INT;

		IF @Nombre1 >= @Nombre2 
			BEGIN
				SELECT @Maxi = @Nombre1
			END
		ELSE
			BEGIN
				SELECT @Maxi = @Nombre2
			END

		RETURN @MAXI
	END

USE Test;
GO

SELECT 
	[Position],
	[Streams],
	[stream],
	[dbo].[Maximum]([Streams],[stream]) AS Max1,
	[dbo].[Maximum]([Streams],[Position]) AS Max2
FROM
	[dbo].[global_rankings]
GO


		



