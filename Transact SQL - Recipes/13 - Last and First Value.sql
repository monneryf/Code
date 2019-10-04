SELECT
	[AccountId],
	[TranDate],
	[TranAmt],
	FIRST_VALUE([AccountId]) OVER(PARTITION BY [TranDate] ORDER BY [TranDate]) AS First_Account
FROM
	[dbo].[Transactions]	
ORDER BY
	[TranDate]
	;
	
GO

SELECT
	[AccountId],
	[TranDate],
	[TranAmt],
	LAST_VALUE([AccountId]) OVER(PARTITION BY [TranDate] ORDER BY [TranDate]) AS First_Account
FROM
	[dbo].[Transactions]	
ORDER BY
	[TranDate]
	;
	
GO
			  