# Alignment
This script was created for calculations of RMSD of two structures
I've used Kabsch algorithm (DOI: 10.1107/S0567739476001873) with finding of rotation martix via SVD for alignment one structure on another
Note, that this algorithm have disadvantage: order of atoms in both matrixes of molecules that you align each other is very important. I.e. first atom of first structure will align to first atom of second structure.
