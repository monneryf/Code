WITH CUMUL ([TranDate],[TOTAL]) AS(
		SELECT
			[TranDate],
			SUM([TranAmt]) AS TOTAL
		FROM
			[dbo].[Transactions]
		GROUP BY
			[TranDate]
			)

SELECT
	C.[TranDate],
	C.[TOTAL],
	LAG(C.[TOTAL],1) OVER(ORDER BY C.[TranDate]) AS RECETTE_VEILLE,
	LAG(C.[TOTAL],2) OVER(ORDER BY C.[TranDate]) AS RECETTE_AVANT_VEILLE
FROM
	CUMUL as C
;

GO


