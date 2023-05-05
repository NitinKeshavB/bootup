# Instruction

## Task 

1. Create a snapshot table for `purchasing.purchaseorderheader` called `snp_purchaseorderheader` 

2. Run the snapshot table once using `dbt snapshot` 

3. For each script in the helper scripts in [../solved/helper/purchasing/](../solved/helper/purchasing/): 
    - Run the `upgrade` SQL portion of the script 
    - Run `dbt snapshot` 

4. Create an accumulating snapshot fact table called `fct_purchaseorderheader_accum_snp`

