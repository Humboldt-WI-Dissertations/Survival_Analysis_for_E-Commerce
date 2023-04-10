# Survival Analysis for Management Support in E-Commerce
Code Repository for M.Sc. Thesis in Economics and Management Science at Humboldt-Universität zu Berlin.

#### Abstract
In the past decade, we have seen the rise of numerous online marketplaces for used cars. This study explores the efficacy of combining survival analysis with model explanation frameworks to enhance the management system of online platforms. We extend the work done by Jerenz (2008) to estimate the demand function of used cars for a specific dealership using survival analysis. During the price and survival modelling stages, various models are evaluated to identify the key factors that impact demand. Finally, we apply the recently developed SurvSHAP(t) framework to derive key insights and recommendations for supporting online platforms.

#### Installation
```bash
pip install -r requirements.txt
```

#### Usage
- The complete code is stored in `survival_modelling.ipynb`
- The models trained in the Price Modelling section are evaluated by calling `model_evaluation.py` from `utilities`
- The explanations created by SurvSHAP are visualized by calling `survshap_util.py` from `utilities`


--------------------------------------------------------------------
This study was done in collaboration with a private sector entity and the data used can not be shared.
