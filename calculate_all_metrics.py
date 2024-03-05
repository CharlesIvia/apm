# This script is used to calculate the LTV for different team compositions and find the optimal team composition for the highest LTV.

#Importing the pandas library
import pandas as pd

# Defining a function to calculate the metrics for different team compositions
def calculate_metrics(total_team_size, initial_ARPU=100, CR=0.10, CRF=0.15, customers_per_sales_agent=5):
    results = []
    for sales_agents in range(total_team_size + 1):
        for support_staff in range(total_team_size - sales_agents + 1):
            account_managers = total_team_size - sales_agents - support_staff
            
            new_customers = sales_agents * customers_per_sales_agent
            new_ARPU = initial_ARPU * ((1 + 0.20) ** 6)
            
            csat_improvement = support_staff * 0.01
            acr = CR - (CR * CRF * csat_improvement)
            acr = max(acr, 0)  # Ensuring ACR doesn't go negative
            
            # Calculate Adjusted LT based on the Adjusted Churn Rate
            adjusted_LT = 1 / acr if acr else float('inf')  # Prevent division by zero
            
            # Calculate LTV based on the new ARPU and Adjusted LT
            ltv = new_ARPU * adjusted_LT
            
            results.append({
                'Sales_Agents': sales_agents,
                'Support_Staff': support_staff,
                'Account_Managers': account_managers,
                'New_Customers': new_customers,
                'New_ARPU': round(new_ARPU, 2),
                'Adjusted_CR': round(acr, 4),
                'Adjusted_LT': round(adjusted_LT, 2),
                'LTV': round(ltv, 2)
            })
    return results

# Use the updated model with a total team size of 20 members
total_team_size = 20
balanced_results = calculate_metrics(total_team_size)

# Convert results to a Pandas DataFrame
df_results = pd.DataFrame(balanced_results)

# Display the first few rows of the DataFrame to verify
print(df_results.head())

# Save the results to a CSV file
df_results.to_csv('balanced_results.csv', index=False)


# Defining a function to find the combination with the highest LTV from the results
def find_optimal_ltv_combination(results):
    # Finding the combination with the highest LTV
    optimal_combination = max(results, key=lambda x: x['LTV'])
    return optimal_combination

# Applying the function to our balanced results with LTV
optimal_ltv_combination = find_optimal_ltv_combination(balanced_results)

# Displaying the optimal combination
print(optimal_ltv_combination)
