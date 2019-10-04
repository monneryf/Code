USE Test
GO

CREATE TABLE dbo.company
	(CompanyID INT NOT NULL PRIMARY KEY,
	 ParentCompanyID INT NULL,
	 CompanyName VARCHAR(25) NOT NULL)

GO

INSERT dbo.Company
	(CompanyID, ParentCompanyID, CompanyName)
VALUES 
	(1, NULL, 'Mega-Corp'),
	(2, 1, 'Mediamus-Corp'),
	(3, 1, 'KindaBigus-Corp'),
	(4, 3, 'GettinSmaller-Corp'),
	(5, 4, 'Smallest-Corp'),
	(6, 5, 'Puny-Corp'),
	(7, 5, 'Small2-Corp');


	  