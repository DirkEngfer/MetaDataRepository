arq --data test.ttl --query test.rq > SDTM_CM_variables.txt ;
arq --data test.ttl --query Order_of_SDTM_vars.rq > SDTM_CM_variables_sort_order.txt ;
arq --data test.ttl --data sdtm2adam_conversion.ttl --data imputation_rules.ttl --query CMSTDTC2ATM.rq > SDTM_Convert_CMSTDTC_to_ATM.txt ; 
arq --data test.ttl --data imputation_rules.ttl --query value_imputation.rq > LLOQ.txt ; 
arq --data test.ttl --data imputation_rules.ttl --query ENDTC_DayImputation.rq > EndDayImputation.txt ;
arq --data imputation_rules.ttl --query impute_missing_start_day.rq > StartDayImputation.txt ;
arq --data ARM.ttl --query ARM_code_ADAS-Cog_summary_table.rq > ARM_code_ADAS-Cog_summary_table.txt ;
arq --data ARM.ttl --query ARM_whereclauses.rq > ARM_whereclause.txt ;
sleep 3 && python query_results_formatter.py ;
