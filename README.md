# Alignment 
(Inspired by ClayFlannigan)
This script was created to calculate RMSD between two molecule structures including proteins (in general case - point clouds).
I've used Kabsch algorithm (DOI: 10.1107/S0567739476001873) to find the rotation martix via SVD to match one structure on another. This algorithm claims both matrix have equal size.
Note, that this algorithm demands the same order of atoms in both matrixes of molecules which one intends to align each other. I.e. first atom of first structure will align to first atom of second structure. Otherwise algorithm will not be able to find the proper rotation. Then also one can calculate root-mean-square-deviation (RMSD) between structures to estimate diversity. 
![alt text](https://github.com/bokertof/alignment/blob/master/20190606_141030.jpg?raw=true)
