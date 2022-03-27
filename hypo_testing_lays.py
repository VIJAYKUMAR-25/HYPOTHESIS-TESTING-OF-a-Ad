'''Reverse engineering in an ad and find the hypothesis test behind in it
1.implementation code
2.access values using excel'''

'''
step1->> y=age lies(5-25) x=age lies(25-45)
step2->> alpha=0.05
step3->> chi square
step4->> H0=pi=pc=pb=ps
         H1=pi=pc=ps
step5->> compare Pval with alpha
step6->> if less reject null hypothesis
step7->> conclusion(target customer is age lies between 5-25)

'''

#sample data's are collected from the population
#include the necessary packages
import pandas as pd
lays_data=pd.read_excel("C:/Users/ELCOT/Desktop/hypothesis test_lays.xlsx")
lays_data.head()

from scipy import stats
stats.shapiro(lays_data.AGE_BETWEEN_5_TO_25)
stats.shapiro(lays_data.AGE_BETWEEN_25_TO_45)

from statsmodels.stats.weightstats import ztest
ztest(lays_data.AGE_BETWEEN_5_TO_25,value=20)
#t-test
from statsmodels.stats.proportion import proportions_ztest
stats.ttest_ind(lays_data.AGE_BETWEEN_5_TO_25,lays_data.AGE_BETWEEN_25_TO_45)

#Pvalue=0.021718443  whilch is less than alpha (0.05)
