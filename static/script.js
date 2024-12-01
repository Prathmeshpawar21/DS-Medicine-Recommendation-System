// Function to get suggestions dynamically based on the last symptom
function getSuggestions() {
    var input = document.getElementById('symptomInput').value.trim();

    // Split the input to focus on the last symptom
    var symptoms = input.split(',').map(s => s.trim());
    var lastSymptom = symptoms[symptoms.length - 1];

    // Only trigger suggestions if the last symptom length is more than 1 character
    if (lastSymptom.length > 1) {
        // Send the last symptom to the backend to fetch suggestions
        fetch('/get_suggestions', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ query: lastSymptom })
        })
        .then(response => response.json())
        .then(data => {
            var suggestions = data.suggestions;
            var suggestionList = "";

            // Check if there are any suggestions
            if (suggestions.length > 0) {
                suggestions.forEach(function(item) {
                    suggestionList += `<div class="suggestion" onclick="selectSuggestion('${item}')">${item},</div>`;
                });
                document.getElementById('suggestions').innerHTML = suggestionList;  // Show suggestions
            } else {
                document.getElementById('suggestions').innerHTML = "";  // Clear if no suggestions
            }
        })
        .catch(error => {
            console.error("Error fetching suggestions:", error);
        });
    } else {
        // If the last symptom is less than 2 characters, clear suggestions
        document.getElementById('suggestions').innerHTML = "";
    }
}

// Function to select a suggestion and append it to the input field
function selectSuggestion(symptom) {
    var inputField = document.getElementById('symptomInput');
    var currentValue = inputField.value;

    // Split the input to append the selected symptom correctly
    var symptoms = currentValue.split(',').map(s => s.trim());
    symptoms[symptoms.length - 1] = symptom;  // Replace the last symptom with the selected one

    // Join symptoms back with a comma and space
    inputField.value = symptoms.join(', ') + ', ';
    document.getElementById('suggestions').innerHTML = "";  // Clear suggestions after selection
}

// Attach the 'input' event listener to trigger suggestions on each keypress
document.getElementById('symptomInput').addEventListener('input', function() {
    getSuggestions();
});


document.addEventListener("DOMContentLoaded", function() {
    // Ensure the page stays at the form position if the hash exists
    if (window.location.hash === "#get-medicines") {
        document.querySelector("#get-medicines").scrollIntoView({ behavior: "smooth" });
    }
});



function adjustSuggestionsWidth() {
    var inputBox = document.getElementById('symptomInput');
    var suggestionsContainer = document.getElementById('suggestions');

    // Set the width of the suggestions container to match the input box
    suggestionsContainer.style.width = inputBox.offsetWidth + "px";
}

// Call this function whenever the page loads or the input box size changes
window.onload = adjustSuggestionsWidth;
window.onresize = adjustSuggestionsWidth;


function redirectToIndex() {
    window.location.href = "/index.html#get-medicines";
}