
/* agency_load_analysis.sql */
-- Find agencies with volume higher than the city-wide average
SELECT 
    a.agency_name,
    COUNT(s.agency_id) AS total_requests,
    -- ADVANCED: Window function to get city-wide total for percentage calculation
    ROUND(100.0 * COUNT(s.agency_id) / SUM(COUNT(s.agency_id)) OVER (), 2) AS percent_of_city_volume,
    -- ADVANCED: Ranking agencies by volume
    RANK() OVER (ORDER BY COUNT(s.agency_id) DESC) as volume_rank
FROM agencies a
JOIN service_requests s ON a.agency_id = s.agency_id
GROUP BY a.agency_id, a.agency_name
ORDER BY volume_rank;