# Data Quality check

Data quality is decomposed into:

- (1) Data Integrity
- (2) Data Fitness

While `(2) Data Fitness` evaluation needs more business sense and more varied cases by base, `(1) Data Integrity` is relatively more framework and recipe-based.

Below is a basic checklist to assess the Data Integrity. 

> **Disclaimer:** Not include steps of EDA - checking distribution, outliers, multivariate relationships.

| Factor                      | Description                                                     | SQL/Pandas code                  |
|-----------------------------|-----------------------------------------------------------------|----------------------------------|
| Timeliness/Historical       | Check the time window of data, the latest time?                 | MIN(date) \| MAX(date)           |
| Completeness                | Count the records over time windows or all categories available | COUNT(*) GROUP BY date\|category |
| Completeness (Missing rate) | Calculate missing rate of key columns                           | COUNT(col) / COUNT(*)            |
| Well-annotation             | Check the values and name of columns / data descriptions        | COUNT(*) GROUP BY \| WHERE       |
| Consistency                 | Same units (check range of values), data types                  | df.describe(), df.info()         |
| Linkage-Granularity         | Check the ids that make each row unique                         | COUNT(DISTINCT id)               |
| Linkage-Mapping             | Dimensionally structure? Keys to map data?                      | INNER JOIN                       |