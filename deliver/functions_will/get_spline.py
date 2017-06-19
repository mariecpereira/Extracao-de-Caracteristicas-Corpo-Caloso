# -*- encoding: utf-8 -*-
import numpy as np
import ia870 as MM
import scipy.interpolate as spline
import functions_will as FW

def get_spline(seg,s):
    nz = np.nonzero(seg)
    x1,x2,y1,y2 = np.amin(nz[0]),np.amax(nz[0]),np.amin(nz[1]),np.amax(nz[1])
    M0 = seg[x1-5:x2+5,y1-5:y2+5]
    nescala = [4*M0.shape[-2],4*M0.shape[-1]]
    M0 = FW.resizedti(M0,nescala).astype('bool')
    con_M0 = np.logical_xor(MM.iaero(M0),M0)
    seq = FW.get_seq_graph(con_M0)
    tck, _ = spline.splprep(seq, k=5, s=s)
    return tck

