
    
    select
      count(*) as failures,
      count(*) != 0 as should_warn,
      count(*) != 0 as should_error
    from (
      
    
  
    
    



select date
from `marketing-analytics-9123`.`raw`.`ga4_traffic_raw`
where date is null



  
  
      
    ) dbt_internal_test