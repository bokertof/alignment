import numpy as np
from scipy.spatial import cKDTree

class Alignment:
     def __init__(self, A, B):
          
         assert self.A.shape == self.B.shape
         self.A = A
         self.B = B

         self.Dim = A.shape[1] # dimensions
         self.number = A.shape[0] # number of points

     def nearest_neighbor(self):
          '''
           Returns:
              distances and indices nearest neighbor in B
          '''

          tree = cKDTree(self.B)
          distances, indices = tree.query(self.A, k=1)
          return distances, indices


     def kabsch(self):
          '''
          Returns:
             R: DxD rotation matrix
             
          '''

          # translate centroids of two point clouds to zero
          centroid_A = np.mean(self.A, axis=0)
          centroid_B = np.mean(self.B, axis=0)
          AA = self.A -centroid_A
          BB = self.B -centroid_B

          # rotation matrix
          H = np.dot(AA.T, BB)
          U, S, Vt = np.linalg.svd(H)
          R = np.dot(Vt.T, U.T)

          # special case
          if np.linalg.det(R) < 0:
              Vt[self.Dim-1,:] *= -1
              R = np.dot(Vt.T, U.T)

          return R

     def new_A(self,R):
        '''
        Returns:
           new matrix A, after rotation
        '''
        new_A = np.dot(R, self.A.T).T
        return new_A


     def get_RMSD(self):
        ''' Returns:
            RMSD between two structures
        '''
        dists,_ = Alignment.nearest_neighbor(self)

        RMSD = (sum([i**2 for i in dists])/self.number)**0.5

        return RMSD



