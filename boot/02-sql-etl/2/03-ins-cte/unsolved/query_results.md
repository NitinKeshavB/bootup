1. show the top 10 customers based on average amount spent per rental, and their total_rental and total_amount_spent figures 

Note: same query as Q4 of the previous activity. You will need to refactor the existing query using CTEs. 

```
| first_name | last_name | avg_spent_per_rental | amount_spent | number_of_rentals |
| ---------- | --------- | -------------------- | ------------ | ----------------- |
| Brittany   | Riley     | 5.42                 | 151.73       | 28                |
| Marshall   | Thorn     | 5.12                 | 117.77       | 23                |
| Linda      | Williams  | 5.03                 | 130.76       | 26                |
| Kent       | Arsenault | 4.99                 | 134.73       | 27                |
| Marion     | Snyder    | 4.99                 | 194.61       | 39                |
| Gordon     | Allard    | 4.93                 | 157.69       | 32                |
| Ana        | Bradley   | 4.93                 | 167.67       | 34                |
| Rhonda     | Kennedy   | 4.91                 | 191.62       | 39                |
| Perry      | Swafford  | 4.91                 | 117.76       | 24                |
| Arnold     | Havens    | 4.90                 | 161.68       | 33                |
```