
# Medication Recommendation System 💊🩺

## Disclaimer ⚠️

- For **educational purposes only**.
- **Do not use** for personal medication decisions.
- Always **consult a healthcare professional** before following any recommendations.
- The system's suggestions do not replace **medical advice**.
- The creators are not liable for any consequences from using this system.
#
#

### App Link - [Live](https://medication-recommendation.onrender.com/index.html)

This repository contains a project focused on building a recommendation system for providing personalized medication suggestions based on user inputs, medical history, and symptoms.

## Project Overview 🌟

The **Medication Recommendation System** is designed to assist healthcare professionals and patients by offering tailored medication suggestions. It leverages advanced machine learning algorithms and medical knowledge to provide reliable and safe recommendations.

## Screenshots

![App Screenshot](https://raw.githubusercontent.com/Prathmeshpawar21/__resources/refs/heads/main/SS/medication3-modified.png)



## Features 🎯

- Input patient symptoms
- Get personalized medication recommendations.
- AI-driven analysis for drug interactions and contraindications.
- User-friendly interface for both professionals and patients.

## Technologies Used 🛠️

- **Python**
- **Libraries:** Scikit-learn, Pandas, NumPy, PyTorch/Hugging Face Transformers
- **Frontend:** Streamlit, Bootstrap
- **Frameworks:** Flask, FastAPI
- **Database:** SQLite or PostgreSQL for patient data storage
- **Model Pipeline:**  
  - **Embedding Model:** `ClinicalBERT` – A transformer model fine-tuned for clinical text analysis.  
  - **Recommendation Model:** Gradient Boosting Algorithm for personalized medication prediction.  

## Project Structure 🗂️

```
├── model
│   └── Model.pkl
├── notebook
│   └── dataset
│       ├── Symptom-severity.csv
│       ├── Training.csv
│       ├── description.csv
│       ├── diets.csv
│       ├── medications.csv
│       ├── symtoms_df.csv
│       └── workout_df.csv
├── templates
│   ├── about.html
│   ├── contact.html
│   ├── departments.html
│   └── index.html
├── .gitignore
├── LICENSE
├── README.md
├── app.py
├── index.py
├── requirements.txt
├── research.py
├── vercel.json
└── wsgi.py
```

## Setup Instructions ⚙️

1. Clone the repository:
   ```bash
   git clone https://github.com/Prathmeshpawar21/DS-Medicine-Recommendation-System.git
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
    **OR**

3. Create and activate a virtual environment using Anaconda:
   ```bash
   conda create -n venv python=3.13.1 -y
   conda activate venv
   ```

4. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

5. Run the application:
   ```bash
   python app.py
   ```

6. Open your browser and navigate to `http://127.0.0.1:<port>`.

## How It Works 🧠

1. **User Input:** Enter symptoms.
2. **Data Processing:** Inputs are preprocessed and tokenized for analysis.
3. **Embedding and Prediction:** Symptoms and history are embedded and recommendation model generates medication suggestions.
4. **Output:**  
   - **Description**  
   - **Diet Recommendations**  
   - **Recommended Medicines**  
   - **Precautions**  
   - **Work Recommendations**


## Results 🏆

- **Accuracy:** High precision in medication recommendations.
- **Efficiency:** Rapid processing of patient data for quick outputs.

## Future Improvements 🚀

- Integrate real-time drug databases for up-to-date recommendations.
- Add support for multilingual input.
- Implement a mobile application interface.
- Incorporate patient feedback for model refinement.

## Contributing 🤝

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch-name`).
3. Commit your changes (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature-branch-name`).
5. Open a Pull Request.

## 🔗 Links

[![portfolio](https://img.shields.io/badge/my_portfolio-000?style=for-the-badge&logo=ko-fi&logoColor=white)](https://prathameshpawar-mu.vercel.app/)
[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/prathameshpawar21/)

## License 📜

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
