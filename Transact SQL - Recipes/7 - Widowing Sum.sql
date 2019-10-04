SELECT 
	[AccountId],
	[TranDate],
	[TranAmt],
	SUM([TranAmt]) OVER(PARTITION BY [AccountId] ORDER BY [TranDate] ROWS BETWEEN 2 PRECEDING AND CURRENT ROW) AS SUM_THREE
FROM
	[dbo].[Transactions]
ORDER BY
	[AccountId],
	[TranDate]
;
GO


