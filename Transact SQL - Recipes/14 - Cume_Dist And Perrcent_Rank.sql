SELECT
	[AccountId],
	[TranDate],
	[TranAmt],
	CUME_DIST() OVER(ORDER BY [TranAmt]) AS Palmares,
	PERCENT_RANK() OVER(ORDER BY [TranAmt]) AS Palmares_Percent

FROM
	[dbo].[Transactions]
		
ORDER BY
	[TranAmt]
	;
	
GO
