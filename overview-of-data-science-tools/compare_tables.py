# List of fields in endpoints and strategyMap
endpoints_fields = ["legalEntities", "companyRoles", "yearsOfExperience", "therapeuticAreas", "pharmaceuticalForms"]

# Create shorter strategyMap list for simplicity
strategyMap_keys = ["api", "companyRoles", "therapeuticAreas", "rx_otc"]

# Identify missing fields in endpoints compared to strategyMap
missing_in_endpoints = [field for field in strategyMap_keys if field not in endpoints_fields]

# DataFrame visualization of comparison
import pandas as pd
comparison_df = pd.DataFrame({
    "Field in StrategyMap": strategyMap_keys,
    "Present in Endpoints": ["Yes" if field in endpoints_fields else "No" for field in strategyMap_keys]
})

# Display the DataFrame
print(comparison_df)