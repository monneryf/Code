-------------------------------------------------------------------------------------

SELECT ROW_NUMBER() OVER (ORDER BY (SELECT NULL)) AS RN
FROM sys.all_columns;

-------------------------------------------------------------------------------------

WITH
TENS (N) AS (SELECT 0 UNION ALL SELECT 0 UNION ALL SELECT 0 UNION ALL
			 SELECT 0 UNION ALL SELECT 0 UNION ALL SELECT 0 UNION ALL
			 SELECT 0 UNION ALL SELECT 0 UNION ALL SELECT 0 UNION ALL SELECT 0),
THOUSANDS (N) AS (SELECT 1 FROM TENS t1 CROSS JOIN TENS t2 CROSS JOIN TENS t3),
MILLIONS (N) AS (SELECT 1 FROM THOUSANDS t1 CROSS JOIN THOUSANDS t2),
TALLY (N) AS (SELECT ROW_NUMBER() OVER (ORDER BY (SELECT 0)) FROM MILLIONS)

SELECT N
	FROM TALLY;

-------------------------------------------------------------------------------------


