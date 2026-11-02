
    
    select
      count(*) as failures,
      count(*) != 0 as should_warn,
      count(*) != 0 as should_error
    from (
      
    
  
    
    



select cost
from `marketing-analytics-9123`.`raw`.`google_ads_performance_raw`
where cost is null



  
  
      
    ) dbt_internal_test