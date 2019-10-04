SELECT 
	   filename,
	   REVERSE(filename),
	   Path = LEFT(filename, 
				   LEN(filename) - CHARINDEX('\', REVERSE(filename)) + 1),
	   
	   FileName = RIGHT(filename, 
				        CHARINDEX('\', REVERSE(filename)) - 1)

FROM 
	
	sys.sysfiles 
;

GO


