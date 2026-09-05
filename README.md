# Rectangular Patch Antenna Dimension Predictor
Machine learning-based microstrip patch antenna design system that uses XGBoost to predict antenna dimensions from frequency, dielectric constant, substrate height, loss tangent, and copper thickness, with a Streamlit interface for prediction and 3D visualization.


A machine learning-based application for predicting the dimensions of a **rectangular microstrip patch antenna** from its electromagnetic and substrate specifications.

The project uses **XGBoost regression** to predict the required patch and ground-plane dimensions and provides an interactive **Streamlit web interface** for making predictions.

---

## 🚀 Project Overview

Designing a rectangular patch antenna requires determining suitable physical dimensions based on parameters such as:

* Operating frequency
* Dielectric constant of the substrate
* Substrate height
* Loss tangent
* Copper thickness

This project generates a dataset using standard rectangular patch antenna design equations and trains an **XGBoost Multi-Output Regression model** to predict antenna dimensions.

The trained model is integrated into a Streamlit application where users can enter antenna specifications and obtain predicted dimensions.

---

## ✨ Features

* 📊 Generates a dataset of **10,000 antenna samples**
* 📐 Uses rectangular patch antenna design equations for dataset generation
* 🤖 Uses **XGBoost Regression**
* 🔢 Performs multi-output regression
* 📏 Predicts four antenna dimensions:

  * Patch Width
  * Patch Length
  * Ground Width
  * Ground Length
* 📈 Evaluates the model using:

  * R² Score
  * Mean Absolute Error (MAE)
  * Root Mean Squared Error (RMSE)
* 💾 Saves the trained model using Joblib
* 🌐 Provides an interactive Streamlit interface

---

## 🧠 Machine Learning Approach

### Input Features

The model takes five antenna parameters as input:

| Feature               | Description                  | Unit |
| --------------------- | ---------------------------- | ---- |
| `Frequency_GHz`       | Operating frequency          | GHz  |
| `Dielectric_Constant` | Relative dielectric constant | —    |
| `Height_mm`           | Substrate height             | mm   |
| `Loss_Tangent`        | Dielectric loss tangent      | —    |
| `Copper_Thickness_mm` | Copper thickness             | mm   |

### Output Targets

The model predicts four physical dimensions:

| Target             | Description         | Unit |
| ------------------ | ------------------- | ---- |
| `Patch_Width_mm`   | Patch width         | mm   |
| `Patch_Length_mm`  | Patch length        | mm   |
| `Ground_Width_mm`  | Ground-plane width  | mm   |
| `Ground_Length_mm` | Ground-plane length | mm   |

---

## 📐 Dataset Generation

The project generates **10,000 synthetic antenna samples**.

The input parameters are randomly generated within defined ranges:

* Frequency: **1–10 GHz**
* Dielectric constant: **2.2–10.2**
* Substrate height: **0.8–3.2 mm**
* Loss tangent: **0.0009–0.03**
* Copper thickness: **0.017, 0.035, or 0.070 mm**

The corresponding patch and ground dimensions are calculated using rectangular microstrip patch antenna equations.

The generated dataset is saved as:

```text
antenna_dataset.csv
```

---

## 🤖 Model

The project uses:

```text
XGBRegressor
      ↓
MultiOutputRegressor
      ↓
Predicted Antenna Dimensions
```

### XGBoost Configuration

```text
objective        = reg:squarederror
n_estimators     = 500
learning_rate    = 0.05
max_depth        = 6
subsample        = 0.8
colsample_bytree = 0.8
random_state     = 42
```

The dataset is divided into:

```text
80% → Training Data
20% → Testing Data
```

---

## 📊 Model Evaluation

The model is evaluated using three metrics:

### R² Score

Measures how well the model explains the variation in the target values.

### MAE

Measures the average absolute difference between the predicted and actual dimensions.

### RMSE

Measures the square root of the average squared prediction error.

The evaluation is performed on the test dataset.

---

## 💾 Trained Model

The trained model is saved using Joblib:

```text
antenna_model.pkl
```

The saved model can then be loaded by the Streamlit application to make predictions without retraining the model.

---

## 🌐 Streamlit Application

The Streamlit interface allows users to enter:

```text
Frequency (GHz)
Dielectric Constant
Substrate Height (mm)
Loss Tangent
Copper Thickness (mm)
```

After clicking **Predict Dimensions**, the application displays:

```text
Patch Width
Patch Length
Ground Width
Ground Length
```

in millimetres.

---

## 🖥️ Project Structure

```text
Rectangular-Patch-Antenna-Predictor/
│
├── app.py
├── antenna_training.ipynb
├── antenna_dataset.csv
├── antenna_model.pkl
├── requirements.txt
└── README.md
```

### File Description

| File                     | Description                           |
| ------------------------ | ------------------------------------- |
| `app.py`                 | Streamlit application                 |
| `antenna_training.ipynb` | Dataset generation and model training |
| `antenna_dataset.csv`    | Generated antenna dataset             |
| `antenna_model.pkl`      | Trained XGBoost model                 |
| `requirements.txt`       | Required Python packages              |
| `README.md`              | Project documentation                 |

---

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/YOUR_REPOSITORY.git
```

```bash
cd YOUR_REPOSITORY
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

For Windows:

```bash
venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 📦 Requirements

The project requires:

```text
numpy
pandas
scikit-learn
xgboost
joblib
streamlit
```

For reproducible results, the package versions used during model training can be specified in `requirements.txt`.

---

## ▶️ Run the Application

After installing the dependencies, run:

```bash
streamlit run app.py
```

The Streamlit application will start locally and provide a URL through which the antenna dimension predictor can be accessed.

---

## 🔬 Example Input

An example set of antenna specifications is:

| Parameter           |    Value |
| ------------------- | -------: |
| Frequency           |  2.4 GHz |
| Dielectric Constant |      4.4 |
| Substrate Height    |   1.6 mm |
| Loss Tangent        |     0.02 |
| Copper Thickness    | 0.035 mm |

The application uses these parameters to generate the predicted antenna dimensions.

---

## 🔄 Project Workflow

```text
Antenna Specifications
        │
        ▼
Dataset Generation
        │
        ▼
10,000 Samples
        │
        ▼
Train / Test Split
        │
        ▼
XGBoost Regression
        │
        ▼
Model Evaluation
        │
        ▼
Saved Model
        │
        ▼
Streamlit Application
        │
        ▼
User Input
        │
        ▼
Predicted Dimensions
```

---

## 🛠️ Technologies Used

* Python
* NumPy
* Pandas
* Scikit-learn
* XGBoost
* Joblib
* Streamlit
* Jupyter Notebook

---

## 🎯 Applications

This project can be used for:

* Rapid antenna dimension estimation
* Antenna design exploration
* RF and microwave engineering experiments
* Educational purposes
* Studying the relationship between substrate parameters and antenna dimensions
* Demonstrating the use of machine learning in engineering applications

---

## ⚠️ Limitations

The training dataset is generated using analytical rectangular patch antenna equations rather than measured or full-wave electromagnetic simulation data.

Therefore, the predicted dimensions should be validated using appropriate electromagnetic simulation software or experimental measurements before practical fabrication.

The current model predicts physical dimensions only and does not directly predict:

* Return loss
* VSWR
* Gain
* Bandwidth
* Radiation pattern
* Efficiency

---

## 🔮 Future Improvements

* Add electromagnetic simulation data
* Add measured antenna data
* Include antenna performance parameters
* Add 3D visualization of the predicted antenna
* Compare XGBoost with other regression algorithms
* Add prediction error visualization
* Add downloadable design reports
* Deploy the Streamlit application online

---

## 👩‍💻 Author

**Nishi Vatsha**

Computer Science & Engineering — Data Science

---

## 📄 License

This project is intended for educational and research purposes.
