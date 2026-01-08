
/* agency_requests.sql */

SELECT
    a.agency AS agency_code,
    a.agency_name,
    COUNT (*) as total_requests
FROM agencies as a
INNER JOIN service_requests as s ON s.agency_id = a.agency_id
WHERE agency_code = 'NYPD'
    OR agency_code = 'FDNY'
    OR agency_code LIKE '%DSNY%'
    OR agency_code LIKE '%DOT%'
    OR agency_code LIKE '%HPD%'
    OR agency_code LIKE '%DEP%'
GROUP BY a.agency_id, a.agency, a.agency_name
HAVING total_requests > 100
ORDER BY -total_requests