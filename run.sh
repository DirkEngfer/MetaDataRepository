arq --data test.ttl --query test.rq > SDTM_CM_variables.txt ;
arq --data test.ttl --query Order_of_SDTM_vars.rq > SDTM_CM_variables_sort_order.txt ; python query_results_formatter.py

