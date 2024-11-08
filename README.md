# Project Overview

Project Details from Data Scientist's Email

Earlier this year, our client, a grocery retailer, launched a campaign for their new “Delivery Club.” This club costs $100 per year and offers free grocery deliveries, compared to the usual $10 per delivery.

For the campaign, customers were randomly divided into three groups:

The first group received a low-cost, basic mailer.
The second group received a high-cost, premium mailer.
The third group, the control group, received no mailer.
The client has observed that customers who received a mailer signed up for the Delivery Club at a much higher rate than those in the control group. Now, they would like to understand if there’s a significant difference in sign-up rates between the low-cost and high-cost mailers. This analysis will help them optimize campaign ROI in the future.

# Action
To compare the sign-up rates of the two groups, we used the Chi-Square Test for Independence (details are provided below).

Note: We could also use a Z-Test for Proportions here, but we chose the Chi-Square Test because:

Both tests yield the same statistic.
Chi-Square can be explained using simple 2x2 tables, making it easier for stakeholders to understand.
It’s flexible for more than two groups, allowing the client a consistent approach to measuring significance.
From the campaign_data table, we selected customers who received “Mailer 1” (low-cost) and “Mailer 2” (high-cost) and excluded the control group.

Hypotheses and Acceptance Criteria:

Null Hypothesis: Mailer type and sign-up rate are independent.
Alternate Hypothesis: Mailer type and sign-up rate are related.
Acceptance Criteria: 0.05 significance level.
For the Chi-Square Test, we organized the data into a 2x2 table of signup_flag by mailer_type. Using the scipy library, we calculated the Chi-Square statistic, p-value, degrees of freedom, and expected values.
