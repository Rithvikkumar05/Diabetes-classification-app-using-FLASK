{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "ba5244e5-433e-4c80-84f3-249357d86ea5",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      " * Serving Flask app '__main__'\n",
      " * Debug mode: on\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.\n",
      " * Running on http://127.0.0.1:5000\n",
      "Press CTRL+C to quit\n",
      "127.0.0.1 - - [06/Jul/2024 18:52:33] \"GET / HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [06/Jul/2024 18:53:34] \"POST /predict1 HTTP/1.1\" 200 -\n"
     ]
    }
   ],
   "source": [
    "from flask import Flask, request, render_template, jsonify\n",
    "import pickle\n",
    "import numpy as np\n",
    "app = Flask(__name__)\n",
    "diabetes = {0: 'Non-Diabetic', 1: 'Diabetic'}\n",
    "model = pickle.load(open('model.pkl','rb'))\n",
    "@app.route('/')\n",
    "def home():\n",
    "    return render_template('diabetes.html')\n",
    "\n",
    "@app.route('/predict1', methods=[\"POST\"])\n",
    "def predict():\n",
    "    data = [float(x) for x in request.form.values()]\n",
    "    features = [np.array(data)]\n",
    "    prediction = model.predict(features)\n",
    "    result = {'prediction': diabetes[prediction[0]]}\n",
    "    return jsonify(result)\n",
    "\n",
    "if __name__ == '__main__':\n",
    "    app.run(debug=True, use_reloader=False)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "127ef4e5-10fa-49b0-9b07-8a3a4df2f4e8",
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
   "version": "3.11.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
