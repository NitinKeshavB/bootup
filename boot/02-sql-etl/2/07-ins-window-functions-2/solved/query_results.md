1. compute a cumulative sum : calculate the cumulative sum of sales for each payment 

```
| payment_id | payment_date               | amount | cumulative_sales |
| ---------- | -------------------------- | ------ | ---------------- |
| 17793      | 2007-02-14 21:21:59.996577 | 2.99   | 2.99             |
| 18173      | 2007-02-14 21:23:39.996577 | 4.99   | 7.98             |
| 19399      | 2007-02-14 21:29:00.996577 | 4.99   | 12.97            |
| 18441      | 2007-02-14 21:41:12.996577 | 6.99   | 19.96            |
| 18698      | 2007-02-14 21:44:52.996577 | 0.99   | 20.95            |
| 19498      | 2007-02-14 21:44:53.996577 | 3.99   | 24.94            |
| 18686      | 2007-02-14 21:45:29.996577 | 4.99   | 29.93            |
| 18051      | 2007-02-14 22:03:35.996577 | 2.99   | 32.92            |
| 19036      | 2007-02-14 22:11:22.996577 | 2.99   | 35.91            |
| 18456      | 2007-02-14 22:16:01.996577 | 2.99   | 38.90            |
```

2. get the most popular item in each category : for each customer, show the most highest spending customer in each country based on the sales amount

```
| customer_id | full_name        | sales  | country        | highest_spending_customer_in_country |
| ----------- | ---------------- | ------ | -------------- | ------------------------------------ |
| 218         | Vera Mccoy       | 67.82  | Afghanistan    | Vera Mccoy                           |
| 441         | Mario Cheatham   | 107.73 | Algeria        | Judy Gray                            |
| 176         | June Carroll     | 151.68 | Algeria        | Judy Gray                            |
| 69          | Judy Gray        | 89.77  | Algeria        | Judy Gray                            |
| 320         | Anthony Schwab   | 47.85  | American Samoa | Anthony Schwab                       |
| 383         | Martin Bales     | 93.75  | Angola         | Martin Bales                         |
| 528         | Claude Herzog    | 93.80  | Angola         | Martin Bales                         |
| 381         | Bobby Boudreau   | 99.68  | Anguilla       | Bobby Boudreau                       |
| 89          | Julia Flores     | 124.71 | Argentina      | Darryl Ashcraft                      |
| 560         | Jordan Archuleta | 129.71 | Argentina      | Darryl Ashcraft                      |
```

