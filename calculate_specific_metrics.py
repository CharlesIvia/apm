def calculate_specific_metrics(sales_agents, account_managers, support_staff, initial_ARPU=100, CR=0.10, CRF=0.15, customers_per_sales_agent=5):
    # Calculate new customers added by sales agents
    new_customers = sales_agents * customers_per_sales_agent
    
    # Calculate New ARPU, assuming account management affects all customers equally
    new_ARPU = initial_ARPU * ((1 + 0.20) ** 6)
    
    # Calculate Adjusted Churn Rate (ACR) with improved formula
    csat_improvement = support_staff * 0.01
    acr = CR - (CR * CRF * csat_improvement)
    acr = max(acr, 0)  # Ensuring ACR doesn't go negative
    
    # Calculate Adjusted LT based on the Adjusted Churn Rate
    adjusted_LT = 1 / acr if acr else float('inf')  # Prevent division by zero
    
    # Calculate LTV based on the new ARPU and Adjusted LT
    ltv = new_ARPU * adjusted_LT
    
    # Return the results as a dictionary
    return {
        'Sales_Agents': sales_agents,
        'Account_Managers': account_managers,
        'Support_Staff': support_staff,
        'New_Customers': new_customers,
        'New_ARPU': round(new_ARPU, 2),
        'Adjusted_CR': round(acr, 4),
        'Adjusted_LT': round(adjusted_LT, 2),
        'LTV': round(ltv, 2)
    }

# Usage with specified team allocations
example_result = calculate_specific_metrics(sales_agents=5, account_managers=10, support_staff=5)

# Nicely formatted print output
print("Metrics Summary:")
for key, value in example_result.items():
    print(f"{key.replace('_', ' ').title()}: {value}")
