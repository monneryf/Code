SELECT
	[AccountId],
	[TranDate],
	[TranAmt],
	NTILE(3) OVER(ORDER BY [TranAmt] DESC) AS Amount_Category
FROM
	[dbo].[Transactions]
ORDER BY
	Amount_Category ASC,
	[AccountId]
;

GO

