arq --data test.ttl --query test.rq > SDTM_CM_variables.txt ;
arq --data test.ttl --query Order_of_SDTM_vars.rq > SDTM_CM_variables_sort_order.txt ;
arq --data test.ttl --data sdtm2adam_conversion.ttl --query CMSTDTC2ATM.rq > SDTM_Convert_CMSTDTC_to_ATM.txt ; 
arq --data test.ttl --data imputation_rules.ttl --query value_imputation.rq > imputations.txt ; python query_results_formatter.py ;
