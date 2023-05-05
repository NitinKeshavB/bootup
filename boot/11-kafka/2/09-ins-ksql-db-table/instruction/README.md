# Creating a KSQL db table

As we've covered previously, a KSQLdb table is quite different to a stream.

A stream contains the history of each key whereas a table contains the latest snapshot of that key.

Here's a classic weather example of a stream vs table.

**A stream will look like this**

| city (KEY) | temp |
|------------|------|
| SYD        | 8    |
| SYD        | 10   |
| SYD        | 14   |
| SYD        | 16   |
| SYD        | 17   |
| SYD        | 20   |
| SYD        | 24   |
| SYD        | 22   |
| SYD        | 19   |
| SYD        | 17   |
| SYD        | 15   |


Whereas a table created with the same schema with the key as the `city` will just have one row

| city (KEY) | temp |
|------------|------|
| SYD        | 15   |


You may need to set run `SET 'auto.offset.reset' = 'earliest';`

---

## General Instruction
1. Run the provided producer on the `temperature.json` file, it matches the schema above. It will create the `key` as the `city`.
2. Create a stream which matches the above schema
3. To get used to the dataset, try to optionally answer the following questions.
   1. What is the hottest temperature each city has experienced? 
   2. What is the average temperature of each of these cities?

4. Create a table now
   1. How many records do you see in the table? Why do you see those records only?
