#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 28 17:58:33 2017

# The script takes csv file that contains outputs from CNN and splits it into 2 csv files company_prob.csv and non_company.csv based on their values 0 (non-company logos) and 1 (company logos)

@author: shailzajolly
"""
import numpy as np
import csv

company_pred = np.genfromtxt('correct_company_pred_prob.csv', skip_header=True, delimiter=',', dtype=str)
real_company_index = list(np.where(company_pred[:,2]=='1')[0])
real_company = company_pred[real_company_index]
non_company_index = list(np.where(company_pred[:,2]=='0')[0])
non_company = company_pred[non_company_index]

with open('company_prob.csv', 'wb') as f:
      csv.writer(f).writerows(real_company)

with open('non_company_prob.csv', 'wb') as f:
      csv.writer(f).writerows(non_company)
