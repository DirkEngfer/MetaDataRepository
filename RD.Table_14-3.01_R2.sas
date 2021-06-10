filename inp_fl "/home/dirk/Dokumente/MDR/ARM_code_ADAS-Cog_summary_table.txt" encoding="utf-8" ;
data _null_;
infile inp_fl;
input display_id path name_of_file $ ;
call symput("path_to_file", CATS(path, name_of_file));
run;

%macro get_code_primary_efficacy;                                                                                                                            
 %let filrf=myfile;                                                                                                                     
 %let rc=%sysfunc(filename(filrf, &path_to_file.));                                                                                  
 %let fid=%sysfunc(fopen(&filrf));                                                                                                      
 %if &fid > 0 %then                                                                                                                     
  %do %while(%sysfunc(fread(&fid))=0); %* iterate over lines ;                                                                                                 
   %let rc=%sysfunc(fget(&fid, c, 200)); %* fget copies data from the buffer into macro variable c;                                                                                          
   &c. %* Generate SAS code dynamically ;                                                                                                                             
  %end;                                                                                                                                 
 %let rc=%sysfunc(fclose(&fid));                                                                                                        
 %let rc=%sysfunc(filename(filrf));                                                                                                     
%mend get_code_primary_efficacy;                                                                                                                             
                                                                                                                                        
%get_code_primary_efficacy;
