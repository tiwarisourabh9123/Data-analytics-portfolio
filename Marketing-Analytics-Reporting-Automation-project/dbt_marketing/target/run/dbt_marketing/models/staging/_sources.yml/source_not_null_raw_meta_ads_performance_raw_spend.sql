
    
    select
      count(*) as failures,
      count(*) != 0 as should_warn,
      count(*) != 0 as should_error
    from (
      
    
  
    
    



select spend
from `marketing-analytics-9123`.`raw`.`meta_ads_performance_raw`
where spend is null



  
  
      
    ) dbt_internal_test