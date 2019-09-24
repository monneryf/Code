## 1. Introducing Joins ##

SELECT f.*,c.*
FROM facts as f INNER JOIN
cities as c 
ON f.id = c.facts_id
LIMIT 10;







## 2. Understanding Inner Joins ##

SELECT c.*,f.name country_name
FROM cities as c
INNER JOIN
facts as f 
on c.facts_id  = f.id
LIMIT 5


## 3. Practicing Inner Joins ##

SELECT f.name country, c.name capital_city FROM cities c
INNER JOIN facts f ON f.id = c.facts_id
WHERE c.capital = 1

## 4. Left Joins ##

SELECT f.name country, f.population population 
FROM facts f
LEFT JOIN cities c 
ON c.facts_id = f.id

Where c.population IS NULL;








## 6. Finding the Most Populous Capital Cities ##

Select c.name capital_city, f.name country,c.population population
from cities as c
inner join facts as f
on c.facts_id = f.id
where capital = 1
Order by c.population desc
limit 10



## 7. Combining Joins with Subqueries ##

SELECT c.name capital_city,f.name country,c.population population
FROM facts as f
inner JOIN
(select * from cities where population>10000000 and capital =1) as c
on f.id = c.facts_id
order by population DESC



## 8. Challenge: Complex Query with Joins and Subqueries ##

select f.name country,
    s.urban_pop urban_pop, 
    f.population total_pop,
    ((s.urban_pop +0.0) / (population +0.0)) AS urban_pct
    
    from facts as f
    inner join 
        (SELECT facts_id,SUM(population) as urban_pop 
         FROM cities group by facts_id) as s
     on f.id = s.facts_id
     WHERE urban_pct > 0.5
     order by urban_pct ASC
     
     
    