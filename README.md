# Alignment 
(Inspired by ClayFlannigan)
This script was created for calculations of RMSD between two structures (including proteins).
I've used Kabsch algorithm (DOI: 10.1107/S0567739476001873) with finding of rotation martix via SVD to align one structure on another. This algorithm claims both matrix have equal size.
Note, that this algorithm have disadvantage: order of atoms in both matrixes of molecules that you want to align each other is very important. I.e. first atom of first structure will align to first atom of second structure. Otherwise algorithm will not be able to find necessary minima of rotation. Then also one can calculate root-mean-square-deviation (RMSD) between structures to estimate diversity. 
![alt text](https://github.com/bokertof/alignment/blob/master/20190606_141030.jpg?raw=true)
