# Instruction

## Task 

1. Create a snapshot table for `sales.salesorderheader` called `snp_salesorderheader` 

2. Run the snapshot table once using `dbt snapshot` 

3. For each script in the helper scripts in [../solved/helper/sales_order_header/](../solved/helper/sales_order_header/): 
    - Run the `upgrade` SQL portion of the script 
    - Run `dbt snapshot` 

4. Create an accumulating snapshot fact table called `fct_salesorderheader_accum_snp`

