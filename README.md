
# 🧮 Employee Salary Prediction

A minimal and clean **Streamlit app** that predicts employee salaries using HR data and a Random Forest model. This project was built as part of the **AICTE IBM project** initiative.

🔗 **Live App:** [aicteprojectibm.streamlit.app](https://aicteprojectibm.streamlit.app/)

---

## 📊 Features

- Predicts salary based on key employee attributes:
  - Gender
  - Department ID
  - Performance Score
  - Satisfaction Level
  - Special Projects
  - Absences
- Simple and clean UI built with **Streamlit**
- Minimal and deployment-ready setup

---

## 🛠️ Tech Stack

- Python
- Streamlit
- Scikit-learn
- Pandas
- Joblib

---

## 🚀 How to Run Locally

1. Clone the repo:

```bash
git clone https://github.com/abinayagoudjandhyala/employee-salary-prediction
cd employee-salary-prediction
````

2. Install requirements:

```bash
pip install -r requirements.txt
```

3. Train the model:

```bash
python model.py
```

4. Run the Streamlit app:

```bash
streamlit run app.py
```

---

## 📝 Dataset

The app uses a cleaned version of the `HRDataset_v14.csv` dataset with selected numeric features for salary prediction.

---

## 📦 Deployment

To deploy this app on **Streamlit Cloud**:

* Upload:

  * `app.py`
  * `model.py`
  * `HRDataset_v14.csv`
  * `requirements.txt`
  * `salary_model.pkl` (after running `model.py`)
* Streamlit will auto-detect and launch the app.

---

## 🙌 Acknowledgments

Built for the **AICTE IBM Project**
Deployed using **Streamlit Cloud**

---

## 📜 License

This project is open source under the [MIT License](LICENSE).


