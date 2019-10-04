WITH Organigramme AS (
	SELECT H.* FROM [dbo].[Hierarchie] AS H WHERE H.[ParendID] IS NULL
	UNION ALL
	SELECT G.* FROM [dbo].[Hierarchie] as G INNER JOIN Organigramme AS O ON G.[ParendID] = O.[PersonID]
	) 
SELECT * FROM Organigramme;

GO

---------------------------------------------------------------------------------------------------------------------------
---------------------------------------------------------------------------------------------------------------------------

WITH    q AS 
        (
        SELECT  m.*, CAST(ROW_NUMBER() OVER (ORDER BY m.PersonId) AS VARCHAR(MAX)) COLLATE Latin1_General_BIN AS bc
        FROM    mytable m
        WHERE   ParentID IS NULL
        UNION ALL
        SELECT  m.*,  q.bc + '.' + CAST(ROW_NUMBER() OVER (PARTITION BY m.ParentID ORDER BY m.PersonID) AS VARCHAR(MAX)) COLLATE Latin1_General_BIN
        FROM    mytable m
        JOIN    q
        ON      m.parentID = q.PersonID
        )
SELECT  *
FROM    q
ORDER BY
        bc
		

---------------------------------------------------------------------------------------------------------------------------
---------------------------------------------------------------------------------------------------------------------------

DECLARE @Table TABLE(
        PersonID INT,
        Initials VARCHAR(20),
        ParentID INT
)

INSERT INTO @Table SELECT     1,'CJ',NULL
INSERT INTO @Table SELECT     2,'EB',1
INSERT INTO @Table SELECT     3,'MB',1
INSERT INTO @Table SELECT     4,'SW',2
INSERT INTO @Table SELECT     5,'YT',NULL
INSERT INTO @Table SELECT     6,'IS',5

DECLARE @PersonID INT

SELECT @PersonID = 1

;WITH Selects AS (
        SELECT *
        FROM    @Table
        WHERE   PersonID = @PersonID
        UNION ALL
        SELECT  t.*
        FROM    @Table t INNER JOIN
                Selects s ON t.ParentID = s.PersonID
)
SELECT  *
FROm    Selects

		