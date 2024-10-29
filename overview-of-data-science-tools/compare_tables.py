import pandas as pd

# Fields in endpoints and strategyMap
endpoints_fields = [
    "legalEntities", "companyRoles", "yearsOfExperience", "therapeuticAreas", 
    "pharmaceuticalForms", "rxOtc", "dealTypes", "gmpCertifications", 
    "offerTypes", "wayOfAdministrations", "primaryPackaging", "originalGx", 
    "protectionCategory", "incoterms2020", "mah", "segments", "regions", 
    "locations", "temperatures", "pharmaceuticalWarehouses", "channelsOfSalesInFocus", 
    "distributionChannels", "customerBaseOfHcps", "inHouseResources", 
    "serializationSystems", "indications"
]

strategyMap_keys = [
    "api", "substance_origin", "atc", "product_category", "origin_country", 
    "pharmaceutical_forms", "way_of_administration", "primary_packaging", 
    "indication", "dossier_type", "dossier_status", "gmp_certification", 
    "country_with_patients", "deal_type", "available_locations", "currency", 
    "delivery_terms", "ma_holder", "original_gx", "rx_otc", "exclusivity", 
    "royalty", "down_payment"
]

# Identifying missing fields in endpoints compared to strategyMap
missing_in_endpoints = [field for field in strategyMap_keys if field not in endpoints_fields]

# Create DataFrame for visualization
comparison_df = pd.DataFrame({
    "Field in StrategyMap": strategyMap_keys,
    "Present in Endpoints": ["Yes" if field in endpoints_fields else "No" for field in strategyMap_keys]
})

import ace_tools as tools; tools.display_dataframe_to_user(name="StrategyMap Fields Comparison", dataframe=comparison_df)
