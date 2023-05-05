1. Compare each film's length to the avg_yearly_length and avg_category_length 

Note: Only first 10 rows being displayed below. 

```
| film_id | title            | release_year | category_name | length | release_year_length | category_length |
| ------- | ---------------- | ------------ | ------------- | ------ | ------------------- | --------------- |
|       1 | Academy Dinosaur |        2,006 | Documentary   |     86 |              115.27 |          108.75 |
|       2 | Ace Goldfinger   |        2,006 | Horror        |     48 |              115.27 |          112.48 |
|       3 | Adaptation Holes |        2,006 | Documentary   |     50 |              115.27 |          108.75 |
|       4 | Affair Prejudice |        2,006 | Horror        |    117 |              115.27 |          112.48 |
|       5 | African Egg      |        2,006 | Family        |    130 |              115.27 |          114.78 |
|       6 | Agent Truman     |        2,006 | Foreign       |    169 |              115.27 |          121.70 |
|       7 | Airplane Sierra  |        2,006 | Comedy        |     62 |              115.27 |          115.83 |
|       8 | Airport Pollock  |        2,006 | Horror        |     54 |              115.27 |          112.48 |
|       9 | Alabama Devil    |        2,006 | Horror        |    114 |              115.27 |          112.48 |
|      10 | Aladdin Calendar |        2,006 | Sports        |     63 |              115.27 |          128.20 |
```

2. now do the same thing using window functions 

Note: Only first 10 rows being displayed below. 

```
| film_id | title            | release_year | category_name | length | release_year_length | category_length |
| ------- | ---------------- | ------------ | ------------- | ------ | ------------------- | --------------- |
|       1 | Academy Dinosaur |        2,006 | Documentary   |     86 |              115.27 |          108.75 |
|       2 | Ace Goldfinger   |        2,006 | Horror        |     48 |              115.27 |          112.48 |
|       3 | Adaptation Holes |        2,006 | Documentary   |     50 |              115.27 |          108.75 |
|       4 | Affair Prejudice |        2,006 | Horror        |    117 |              115.27 |          112.48 |
|       5 | African Egg      |        2,006 | Family        |    130 |              115.27 |          114.78 |
|       6 | Agent Truman     |        2,006 | Foreign       |    169 |              115.27 |          121.70 |
|       7 | Airplane Sierra  |        2,006 | Comedy        |     62 |              115.27 |          115.83 |
|       8 | Airport Pollock  |        2,006 | Horror        |     54 |              115.27 |          112.48 |
|       9 | Alabama Devil    |        2,006 | Horror        |    114 |              115.27 |          112.48 |
|      10 | Aladdin Calendar |        2,006 | Sports        |     63 |              115.27 |          128.20 |
```

3. find each film's length rank within its category 

Note: Only first 10 rows being displayed below. 

```
| film_id | title            | release_year | category_name | length | release_year_length | category_length | length_rank_by_category |
| ------- | ---------------- | ------------ | ------------- | ------ | ------------------- | --------------- | ----------------------- |
|       1 | Academy Dinosaur |        2,006 | Documentary   |     86 |              115.27 |          108.75 |                      44 |
|       2 | Ace Goldfinger   |        2,006 | Horror        |     48 |              115.27 |          112.48 |                      56 |
|       3 | Adaptation Holes |        2,006 | Documentary   |     50 |              115.27 |          108.75 |                      63 |
|       4 | Affair Prejudice |        2,006 | Horror        |    117 |              115.27 |          112.48 |                      26 |
|       5 | African Egg      |        2,006 | Family        |    130 |              115.27 |          114.78 |                      27 |
|       6 | Agent Truman     |        2,006 | Foreign       |    169 |              115.27 |          121.70 |                      15 |
|       7 | Airplane Sierra  |        2,006 | Comedy        |     62 |              115.27 |          115.83 |                      51 |
|       8 | Airport Pollock  |        2,006 | Horror        |     54 |              115.27 |          112.48 |                      54 |
|       9 | Alabama Devil    |        2,006 | Horror        |    114 |              115.27 |          112.48 |                      27 |
|      10 | Aladdin Calendar |        2,006 | Sports        |     63 |              115.27 |          128.20 |                      68 |
```

4. find each film's longest length within its category 

Note: Only first 10 rows being displayed below. 

```
| film_id | title            | release_year | category_name | length | release_year_length | category_length | length_rank_by_category | max_length_by_category |
| ------- | ---------------- | ------------ | ------------- | ------ | ------------------- | --------------- | ----------------------- | ---------------------- |
|       1 | Academy Dinosaur |        2,006 | Documentary   |     86 |              115.27 |          108.75 |                      44 |                    183 |
|       2 | Ace Goldfinger   |        2,006 | Horror        |     48 |              115.27 |          112.48 |                      56 |                    181 |
|       3 | Adaptation Holes |        2,006 | Documentary   |     50 |              115.27 |          108.75 |                      63 |                    183 |
|       4 | Affair Prejudice |        2,006 | Horror        |    117 |              115.27 |          112.48 |                      26 |                    181 |
|       5 | African Egg      |        2,006 | Family        |    130 |              115.27 |          114.78 |                      27 |                    184 |
|       6 | Agent Truman     |        2,006 | Foreign       |    169 |              115.27 |          121.70 |                      15 |                    184 |
|       7 | Airplane Sierra  |        2,006 | Comedy        |     62 |              115.27 |          115.83 |                      51 |                    185 |
|       8 | Airport Pollock  |        2,006 | Horror        |     54 |              115.27 |          112.48 |                      54 |                    181 |
|       9 | Alabama Devil    |        2,006 | Horror        |    114 |              115.27 |          112.48 |                      27 |                    181 |
|      10 | Aladdin Calendar |        2,006 | Sports        |     63 |              115.27 |          128.20 |                      68 |                    184 |
```
