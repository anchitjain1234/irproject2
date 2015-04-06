This directory contains 
					
					1 data scraping directory "googleresults" which scrapes the best 30 results from google and yahoo for search term "jaguar"

					1 differenct packages installing script installation.sh

					1 main script main.sh

					1 main program file program.py

To run the program please make sure that all the dependencies are installed beforehand.
Install all the dependencies by running installation.sh

Run the main program by running main.sh

The output files generated would be:
	1.aggregateddata.txt
	2.googletitleandsnippet.txt
	3.googleurls.txt
	4.ResultantRanks_A1.txt
	5.ResultantRanks_A2.txt
	6.yahootitleandsnippet.txt
	7.yahoourls.txt



Function descriptions :-

1. read_raw_json :- This function reads data dumped by crawler in JSON format and prints it in 4 files googletitleandsnippet.txt,googleurls.txt,yahootitleandsnippet.txt,yahoourls.txt.

2.printagg :- This function prints the aggreggate data of all the links searched by Google and Yahoo in aggregateddata.txt

3.algo1 :- This function runs the Best Rank Approach and store the result in a list algo1res.

4.algo2 :- This function runs the Borda's Approach and store the result in a list algo2res.

5.calcprec :- This function calculates the precision

6.spearmancoeff :- This function calculates the spearman coefficient .