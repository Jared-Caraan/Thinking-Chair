'''
Astronomers at the Intergalactic Observation Network are analyzing telescope logs to identify Earth-like exoplanets — planets whose atmospheres contain the key spectral features associated with habitability and potential life.

Modern exoplanet detection relies on observing absorption lines in starlight that passes through the atmosphere of a planet during transit. These lines appear in telescope data as biosignature codes — identifiers representing specific atmospheric molecules or physical effects.

Examples of biosignature codes found in the logs include:

"O2_ABS" — oxygen absorption
"H2O_VAPOR" — water vapor
"CH4_TRACE" — trace methane
"O3_UV_SHIELD" — ozone ultraviolet absorption
"CO2_BASELINE" — carbon dioxide baseline
"N2_BALANCE" — atmospheric nitrogen stability
"THERMAL_IR" — infrared thermal profile
"DUST_INTERFERENCE" — dust or debris noise
"STELLAR_NOISE" — general stellar contamination
…and many others

To classify a planet candidate as potentially Earth-like, astronomers look for the presence of a well-known biosignature suite associated with habitability:

O2_ABS
H2O_VAPOR
CH4_TRACE
O3_UV_SHIELD
CO2_BASELINE
  
These represent (respectively) oxygen, water vapor, methane, ozone, and CO₂ — a simplified but scientifically recognizable minimal set for Earth-like atmospheric analysis.

Because cosmic noise and transient artifacts can easily produce false positives, astronomers require:

Each required biosignature must appear at least twice (two independent confirmations)
Additional biosignatures are allowed: Real exoplanet atmospheres contain many more signals; these do not disqualify a candidate.
Some spectral combinations correspond to environments entirely incompatible with Earth-like life. One such disqualifying atmospheric set is Runaway Greenhouse (Venus-like):

CO2_SUPERDENSE
SO2_ACIDITY
SULFURIC_CLOUDS

If a planet contains all biosignatures from this set (at least once), it is immediately excluded even if it also contains every required biosignature twice.

A full detection of this set strongly indicates a runaway greenhouse atmosphere — far too hot and acidic for habitability.

Partial matches do not disqualify a planet. All three markers must be present.

We have spectral_logs table:

id (int): primary key
object_id (int): Observed astronomical object
signature (varchar): Detected biosignature code
observed_at (timestamp): Time of detection
  
All rows come from a single day, so no date filtering is required.

Your query must return object_id — ID of each Earth-like candidate planet. And be sorted ascending by object_id.

For this sample data:

 object_id |   signature        |     observed_at
-----------+--------------------+-------------------------
    101    |  O2_ABS            | 2024-06-01 00:01:00
    101    |  O2_ABS            | 2024-06-01 00:03:00
    101    |  H2O_VAPOR         | 2024-06-01 00:04:00
    101    |  H2O_VAPOR         | 2024-06-01 00:05:00
    101    |  CH4_TRACE         | 2024-06-01 00:06:00
    101    |  CH4_TRACE         | 2024-06-01 00:08:00
    101    |  O3_UV_SHIELD      | 2024-06-01 00:10:00
    101    |  O3_UV_SHIELD      | 2024-06-01 00:12:00
    101    |  CO2_BASELINE      | 2024-06-01 00:14:00
    101    |  CO2_BASELINE      | 2024-06-01 00:16:00

Expected output is:

 object_id
-----------
    101

GLHF!
'''

SELECT object_id
FROM spectral_logs
GROUP BY object_id
HAVING 
  -- 1. Must have all 5 required signatures, each appearing at least twice
  COUNT(CASE WHEN signature = 'O2_ABS' THEN 1 END) >= 2 AND
  COUNT(CASE WHEN signature = 'H2O_VAPOR' THEN 1 END) >= 2 AND
  COUNT(CASE WHEN signature = 'CH4_TRACE' THEN 1 END) >= 2 AND
  COUNT(CASE WHEN signature = 'O3_UV_SHIELD' THEN 1 END) >= 2 AND
  COUNT(CASE WHEN signature = 'CO2_BASELINE' THEN 1 END) >= 2
  
  AND 
  
  -- 2. Must NOT have the full "Runaway Greenhouse" set
  -- We check if the count of distinct signatures from the "bad" list is less than 3
  COUNT(DISTINCT CASE WHEN signature IN ('CO2_SUPERDENSE', 'SO2_ACIDITY', 'SULFURIC_CLOUDS') 
                      THEN signature END) < 3
ORDER BY object_id ASC;
