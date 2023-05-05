1. calculate the cumulative sum of sales by month for each payment 

```
| payment_id | payment_date               | payment_year_month | amount | cumulative_sales |
| ---------- | -------------------------- | ------------------ | ------ | ---------------- |
| 17793      | 2007-02-14 21:21:59.996577 | 2007-2             | 2.99   | 2.99             |
| 18173      | 2007-02-14 21:23:39.996577 | 2007-2             | 4.99   | 7.98             |
| 19399      | 2007-02-14 21:29:00.996577 | 2007-2             | 4.99   | 12.97            |
| 18441      | 2007-02-14 21:41:12.996577 | 2007-2             | 6.99   | 19.96            |
| 18698      | 2007-02-14 21:44:52.996577 | 2007-2             | 0.99   | 20.95            |
| 19498      | 2007-02-14 21:44:53.996577 | 2007-2             | 3.99   | 24.94            |
| 18686      | 2007-02-14 21:45:29.996577 | 2007-2             | 4.99   | 29.93            |
| 18051      | 2007-02-14 22:03:35.996577 | 2007-2             | 2.99   | 32.92            |
| 19036      | 2007-02-14 22:11:22.996577 | 2007-2             | 2.99   | 35.91            |
| 18456      | 2007-02-14 22:16:01.996577 | 2007-2             | 2.99   | 38.90            |
```

2. for each film, show the most popular film in each category based on the number of rentals 

```
| film_id | title              | category_name | most_popular_film_in_category |
| ------- | ------------------ | ------------- | ----------------------------- |
| 659     | Park Citizen       | Action        | Rugrats Shakespeare           |
| 126     | Casualties Encino  | Action        | Rugrats Shakespeare           |
| 594     | Montezuma Command  | Action        | Rugrats Shakespeare           |
| 375     | Grail Frankenstein | Action        | Rugrats Shakespeare           |
| 29      | Antitrust Tomatoes | Action        | Rugrats Shakespeare           |
| 549     | Magnolia Forrester | Action        | Rugrats Shakespeare           |
| 250     | Dragon Squad       | Action        | Rugrats Shakespeare           |
| 530     | Lord Arizona       | Action        | Rugrats Shakespeare           |
| 210     | Darko Dorado       | Action        | Rugrats Shakespeare           |
| 371     | Gosford Donnie     | Action        | Rugrats Shakespeare           |
```
