# Instruction

## Concept

### Data types
Snowflake supports all the usual data types
- numeric
- string and binary
- logical
- date & time
- semi-structured
- geospatial

Among these, semi-structured data types are quite special and useful:
- variant - stores any other data type (like a Pokémon Ditto, it transforms into anything else)
- object - equivalent of JSON Object
- array - equivalent of JSON Array or in fact array of any type

![](images/ditto.jpg)


### Notations
- `::` cast data types
- `:` first level element
- `.` traverse down a path
- `[]` traverse down a path
- `FLATTEN`: table function that returns a row for each object in an array
- `LATTERAL`: modifier that joins the data with any information outside the object

## Task
1. load example data
2. select and see 
3. get the dealerships 
4. get the dealerships as string 
5. get salespersons' name using `.` and `[]`
6. get customer name and vehicle details 
7. get make, model and extras using `FLATTEN` and `LATTERAL`
