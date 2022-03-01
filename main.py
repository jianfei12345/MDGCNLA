import numpy as np
import jianfei_src

Dataset = np.load('Dataset_formulated.npy', allow_pickle=True).item()
Dataset1 = dict()
Dataset1['miR_dis'] = Dataset['Dataset2_miR_dis']
Dataset1['miR_dis']['input1_name'] = Dataset1['miR_dis']['input1_name'].iloc[:,0]
Dataset1['miR_dis']['input2_name'] = Dataset1['miR_dis']['input2_name'].iloc[:,0]

Dataset2 = np.load("F:\papers\my work\Drug repurposing\miRNA-drug\pythonProject1_算法\Dataset1.npy", allow_pickle=True).item()

Dataset2.update(Dataset1)
np.save('Dataset2.npy', Dataset2)
output = jianfei_src.InterAB_Run(Dataset2, jianfei_src.AB_GCNGAT)



