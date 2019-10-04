SELECT StudentId,
CHECKSUM_AGG(Grade) AS GradeChecksumAgg
FROM (VALUES (1, 100),
(1, 100),
(1, 100),
(1, 99),
(1, 99),
(1, 98),
(1, 98),
(1, 95),
(1, 95),
(1, 95)
) dt (StudentId, Grade)
GROUP BY StudentID;

SELECT StudentId,
CHECKSUM_AGG(Grade) AS GradeChecksumAgg
FROM (VALUES (1, 100),
(1, 100),
(1, 100),
(1, 99),
(1, 99),
(1, 98),
(1, 98),
(1, 95),
(1, 95),
(1, 90)
) dt (StudentId, Grade)
GROUP BY StudentID;

