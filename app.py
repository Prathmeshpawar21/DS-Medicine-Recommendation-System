from flask import Flask, render_template, request,redirect,jsonify
from research import *
import ast
from fuzzywuzzy import process
import difflib


app = Flask(__name__)

symptom_list = [
    'itching', 'skin_rash', 'nodal_skin_eruptions', 'continuous_sneezing', 'shivering', 'chills',
    'joint_pain', 'stomach_pain', 'acidity', 'ulcers_on_tongue', 'muscle_wasting', 'vomiting', 
    'burning_micturition', 'spotting_urination', 'fatigue', 'weight_gain', 'anxiety', 'cold_hands_and_feets', 
    'mood_swings', 'weight_loss', 'restlessness', 'lethargy', 'patches_in_throat', 'irregular_sugar_level',
    'cough', 'high_fever', 'sunken_eyes', 'breathlessness', 'sweating', 'dehydration', 'indigestion',
    'headache', 'yellowish_skin', 'dark_urine', 'nausea', 'loss_of_appetite', 'pain_behind_the_eyes', 'back_pain',
    'constipation', 'abdominal_pain', 'diarrhoea', 'mild_fever', 'yellow_urine', 'yellowing_of_eyes', 
    'acute_liver_failure', 'fluid_overload', 'swelling_of_stomach', 'swelled_lymph_nodes', 'malaise',
    'blurred_and_distorted_vision', 'phlegm', 'throat_irritation', 'redness_of_eyes', 'sinus_pressure', 
    'runny_nose', 'congestion', 'chest_pain', 'weakness_in_limbs', 'fast_heart_rate', 'pain_during_bowel_movements', 
    'pain_in_anal_region', 'bloody_stool', 'irritation_in_anus', 'neck_pain', 'dizziness', 'cramps', 'bruising',
    'obesity', 'swollen_legs', 'swollen_blood_vessels', 'puffy_face_and_eyes', 'enlarged_thyroid', 'brittle_nails',
    'swollen_extremeties', 'excessive_hunger', 'extra_marital_contacts', 'drying_and_tingling_lips', 'slurred_speech',
    'knee_pain', 'hip_joint_pain', 'muscle_weakness', 'stiff_neck', 'swelling_joints', 'movement_stiffness',
    'spinning_movements', 'loss_of_balance', 'unsteadiness', 'weakness_of_one_body_side', 'loss_of_smell',
    'bladder_discomfort', 'foul_smell_of_urine', 'continuous_feel_of_urine', 'passage_of_gases', 'internal_itching',
    'toxic_look_(typhos)', 'depression', 'irritability', 'muscle_pain', 'altered_sensorium', 'red_spots_over_body',
    'belly_pain', 'abnormal_menstruation', 'dischromic_patches', 'watering_from_eyes', 'increased_appetite',
    'polyuria', 'family_history', 'mucoid_sputum', 'rusty_sputum', 'lack_of_concentration', 'visual_disturbances',
    'receiving_blood_transfusion', 'receiving_unsterile_injections', 'coma', 'stomach_bleeding', 'distention_of_abdomen',
    'history_of_alcohol_consumption', 'fluid_overload.1', 'blood_in_sputum', 'prominent_veins_on_calf', 'palpitations',
    'painful_walking', 'pus_filled_pimples', 'blackheads', 'scurring', 'skin_peeling', 'silver_like_dusting', 
    'small_dents_in_nails', 'inflammatory_nails', 'blister', 'red_sore_around_nose', 'yellow_crust_ooze', 'prognosis'
]


@app.route("/")
def home_redirect():
    return redirect("/index.html")  # Redirects `/` to `/index.html`

@app.route('/index.html', methods=['POST', 'GET'])
def index():
    userInputSymptomList = ""
    PredictedPersonDisease = ""
    desc, diet, med, prec, work = "", [], [], [], []
    matched_symptoms = []
    error_message = ""

    if request.method == 'POST':
        userInputSymptomList = request.form.get("text").strip()
        if userInputSymptomList.endswith(','):
            userInputSymptomList = userInputSymptomList.rstrip(',')
            
        print('user input list:',userInputSymptomList)
        
        # Split the user input into individual symptoms and check each one
        symptoms = [s.strip() for s in userInputSymptomList.split(',')]


        # Check for fuzzy matching
        for symptom in symptoms:
            if symptom not in symptom_list:
                matches = process.extract(symptom, symptom_list, limit=3)  # Top 3 closest matches
                matched_symptoms.append((symptom, matches))
            else:
                matched_symptoms.append((symptom, [("Exact match", 100)]))

        # If symptoms are valid, proceed to prediction
        if all(symptom in symptom_list for symptom in symptoms):
            PredictedPersonDisease = get_prediction(userInputSymptomList)
            
            # Assuming these values are returned as string representations of lists
            desc, diet, med, prec, work = otherDetails(PredictedPersonDisease)
            
            # Convert string representations to actual lists using ast.literal_eval
            if isinstance(diet, str):
                diet = ast.literal_eval(diet)
            if isinstance(med, str):
                med = ast.literal_eval(med)
            if isinstance(prec, str):
                prec = ast.literal_eval(prec)
            if isinstance(work, str):
                work = ast.literal_eval(work)
        else:
            error_message = "Some symptoms are invalid. Please check the spelling and try again."
    
    return render_template("index.html", 
                           userInputSymptomList=userInputSymptomList, 
                           PredictedPersonDisease=PredictedPersonDisease, 
                           desc=desc, diet=diet, med=med, prec=prec, work=work, 
                           matched_symptoms=matched_symptoms, error_message=error_message)



@app.route('/get_suggestions', methods=['POST'])
def get_suggestions():
    data = request.get_json()
    query = data.get('query', '').lower()  # Get query from the request body

    # Ensure there is a valid query
    if not query:
        return jsonify({'suggestions': []})

    # Get symptoms that contain the query (case-insensitive)
    suggestions = [symptom for symptom in symptom_list if query in symptom.lower()]

    return jsonify({'suggestions': suggestions[:10]})  # Return top 10 suggestions






@app.route("/about.html")
def about():
    return render_template("about.html")

@app.route("/departments.html")
def departments():
    return render_template("departments.html")

@app.route("/contact.html")
def contact():
    return render_template("contact.html")








    
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
    