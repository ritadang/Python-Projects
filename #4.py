import numpy as np
import matplotlib.image as mpimg
import matplotlib.pyplot as plt

def detect_edge(im, method):
    """
    The function  takes a gray-scale image and detects edges, 
    with the option of horizontal, vertical or both.
    """ 
    #import the necessary modules
    import numpy as np
    import matplotlib.pyplot as plt
    
    #convert 3D grayscale to 2D grayscale
    gray2D=im[:,:,0].copy()
    grayscore=gray2D.copy()  #create a separate matrix to store the scores 
    
    vertical_filter=np.array([[-1,0,1],[-2,0,2],[-1,0,1]])  #create a vertical filter
    horizontal_filter=np.array([[-1,-2,-1],[0,0,0],[1,2,1]])  #create a horizontal filter

    if method == "vertical":
        
        for i in range(1,gray2D.shape[0]-1):
            for j in range(1,gray2D.shape[1]-1):
                
                submatrix=gray2D[(i-1):((i+1)+1),(j-1):((j+1)+1)]
                S_V=np.sum(vertical_filter*submatrix)
                grayscore[i][j]=(S_V+4)/8
            
    
    if method == "horizontal":
        
        for i in range(1,gray2D.shape[0]-1):
            for j in range(1,gray2D.shape[1]-1):
                submatrix=gray2D[(i-1):((i+1)+1),(j-1):((j+1)+1)]
                S_H=np.sum(horizontal_filter*submatrix)
                grayscore[i][j]=(S_H+4)/8
        
    if method == "both":
        
        for i in range(1,gray2D.shape[0]-1):
            for j in range(1,gray2D.shape[1]-1):
                submatrix=gray2D[(i-1):((i+1)+1),(j-1):((j+1)+1)]
                a=(np.sum(horizontal_filter*submatrix))**2
                b=(np.sum(vertical_filter*submatrix))**2
                grayscore[i][j]=(np.sqrt(a+b))/4

        
        
    
    #convert 2D grayscale back to 3D grayscale
    gray3D = np.einsum("ij,k->ijk", grayscore, np.ones(3))
    #print(gray3D)
    
    
    return gray3D
    

#test

x,y=np.ogrid[0:100, 0:100]
im=[[[1,1,1]]*100]*100 
im=np.array(im,dtype='float') 
mask= (x>30) & (x<70) & (y>30) & (y<70)
im[mask]=[0,0,0]

plt.imshow(im, cmap="gray")  #show original input pic
plt.show()

vimg=detect_edge(im,"vertical")
plt.imshow(vimg, cmap="gray")  #show vertical edges
plt.show()

himg=detect_edge(im,"horizontal")
plt.imshow(himg, cmap="gray")  #show horizontal edges
plt.show()

bimg=detect_edge(im,"both")
plt.imshow(bimg, cmap="gray")  #show edges in both directions 
plt.show()
   
    
