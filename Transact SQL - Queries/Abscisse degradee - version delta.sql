WITH Data_ AS (
	SELECT
		*,
		DATEDIFF(day,[Date],getdate())-643 as jour
	FROM
		[dbo].[global_rankings]),
_abscisse AS (
SELECT 
	CASE
		WHEN Data_.jour<=7 THEN concat(convert(varchar(50),DATEPART(year,Data_.[Date])),' - 04 - ' + ' Jour n° ',dbo.numerator(DATEPART(day,Data_.[Date]),2))
		WHEN Data_.jour<=60 THEN concat(convert(varchar(50),DATEPART(year,Data_.[Date])),' - 03 - Semaine n° ',dbo.numerator(DATEPART(week,Data_.[Date]),2))
		WHEN Data_.jour<=360 THEN concat(convert(varchar(50),DATEPART(year,Data_.[Date])),' - 02 - Mois n° ',dbo.numerator(DATEPART(month,Data_.[Date]),2))
		ELSE concat(convert(varchar(50),DATEPART(year,Data_.[Date])),' - 01 - Année - ',DATEPART(year,Data_.[Date]))
			END AS Abscisse
		,Data_.Date
		,Convert(BIGINT,[Streams]) AS strea
	FROM
		Data_)

SELECT 
	a.Abscisse,
	SUM(a.[strea]) AS Total_Stream 
FROM _abscisse as a
	GROUP BY Abscisse
	ORDER BY Abscisse ASC;
GO



