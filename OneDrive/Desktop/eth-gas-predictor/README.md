# Ethereum Gas Price Predictor 

This project uses machine learning to predict Ethereum gas prices using real-time data collected from the Etherscan Gas Oracle API. It combines classic regression techniques (Random Forest) with neural networks (MLP) to forecast the gas price for the next minute.

---

## Features
- Collects live gas prices every minute using Etherscan API
- Logs data into a local CSV file
- Performs feature engineering using timestamp features
- Trains and compares two ML models:
  - Random Forest Regressor
  - MLP Regressor
- Outputs Mean Absolute Error and visualizes prediction performance
- Predicts next-minute gas prices using the latest logged values

---

## Technologies Used
- Python (pandas, scikit-learn, joblib, matplotlib)
- Jupyter Notebook for training and visualization
- CSV file logging from Etherscan API

---

## Folder Structure
```
eth-gas-predictor/
├── models/
│   ├── rf_model.pkl              # Random Forest model
│   ├── mlp_model.pkl             # MLP model
│   └── scaler.pkl                # Scaler for MLP
├── src/
│   └── predict.py                # Predict next gas price
├── notebooks/
│   └── modeling.ipynb            # Full training pipeline + plots
├── gas_log.csv                   # sample dataset
├── requirements.txt
└── README.md
```

Outputs gas price predictions from both models using the latest row in your dataset.

---

## Author
Evangelos Kalemkeridis  