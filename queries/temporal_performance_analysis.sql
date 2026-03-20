
/* temporal_performance_analysis.sql */
SELECT 
    a.agency AS agency_code,
    strftime('%Y-%m', s.created_date) AS request_month,
    COUNT(*) AS monthly_requests,
    ROUND(AVG(julianday(s.closed_date) - julianday(s.created_date)), 2) AS avg_resolution_days,
    
    RANK() OVER (
        PARTITION BY strftime('%Y-%m', s.created_date) 
        ORDER BY AVG(julianday(s.closed_date) - julianday(s.created_date)) ASC
    ) as speed_rank

FROM agencies AS a
INNER JOIN service_requests AS s ON s.agency_id = a.agency_id
WHERE s.status = 'Closed'
GROUP BY 1, 2
HAVING monthly_requests >= 5
ORDER BY request_month DESC, speed_rank ASC;
