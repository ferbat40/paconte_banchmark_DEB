from DTLZ1 import DTLZ1
from init_benchmark import InitBenchmark
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from algorithms import NSGA_benchmark




class CreateBenchmark(InitBenchmark):
    
    def __init__(self,benchmark,P,N,M,fo_in=[],fo_out=[],fo_out_g=[],DTLZ=None):
        super().__init__(P,N,M,fo_in,fo_out,fo_out_g,DTLZ)
        self.benchmark=benchmark
        self.PARAM = {
                1:  self.call_DTLZ1,
                2:  self.call_DTLZ2,
                }
          
            
        
    def call_DTLZ1(self):
        self.set_DTLZ(DTLZ1(self))

    
    def call_DTLZ2(self):
        print("em construção")


    def call_benchmark(self):
        if self.benchmark in self.PARAM:
           self.PARAM[self.benchmark]()

    
    

    def plot_graphic_configure(self,vet_0=[],vet_1=[],vet_3=[]):
        fig = plt.figure()
        fig = plt.figure(figsize=(10, 15))
        ax = fig.add_subplot(111, projection='3d')
        try:
            ff = np.array([fp[0:] if len(fp) > 0 else [0,0,0] for fp in vet_0])
            pp = np.array([fp[0:] if len(fp) > 0 else [0,0,0] for fp in vet_1])
            cp = np.array([cv[0:] if len(cv) > 0 else [0,0,0] for cv in vet_3])
        except Exception as e:
            ff = np.array([fp[0:] if len(fp) > 0 else [0,0,0] for fp in vet_0[0]])
            pp = np.array([fp[0:] if len(fp) > 0 else [0,0,0] for fp in vet_0[1]])
            try:
                cp = np.array([cv[0:] if len(cv) > 0 else [0,0,0] for cv in vet_1])
            except Exception as e:
                print(f'{e}')
            
             
        try:
            print(len(ff),len(pp),len(cp))
        except Exception as h:
            print(f'{h}')
        if (len(ff) >0):
            ax.scatter(ff[:,0],ff[:,1],ff[:,2],color='red')
        if (len(pp) >0):
            ax.scatter(pp[:,0],pp[:,1],pp[:,2],color='gray')
        try:
            if (len(cp) >0):
                ax.scatter(cp[:,0],cp[:,1],cp[:,2])
        except Exception as c:
            print(f'{c}')
        ax.view_init(elev=360, azim=25)
        plt.show()

        
    
    def plot_graphic_in_G(self):
        fig = plt.figure()
        fig = plt.figure(figsize=(10, 15))
        ax = fig.add_subplot(111, projection='3d')
        pp = np.array([fp[0:] if len(fp) > 0 else [0,0,0] for fp in self.get_fo_in() ])
        cp = np.array([cv[0:] if len(cv) > 0 else [0,0,0] for cv in self.get_fo_out() ])
        print(pp.shape,cp.shape)
        if (len(cp)>0):
            ax.scatter(cp[:,0],cp[:,1],cp[:,2],color='gray')
        if (len(pp)>0):
            ax.scatter(pp[:,0],pp[:,1],pp[:,2],color='red')
        ax.view_init(elev=360, azim=25)
        plt.show()


    def plot_graphic_out_G(self):
        fig = plt.figure()
        fig = plt.figure(figsize=(10, 15))
        ax = fig.add_subplot(111, projection='3d')
        ff = np.array([fp[0:] if len(fp) > 0 else [0,0,0] for fp in self.get_fo_out_g()])
        pp = np.array([fp[0:] if len(fp) > 0 else [0,0,0] for fp in self.get_fo_in() ])
        cp = np.array([cv[0:] if len(cv) > 0 else [0,0,0] for cv in self.get_fo_out()  ])
        print(pp.shape,cp.shape,ff.shape)
        if (len(pp) >0):
            ax.scatter(pp[:,0],pp[:,1],pp[:,2],color='red')
        if (len(cp) >0):
            ax.scatter(cp[:,0],cp[:,1],cp[:,2],color='gray')
        ax.scatter(ff[:,0],ff[:,1],ff[:,2])
        ax.view_init(elev=360, azim=25)
        plt.show()
        
       

  

benchmark = CreateBenchmark(1,1500,7,3)
benchmark.call_benchmark()
benchmark.get_DTLZ().build_objective_space_in_G()
#var2=benchmark.get_DTLZ().build_objective_space_out_G()
#benchmark.plot_graphic_configure(var,var2,var2)
#benchmark.plot_graphic_in_G()
#NSGAbenchmark = NSGA_benchmark(benchmark.get_Nvar(),benchmark.get_M(),1,np.full(2, 0.49),np.full(2, 0.50),benchmark.get_fo_out_g())


#dados=benchmark.get_fo_out()
#print(benchmark.get_fo_out())





#benchmark.get_DTLZ().build_objective_space_in_G()
#benchmark.plot_graphic_in_G()
 








