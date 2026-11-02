
    
    select
      count(*) as failures,
      count(*) != 0 as should_warn,
      count(*) != 0 as should_error
    from (
      
    
  
    
    



select campaign_id
from `marketing-analytics-9123`.`raw`.`google_ads_performance_raw`
where campaign_id is null



  
  
      
    ) dbt_internal_test