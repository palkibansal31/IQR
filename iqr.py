# -*- coding: utf-8 -*-
"""
Created on Thu Feb  6 21:25:04 2020

@author: HP
"""

import pandas as pd
import numpy as np

def iqr(old_file,new_file):
    
    #data=pd.read_csv(r"C:\Users\HP\Documents\dat_pacakge2.csv",index_col=0)
    #data=pd.read_csv(r"C:\Users\HP\Desktop\dataset2-package2.csv",index_col=0)
    dataset=pd.DataFrame(old_file)
    print(dataset)
    
    row_count=dataset.shape[0]
    column_count=dataset.shape[1]
     
    
    
        
    column_list= [column for column in dataset.columns]
    removed_rows=0
        #column_list=list(dataset.columns)
        #dataset=dataset.sort_values(by=column_list[i])
        #pcolumn=dataset.iloc[:,i].values
        # x=list(dataset.iloc[:,2].values)
        #print(x)
        #dataset=dataset.sort_values(by=x)
        #dataset[order( dataset[,1] ),]
    for i in column_list:
        #print(dataset)
        quantile1,quantile3=np.percentile(dataset[i],[25,75])
        #print(quantile1)
        print(quantile3)
        iqr=quantile3-quantile1
        lower_bound=quantile1-(1.5*iqr)
        upper_bound=quantile3+(1.5*iqr)
        #print(iqr)
        #print(lower_bound)
        #print(upper_bound)
       
        iqr_outliers = dataset[(dataset[i] < lower_bound) | (dataset[i] > upper_bound)].index
        dataset.drop(iqr_outliers, inplace = True)
        removed_rows += len(iqr_outliers)
    dataset.to_csv(new_file)
    
import sys 

def main():
    dataset=pd.read_csv(sys.argv[1]).values
    newdata=sys.argv[2]
    iqr(dataset,newdata)
    
if __name__=="__main__":
     main()