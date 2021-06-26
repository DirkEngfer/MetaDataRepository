/*
  Use metadata for imputation of partial end date, as selected from your repository


  see template for imputation code: https://www.lexjansen.com/phuse/2006/po/PO11.pdf
  page 5.
*/

filename metadata "/home/dirk/Dokumente/MDR/EndDayImputation.txt" encoding="utf-8" ;
data _null_;
INFILE metadata dlm='|' dsd truncover;
INPUT study rulename :$50. applicable_var rule_short  :$50. description  :$50.;
IF applicable_var = "AEENDTC" THEN DO;
  IF rule_short = "Last_of_month" THEN
  DO;
    CALL SYMPUT('impute_by_last_of_month', %STR(
       if enddt = . and endd_ ne '' then do;
          if substr(endd_,1,2) = '--' and substr(endd_,3,3) ne '---' then ienddt=intnx('month',input(trim('01')||substr(endd_,3),date9.),1)-1;
    ));
  END;
END;
run;

data adae;
  set ...;
  &impute_by_last_of_month.;

run;
  
