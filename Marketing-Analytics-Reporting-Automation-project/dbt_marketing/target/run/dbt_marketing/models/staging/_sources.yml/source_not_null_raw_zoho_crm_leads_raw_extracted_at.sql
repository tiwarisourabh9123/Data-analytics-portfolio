
    
    select
      count(*) as failures,
      count(*) != 0 as should_warn,
      count(*) != 0 as should_error
    from (
      
    
  
    
    



select extracted_at
from `marketing-analytics-9123`.`raw`.`zoho_crm_leads_raw`
where extracted_at is null



  
  
      
    ) dbt_internal_test