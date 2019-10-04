DBCC FREEPROCCACHE;
GO

USE Test;
GO

SELECT A1.*,A2.* FROM [dbo].[Animals] AS A1,
			  [dbo].[Animals] AS A2
;

SELECT t.text,
	st.total_logical_reads,
	st.total_physical_reads,
	st.total_elapsed_time/1000000 Total_Time_Secs,
	st.total_logical_writes
FROM 
	sys.dm_exec_query_stats st
	CROSS APPLY sys.dm_exec_sql_text(st.sql_handle) t
	;
GO


