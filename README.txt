Purpose:
  Giving a pathway to replace manual SAS programming by an automated process chain especially for creating CDISC SDTM + ADaM and TFL outputs.

Key steps for a successful design:
  - Build up a Metadata Repository consisting of graph data (RDF triples) sitting at the heart of your processes.
  - Thoroughly identify data items to be stored in the MDR (Metadata Repository).
  - Setup of database queries to pull out metadata items to be consumed by standardized SAS programs. Permanent storage of query code in a library. SAS programs to read in all needed metadata via INFILE and INPUT statement (Queried metadata from MDR resides as lists in application readable text files).
  - Creation of standardized and metadata driven SAS programs.
  - Submission: Agencies are passed SAS programs along with connected input metadata fetched from the MDR thus, keep the SAS program logic alive across sites.
