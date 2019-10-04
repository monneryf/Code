SELECT
	[AccountId],
	[TranDate],
	[TranAmt],
	ROW_NUMBER() OVER(PARTITION BY [AccountId] ORDER BY [TranDate] ASC) AS Number_Transaction
FROM
	[dbo].[Transactions]
ORDER BY
	[AccountId] DESC,
	[TranDate]
;
GO


