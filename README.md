# Survival Analysis for Management Support in E-Commerce

**Type:** Master's Thesis

**Author:** Danyal Ahmed

**1st Examiner:** Prof. Dr. Stefan Lessmann

**2nd Examiner:** Prof. Dr. Benjamin Fabian


## Table of Content

- [Summary](#summary)
- [Setup](#setup)
- [Training](#training)
- [Evaluation](#evaluation)
- [Results](#results)
- [Repository structure](-Repository-structure)

Code Repository for M.Sc. Thesis in Economics and Management Science at Humboldt-Universität zu Berlin.

## Summary
In the past decade, we have seen the rise of numerous online marketplaces for used cars. This study explores the efficacy of combining survival analysis with model explanation frameworks to enhance the management system of online platforms. We extend the work done by Jerenz (2008) to estimate the demand function of used cars in an online marketplace for a specific dealership using survival analysis. The project can be summarised in the following steps:

- Develop a hedonic pricing model utilizing all competing listings in the online marketplace. 
- Use the most accurate hedonic pricing model to estimate the degree-of-overpricing (DOP) of every listing.
- Apply and benchmark modern survival algorithms on target dealership data with their estimated DOPs.
- Create time-dependent explanations through the SurvSHAP framework developed by Krzyziński et al. (2022).
- Develop DOP Quartile based Survival Curves and Risk Scores.

Our experiments conclude that the Catboost Regressor in combination with the Random Survival Forest prove to be the best fit for our data. Analysis of the SurvSHAP explanations and the survival function allow us to predict survival probabilities over time for different DOP Quartiles.

## Setup

- Install Requirements
```bash
pip install -r requirements.txt
```

- This study was done in collaboration with a private sector entity and the data used can not be shared.

## Training
- Fit Pricing Models:
```python
price_model = CatBoostRegressor(random_state=42).fit(X_train, y_train)
```
- Fit Survival Models:
```python
surv_model = RandomSurvivalForest(random_state=42).fit(X,y)
```
- Fit SurvSHAP
```python
model_exp = SurvivalModelExplainer(surv_model, X, y)
global_rsf_exp = ModelSurvSHAP(random_state=42).fit(model_exp)
```

## Evaluation
- Evaluate Pricing Models:
```python
model_evaluation.reg_eval(price_model, X_test, y_test)
```

- Evaluate SurvSHAP:
```python
survshap_util.shap_lines_plot(global_rsf_exp.full_result, 'DOP')
plt.savefig('plots/dop_shap(t).png', transparent=True)
```

## Results
- Survival Modelling Accuracy

|                  | Accelerated Failure Time Model | Survival Catboost | Random Survival Forest | Survival Gradient Boosting |
| ---------------  | ------------------------------ | ----------------- | ---------------------- | -------------------------- |
| Concorance Index |              0.744             |       0.732       |         0.765          |           0.765            |

- Global SurvSHAP Feature Impact

![alt text](https://github.com/danyalahmed247/HU-Thesis/blob/f6b6e173359e05ef6967b7504e3b69371a943c94/plots/mean_shap(t).png?raw=true)

- DOP Quartile based Survival Curves

![alt text](https://github.com/danyalahmed247/HU-Thesis/blob/25bf5d5b8f75b7aa805e23433d5061c17ec8d193/plots/survival_function.png?raw=true)


## Repository structure

```bash
├── README.md
├── requirements.txt                                -- required libraries
├── plots                                           -- stores image files
├── survival_modelling.ipynb                        -- full code application
└── utilities                                       -- helper functions
    ├── model_evaluation.py                           -- hedonic pricing model evaluation
    └── survshap_util.py                              -- create SurvShap plots               
```

