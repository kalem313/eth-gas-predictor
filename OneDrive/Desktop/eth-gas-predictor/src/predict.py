{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "d3044cbc-caf1-4c29-a607-3b38128d4315",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "Ethereum Gas Price Prediction (next 1 minute):\n",
      "Random Forest: 1.61 gwei\n",
      "MLP Regressor: 1.55 gwei\n"
     ]
    }
   ],
   "source": [
    "import pandas as pd\n",
    "import joblib\n",
    "\n",
    "df = pd.read_csv('gas_log.csv')\n",
    "df['timestamp'] = pd.to_datetime(df['timestamp'])\n",
    "df = df.sort_values('timestamp')\n",
    "\n",
    "latest = df.iloc[-1]\n",
    "hour = latest['timestamp'].hour\n",
    "dayofweek = latest['timestamp'].dayofweek\n",
    "\n",
    "x_input = pd.DataFrame([{\n",
    "    'propose_gas': latest['propose_gas'],\n",
    "    'hour': hour,\n",
    "    'dayofweek': dayofweek\n",
    "}])\n",
    "\n",
    "rf_model = joblib.load('models/rf_model.pkl')\n",
    "mlp_model = joblib.load('models/mlp_model.pkl')\n",
    "scaler = joblib.load('models/scaler.pkl')\n",
    "\n",
    "# predictions\n",
    "rf_pred = rf_model.predict(x_input)[0]\n",
    "mlp_pred = mlp_model.predict(scaler.transform(x_input))[0]\n",
    "\n",
    "print(\"\\nEthereum Gas Price Prediction (next 1 minute):\")\n",
    "print(f\"Random Forest: {rf_pred:.2f} gwei\")\n",
    "print(f\"MLP Regressor: {mlp_pred:.2f} gwei\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "601c0362-c0bd-454b-89b8-6c5f620dd047",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "7d0f9fec-ce9a-4989-97c4-9638c9ee0f08",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
