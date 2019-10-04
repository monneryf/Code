WITH hierarchie_company([CompanyID],
						[ParentCompanyID],
						[CompanyName],
						[CompanyLevel]) AS (

	SELECT C1.*,0 AS [CompanyLevel] FROM [dbo].[company] as C1 WHERE C1.[ParentCompanyID] IS NULL
	UNION ALL
	SELECT C3.*,C2.[CompanyLevel]+1 
		FROM hierarchie_company as C2 
			INNER JOIN [dbo].[company] AS C3
			ON C3.[ParentCompanyID] = C2.[CompanyID])

SELECT * FROM hierarchie_company;

GO



