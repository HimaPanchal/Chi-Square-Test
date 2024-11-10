#!/usr/bin/env python
# coding: utf-8

# # Data Preparation and Processing 
# 
# In the database provided, we have a campaign_data table which shows us which customers received each type of “Delivery Club” mailer, which customers were in the control group, and which customers joined the club as a result. I have included the raw excel file in the main folder, take a look at campaign_data
# 
# For this task, we are looking to find evidence that the Delivery Club sign-up rate for customers that received “Mailer 1” (low cost) was different to those who received “Mailer 2” (high cost) and thus from the campaign_data table we will just extract customers in those two groups, and exclude customers who were in the control group.
# 
# In the code below, we:
# 
# Load in the Python libraries we require for importing the data and performing the chi-square test (using scipy)
# Import the required data from the campaign_data table
# Exclude customers in the control group, giving us a dataset with Mailer 1 & Mailer 2 customers only

# In[35]:


# Import required packages
import pandas as pd
from scipy.stats import chi2_contingency,chi2


# In[ ]:





# In[36]:


# Import Data from an excel file in campaign_data sheet
campaign_data = pd.read_excel("grocery_database.xlsx", sheet_name ="campaign_data")


# In[23]:


# Filtering data from the campaign_data sheet to filter and remove the Control group
campaign_data = campaign_data.loc[campaign_data["mailer_type"] != "Control"]


# # Applying Chi-Square Test For Independence
# 
# State Hypotheses & Acceptance Criteria For Test
# First things first for the Hypothesis test is state our Null Hypothesis, our Alternate Hypothesis, and the Acceptance Criteria 
# 
# We specify the common Acceptance Criteria value of 0.05.

# In[24]:


# specify hypotheses & acceptance criteria for test
null_hypothesis = "There is no relationship between mailer type and sign-up rate.  They are independent"
alternate_hypothesis = "There is a relationship between mailer type and sign-up rate.  They are not independent"
acceptance_criteria = 0.05


# # Calculate Observed Frequencies & Expected Frequencies
# 
# In a Chi-Square Test For Independence, the observed frequencies are the true values that we have seen, in other words the actual rates per group in the data itself. The expected frequencies are what we would expect to see based on all of the data combined.
# 
# Explanation of code below:
# 
# Summarizes our dataset to a 2x2 matrix for signup_flag by mailer_type
# Based on this, calculates the:
# Chi-Square Statistic
# p-value
# Degrees of Freedom - dof
# Expected Values
# Prints out the Chi-Square Statistic & p-value from the test
# Calculates the Critical Value based upon our Acceptance Criteria & the Degrees Of Freedom
# Prints out the Critical Value

# In[25]:


# 2* 2 matric summarize to get our observed frequencies
# aggregate our data to get observed values
observed_values = pd.crosstab(campaign_data["mailer_type"], 
                              campaign_data["signup_flag"]).values


# In[34]:


# run the chi-square test
chi2_statistic, p_value, dof, expected_values = chi2_contingency(observed_values, correction = False)


# In[27]:


# print chi-square statistic
print(chi2_statistic)


# In[28]:


print(p_value)


# In[29]:


critical_value = chi2.ppf(1 - acceptance_criteria, dof)


# In[30]:


# print critical value
print(critical_value)


# # Analysing The Results
# 
# At this point we have all the required results to prove our Chi-Square test - and just from the results above we can see that, since our resulting p-value of 0.16 is greater than our Acceptance Criteria of 0.05 then we will retain the Null Hypothesis and conclude that there is no significant difference between the sign-up rates of Mailer 1 and Mailer 2.
# 
# We can make the same conclusion based upon our resulting Chi-Square statistic of 1.94 being lower than our Critical Value of 3.84
# 
# To make this script more dynamic, following is the code which meets our objective more closely : 

# In[32]:


# print the results (based upon p-value)
if p_value <= acceptance_criteria:
    print(f"As our p-value of {p_value} is lower than our acceptance_criteria of {acceptance_criteria} - we reject the null hypothesis, and conclude that: {alternate_hypothesis}")
else:
    print(f"As our p-value of {p_value} is higher than our acceptance_criteria of {acceptance_criteria} - we retain the null hypothesis, and conclude that: {null_hypothesis}")



# In[33]:


# print the results (based upon p-value)
if chi2_statistic >= critical_value:
    print(f"As our chi-square statistic of {chi2_statistic} is higher than our critical value of {critical_value} - we reject the null hypothesis, and conclude that: {alternate_hypothesis}")
else:
    print(f"As our chi-square statistic of {chi2_statistic} is lower than our critical value of {critical_value} - we retain the null hypothesis, and conclude that: {null_hypothesis}")
    


# As we can see from the outputs above, we retain the null hypothesis. We could not find enough evidence that the sign-up rates for Mailer 1 and Mailer 2 were different - and thus conclude that there was no significant difference.
# 
# 

# In[ ]:




