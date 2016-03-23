# RNAFolding]
This program is based on Nussinov Algorithm, which is based on Dynamic Programming paradigm.

The worst case of the performance is O(n^3) when assgined the input with the size being n.

All you need to do in order to run the simulation:
1. Give an RNA sequence, which contains the nucleotides symbol, A, U, C, G.
2. Assign the minimum paring distance in the unit of number of nucleotides.

The results will output all the paring cases which allows the maximum pairing.

Besides, two Nussinov packages, Vienna and mfold, are benchmarked. The sequantial and parallel performance of Nussinov Algorithm are compare to that of Four Russian Algorithm(http://almob.biomedcentral.com/articles/10.1186/1748-7188-9-5). The details are summazied in my bigpieit/RNAFolding-benchmark/main.pdf.

Thanks for your attention!

Bingxi Li (bigpieit)
