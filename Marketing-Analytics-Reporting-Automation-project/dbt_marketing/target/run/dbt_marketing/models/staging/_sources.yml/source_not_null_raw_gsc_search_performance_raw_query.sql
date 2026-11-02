
    
    select
      count(*) as failures,
      count(*) != 0 as should_warn,
      count(*) != 0 as should_error
    from (
      
    
  
    
    



select query
from `marketing-analytics-9123`.`raw`.`gsc_search_performance_raw`
where query is null



  
  
      
    ) dbt_internal_test