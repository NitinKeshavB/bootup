-- example data
create or replace table car_sales
(
  src variant
)
as
select parse_json(column1) as src
from values
('{
    "date" : "2017-04-28",
    "dealership" : "Valley View Auto Sales",
    "salesperson" : {
      "id": "55",
      "name": "Frank Beasley"
    },
    "customer" : [
      {"name": "Joyce Ridgely", "phone": "16504378889", "address": "San Francisco, CA"}
    ],
    "vehicle" : [
      {"make": "Honda", "model": "Civic", "year": "2017", "price": "20275", "extras":["ext warranty", "paint protection"]}
    ]
}'),
('{
    "date" : "2017-04-28",
    "dealership" : "Tindel Toyota",
    "salesperson" : {
      "id": "274",
      "name": "Greg Northrup"
    },
    "customer" : [
      {"name": "Bradley Greenbloom", "phone": "12127593751", "address": "New York, NY"}
    ],
    "vehicle" : [
      {"make": "Toyota", "model": "Camry", "year": "2017", "price": "23500", "extras":["ext warranty", "rust proofing", "fabric protection"]}
    ]
}') v;

-- select and see
select * from HR.SOURCE.CAR_SALES;
-- get the dealerships
select
    src:dealership
from HR.SOURCE.CAR_SALES;
-- get the dealerships as string
select
    src:dealership::varchar
from HR.SOURCE.CAR_SALES;
-- get salespersons' name using . or []
select
    src:salesperson.name
from HR.SOURCE.CAR_SALES;

select
    src['salesperson']['name']
from HR.SOURCE.CAR_SALES;
-- get customer name and vehicle details
select
    src:customer[0].name, src:vehicle[0]
from HR.SOURCE.CAR_SALES;
-- get make, model and extras
select
  vm.value:make::string as make,
  vm.value:model::string as model,
  ve.value::string as "Extras Purchased"
from HR.SOURCE.CAR_SALES
    , lateral flatten(input => src:vehicle) vm
    , lateral flatten(input => vm.value:extras) ve
;