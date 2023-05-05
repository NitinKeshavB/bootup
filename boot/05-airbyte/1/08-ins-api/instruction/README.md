# Instruction

## Concept 

Airbyte supports integration for APIs as well. 

The same sync modes that we covered off earlier for databases, are also supported with APIs. 

###  Sync modes 
- Source: Full Refresh | Destination: Overwrite 
- Source: Incremental | Destination: Append
- Source: Incremental | Destination: De-duped + history 
- Source: Full refresh | Destination: Append

#### Source: Full Refresh | Destination: Overwrite 

![images/full-refresh-overwrite-day1.png](images/full-refresh-overwrite-day1.png)

![images/full-refresh-overwrite-day2.png](images/full-refresh-overwrite-day2.png)

#### Incremental | Destination: Append

![images/incremental-append-day1.png](images/incremental-append-day1.png)

![images/incremental-append-day2.png](images/incremental-append-day2.png)

Note: 
- The API needs to support querying data with a cursor i.e. date or datetime. If the API does not provide that support, then you would have to resort to full refreshes. 

## Task 

### Open Weather API 


#### Source 

1. Create a new source
2. Select "OpenWeather" 
3. Provide latitude, longitude, and app id
4. Set up source

#### Destination 

Use the existing postgres `dw` that has already been set up. 

#### Connection

1. Create new connection 
2. Set Sync mode: `Incremental | Append` 
3. Create connection

We are able to use this sync mode because each time the connector runs, it retrieves the latest weather. 

Note: There may be duplicates if the connection is run twice within a very short window. We may have to use de-duped to remove duplicates using the primary key `id` and `dt`. 
