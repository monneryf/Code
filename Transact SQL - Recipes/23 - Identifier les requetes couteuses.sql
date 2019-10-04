USE Test;
GO

SELECT TOP 2
	wait_type, 
	wait_time_ms 
FROM 
	sys.dm_os_wait_stats 

WHERE wait_type NOT IN
			('LAZYWRITER_SLEEP', 
			'SQLTRACE_BUFFER_FLUSH', 
			'REQUEST_FOR_DEADLOCK_SEARCH', 
			'LOGMGR_QUEUE',
			'CHECKPOINT_QUEUE', 
			'CLR_AUTO_EVENT',
			'WAITFOR', 
			'BROKER_TASK_STOP', 
			'SLEEP_TASK', 
			'BROKER_TO_
			FLUSH')
ORDER BY wait_time_ms DESC;

GO

