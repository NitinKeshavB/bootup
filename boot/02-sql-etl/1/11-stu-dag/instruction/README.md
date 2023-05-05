# Directed acyclic graphs (DAGs)

## Task 

Create a directed acyclic graph to execute your models in the correct order. 

1. Create a `ts` object of the class `TopologicalSorter()`
2. Add nodes to the `ts` object in the correct order. `ts.add("this_node", "parent_node_1", "parent_node_2")` 
3. Extract the nodes's static order using `ts.static_order()`
4. Loop through each node and execute the build model function against the node name

Note: We have included an additional model called `serving_exchange_summary.sql`. Include this model in the appropriate step in the DAG. 
