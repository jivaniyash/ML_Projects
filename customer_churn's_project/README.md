# BANK_CHURN_PROJECT

This folder cantains files to process the bank churner's sample data for finding out the answers.

### Business Questions:

    1) What reasons or factors majorly affects the customer to leave the company?

    2) Find out which existing customers might leave the company in future?

Sample data - [BankChurners for EDA 2023](https://github.com/jivaniyash/ML_Projects/blob/master/customer_churn's_project/BankChurners.csv) - is csv file of sample data set containing of 5,998 records of customers from 3,100,111 customers' record.

There are total 21 attributes(columns) containing customer's info:

    1. Clientnum - Client number. Unique identifier for the customer holding the account
    2. Attrition_Flag - Internal event (customer activity) variable -
        - Existing Customer: if the account is open 
        - Attrited Customer: if the account is closed
    3. Customer_Age - Demographic variable - Customer's Age in Years
    4. Gender - Demographic variable - 
        - M: Male 
        - F: Female
    5. Dependent_count - Demographic variable - Number of dependents
    6. Education_Level - Demographic variable - Educational Qualification of the account holder -
        - high school
        - college graduate, etc
    7. Marital_Status - Demographic variable - 
        - Married
        - Single
        - Divorced
        - Unknown
    8. Income_Category - Demographic variable - Annual Income Category of the account holder -
        - < $40K
        - $40K - 60K- $60K
        - $80K, $80K-$120K
        - > $120K
        - Unknown
    9. Card_Category - Product Variable - Type of Card - 
        - Blue
        - Silver
        - Gold
        - Platinum
    10. Months_on_book - Period of relationship with bank
    11. Total_Relationship_Count - Total no. of products held by the customer
    12. Months_Inactive_12_mon - No. of months inactive in the last 12 months
    13. Contacts_Count_12_mon - No. of Contacts in the last 12 months
    14. Credit_Limit - Credit Limit on the Credit Card
    15. Total_Revolving_Bal - Total Revolving Balance on the Credit Card
    16. Avg_Open_To_Buy - Open to Buy Credit Line (Average of last 12 months)
    17. Total_Amt_Chng_Q4_Q1 - Change in Transaction Amount (Q4 over Q1)
    18. Total_Trans_Amt - Total Transaction Amount (Last 12 months)
    19. Total_Trans_Ct - Total Transaction Count (Last 12 months)
    20. Total Ct Chng Q4 Q1 – Rate of counts from Q1 to Q4
    21. Avg_Utilization_Ratio - Average Card Utilization Ratio
