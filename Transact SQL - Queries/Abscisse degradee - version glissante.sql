SET DATEFIRST 1;

WITH Data_ AS (
	SELECT
		*,
		DATEDIFF(day,[Date],getdate())-643 as jour,
		
		DATEPART(year,[Date]) as annee,
		DATEPART(quarter,[Date]) as trimestre,
		DATEPART(month,[Date]) as mois,
		DATEPART(week,[Date]) as semaine,
		DATEPART(day,[Date]) as journee,
		
		DATEPART(year,getdate()-644) as annee_jour,
		DATEPART(quarter,getdate()-644) as trimestre_jour,
		DATEPART(month,getdate()-644) as mois_jour,
		DATEPART(week,getdate()-644) as semaine_jour,
		DATEPART(day,getdate()-644) as journee_jour

	FROM
		[dbo].[global_rankings]),
_abscisse AS (
SELECT 
	CASE
		WHEN datediff(year,Data_.[Date],getdate()-644)<=1 AND datediff(quarter,Data_.[Date],getdate()-644)<=1 AND datediff(month,Data_.[Date],getdate()-644)<=1 AND datediff(week,Data_.[Date],getdate()-644)<1 THEN concat(convert(varchar(50),DATEPART(year,Data_.[Date])),' - 04 - ' + ' Jour n° ',dbo.numerator(DATEPART(day,Data_.[Date]),2))
		WHEN datediff(year,Data_.[Date],getdate()-644)<=1 AND datediff(quarter,Data_.[Date],getdate()-644)<=1 AND datediff(month,Data_.[Date],getdate()-644)<=1 THEN concat(convert(varchar(50),DATEPART(year,Data_.[Date])),' - 03 - Semaine n° ',dbo.numerator(DATEPART(week,Data_.[Date]),2))
		WHEN datediff(year,Data_.[Date],getdate()-644)<=1 AND datediff(quarter,Data_.[Date],getdate()-644)<=1 THEN concat(convert(varchar(50),DATEPART(year,Data_.[Date])),' - 02 - Mois n° ',dbo.numerator(DATEPART(month,Data_.[Date]),2))
		WHEN datediff(year,Data_.[Date],getdate()-644)<=1 THEN concat(convert(varchar(50),DATEPART(year,Data_.[Date])),' - 01 - Trimestre n° ',dbo.numerator(DATEPART(quarter,Data_.[Date]),2))
		ELSE concat(convert(varchar(50),DATEPART(year,Data_.[Date])),' - 00 - Année - ',DATEPART(year,Data_.[Date]))
			END AS Abscisse
		,Data_.Date
		,datediff(year,Data_.[Date],getdate()-644) as ann
		,datediff(quarter,Data_.[Date],getdate()-644) as trime
		,datediff(month,Data_.[Date],getdate()-644) as moi
		,datediff(week,Data_.[Date],getdate()-644) as sem
		,Convert(BIGINT,[Streams]) AS strea
	FROM
		Data_)

SELECT 
	a.Abscisse,
	AVG(a.[strea]) AS Total_Stream 
FROM _abscisse as a
	GROUP BY Abscisse
	ORDER BY Abscisse ASC;
GO





