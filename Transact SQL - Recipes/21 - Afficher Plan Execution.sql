USE Test;
GO

SET SHOWPLAN_ALL ON;
GO

SELECT A1.*,A2.* FROM [dbo].[Animals] AS A1,
			  [dbo].[Animals] AS A2

;
GO

