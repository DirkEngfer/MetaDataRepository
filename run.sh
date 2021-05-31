arq --data test.ttl --query test.rq > SDTM_CM_variables.txt ;
arq --data test.ttl --query Order_of_SDTM_vars.rq > SDTM_CM_variables_sort_order.txt ; python query_results_formatter.py ;
arq --data test.ttl --data sdtm2adam_conversion.ttl --query CMSTDTC2ATM.rq > SDTM_Convert_CMSTDTC_to_ATM.txt ; python query_results_formatter.py ;
