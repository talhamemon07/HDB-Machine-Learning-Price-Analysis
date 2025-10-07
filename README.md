# HDB Price Predictor

This project enables one to predict HDB prices based on factors like location, flat type, flat size and its lease commencement date.

## Key Findings

Fascinating insights can be drawn by how the algorithm weighs the various factors below on the influence they have on market pricing:

- **Town**: 24.2%
- **Flat Type**: 3.5%
- **Floor Area**: 50.8%
- **Remaining Lease**: 21.5%

## Insights

This analysis highlights that factors often overlooked in HDB pricing, such as the remaining lease, can actually be more important than the location of the flats. This program could in turn benefit:

- **Buyers** to gauge reasonable prices for resale flats
- **Sellers** to adjust their selling prices based on market factors  
- **All parties** to make better decisions and reduce information asymmetry
- **Market efficiency** by discouraging buyers and sellers from 'trying their luck' in price negotiations

## Technical Details

- **Language**: Python
- **Algorithm**: Random Forest Regression
- **Packages**: Pandas, Numpy, Scikit-learn
- **Data compatibility**: Please use the model with data from 2017 onwards

## Disclaimer

Do note that in the future, the data from data.gov.sg will change and this model may not be appropriate for periods beyond 2025/2026 due to ever-evolving market conditions and government policy. Also, please do not use this as financial advice or for price speculation beyond 2025.
