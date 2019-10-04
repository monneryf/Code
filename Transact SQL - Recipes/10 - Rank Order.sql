SELECT
	[AccountId],
	[TranDate],
	[TranAmt],
	RANK() OVER(PARTITION BY [AccountId] ORDER BY [TranAmt] DESC) AS Rank_Amount
FROM
	[dbo].[Transactions]
ORDER BY
	Rank_Amount ASC,
	[AccountId]
;

GO

SELECT
	[AccountId],
	[TranDate],
	[TranAmt],
	DENSE_RANK() OVER(ORDER BY [TranAmt] DESC) AS Rank_Amount
FROM
	[dbo].[Transactions]
ORDER BY
	Rank_Amount ASC,
	[AccountId]
;

GO
