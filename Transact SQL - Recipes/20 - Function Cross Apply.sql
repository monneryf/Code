SELECT 
	r.session_id, 
	r.status, 
	r.start_time, 
	r.command, 
	s.text
FROM sys.dm_exec_requests r
	CROSS APPLY sys.dm_exec_sql_text(r.sql_handle) s

WHERE r.status = 'running';

GO

