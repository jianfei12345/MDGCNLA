import numpy as np
import jianfei_src

Dataset2 = np.load('Dataset2.npy', allow_pickle=True).item()

output = jianfei_src.InterAB_Run(Dataset2, jianfei_src.AB_GCNGAT)



