/*
   This is an example SAS program to create display 14.3.1 Result no. 2.
   To do so it takes on metadata SAS code that models the primary efficacy.
   The only hardcode is a link to your MDR item connecting the statistical model to this output + string indicating the desired analysis result number.
   I have chosen FOPEN to read SAS code as it is more generic in reading files.
   The other way to read SAS code is by using %INCLUDE of course.

   Benefits:
   ---------

   - Statistical model code comes from a pre-specified source. No manual typing necessary nor
        lookup for code template.
   - At the same time the statistical model code (as part of the MDR) can be used for Define.xml section
        "Analysis Results Metadata" on the respective SAS output (table 14.3.1 R2).
        Thus documentation goes along with coding.
*/

filename inp_fl "/home/dirk/Dokumente/MDR/ARM_code_ADAS-Cog_summary_table.txt" encoding="utf-8" ;
data _null_;
infile inp_fl;
input display_id path name_of_file $ ;
IF display_id = "RD.Table_14-3.01_R2" THEN call symput("path_to_file", CATS(path, name_of_file));
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
