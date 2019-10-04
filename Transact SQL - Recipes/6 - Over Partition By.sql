SELECT 
	[AccountId],
	[TranDate],
	[TranAmt],
	SUM([TranAmt]) OVER(PARTITION BY [AccountId] ORDER BY [TranDate]) AS Cumul,
	AVG([TranAmt]) OVER(PARTITION BY [AccountId] ORDER BY [TranDate]) AS Moyenne,
	COUNT([TranAmt]) OVER(PARTITION BY [AccountId] ORDER BY [TranDate]) AS Nombre,
	MAX([TranAmt]) OVER(PARTITION BY [AccountId] ORDER BY [TranDate]) AS Maximum,
	MIN([TranAmt]) OVER(PARTITION BY [AccountId] ORDER BY [TranDate]) AS Minimum
FROM
	[dbo].[Transactions]
ORDER BY
	[AccountId],
	[TranDate]
;
GO



