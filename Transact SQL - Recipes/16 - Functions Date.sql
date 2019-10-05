SELECT 'GETDATE()' AS [Function], GETDATE() AS [Value];
SELECT 'CURRENT_TIMESTAMP'AS [Function], CURRENT_TIMESTAMP AS [Value];
SELECT 'GETUTCDATE()' AS [Function], GETUTCDATE() AS [Value];
SELECT 'SYSDATETIME()' AS [Function], SYSDATETIME() AS [Value];
SELECT 'SYSUTCDATETIME()' AS [Function], SYSUTCDATETIME() AS [Value];
SELECT 'SYSDATETIMEOFFSET()' AS [Function], SYSDATETIMEOFFSET() AS [Value];

GO

SELECT DATEADD(YEAR, -1, '2009-04-02T00:00:00');
GO

SELECT DATEDIFF(day,[TranDate],getdate())
FROM [dbo].[Transactions];
GO

SELECT 
	DATENAME(MONTH,[TranDate]),
	DATENAME(WEEKDAY,[TranDate])
FROM [dbo].[Transactions];
GO

SELECT 
	DATEPART(YEAR,[TranDate]) As Year,
	DATEPART(MONTH,[TranDate]) As Month,
	DATEPART(DAY,[TranDate]) As Day
FROM
	[dbo].[Transactions]
GO

SELECT 
	MyData ,
	ISDATE(MyData) AS IsADate
FROM 
	(VALUES
	('IsThisADate'),
	('2012-02-14'),
	('2012-01-01T00:00:00'),
	('2012-12-31T23:59:59.9999999')) dt(MyData);

	GO

SELECT
	[TranDate],
	EOMONTH([TranDate]) As Fin_Mois
FROM
	[dbo].[Transactions]
GO

SELECT TIMEFROMPARTS(18, 25, 32, 5, 1);
SELECT TIMEFROMPARTS(18, 25, 32, 5, 2);
SELECT TIMEFROMPARTS(18, 25, 32, 5, 3);

GO

SELECT MyDate,
DATETIMEFROMPARTS(TrDate.Annee, 1, 1, 0, 0, 0, 0) AS FirstDayOfYear,
DATETIMEFROMPARTS(TrDate.Annee, TrDate.Mois, 1, 0, 0, 0, 0) AS FirstDayOfMonth,
DATETIMEFROMPARTS(TrDate.Annee, TrDate.Trimestre, 1, 0, 0, 0, 0) AS FirstDayOfQuarter
FROM 
	(VALUES 
	('1981-01-17T00:00:00'),
	('1961-11-23T00:00:00'),
	('1960-07-09T00:00:00'),
	('1980-07-11T00:00:00'),
	('1983-01-05T00:00:00'),
	('2006-11-27T00:00:00')) dt (MyDate)
CROSS APPLY (SELECT DATEPART(YEAR, dt.MyDate) AS Annee,
					DATEPART(MONTH, dt.MyDate) AS Mois,
					((CEILING(MONTH(dt.MyDate)/3.0)*3)-2) AS Trimestre
) TrDate;
;

GO


SELECT 
	TR.[TranDate],
	DATETIMEFROMPARTS(2019,10,09,01,15,12,0) as SomeDate,
	DATETIMEFROMPARTS(TrDate.Annee, 1, 1, 0, 0, 0, 0) AS FirstDayOfYear,
	DATETIMEFROMPARTS(TrDate.Annee, TrDate.Mois, 1, 0, 0, 0, 0) AS FirstDayOfMonth,
	DATETIMEFROMPARTS(TrDate.Annee, TrDate.Trimestre, 1, 0, 0, 0, 0) AS FirstDayOfQuarter
FROM 
	[dbo].[Transactions] As TR
	
	CROSS APPLY (SELECT DATEPART(YEAR, TR.TranDate) AS Annee,
						DATEPART(MONTH, TR.TranDate) AS Mois,
						((CEILING(MONTH(TR.TranDate)/3.0)*3)-2) AS Trimestre
	) TrDate;
;

GO












