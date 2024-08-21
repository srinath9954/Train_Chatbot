import spacy
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Load spaCy model
nlp = spacy.load("en_core_web_sm")

train_data = [
    {"train_number": "12301", "name": "Rajdhani Express", "from": "New Delhi", "to": "Mumbai", "availability": 50},
    {"train_number": "12951", "name": "Mumbai Rajdhani", "from": "Mumbai", "to": "New Delhi", "availability": 40},
    {"train_number": "12002", "name": "Bhopal Shatabdi", "from": "Bhopal", "to": "New Delhi", "availability": 60},
    {"train_number": "12626", "name": "Kerala Express", "from": "New Delhi", "to": "Trivandrum", "availability": 70},
    {"train_number": "12295", "name": "Sanghamitra Express", "from": "Bangalore", "to": "Patna", "availability": 80},
    {"train_number": "12505", "name": "North East Express", "from": "Guwahati", "to": "New Delhi", "availability": 45},
    {"train_number": "12860", "name": "Gitanjali Express", "from": "Mumbai", "to": "Kolkata", "availability": 55},
    {"train_number": "12623", "name": "Trivandrum Mail", "from": "Chennai", "to": "Trivandrum", "availability": 65},
    {"train_number": "12903", "name": "Golden Temple Mail", "from": "Mumbai", "to": "Amritsar", "availability": 75},
    {"train_number": "12634", "name": "Kanyakumari Express", "from": "Bangalore", "to": "Kanyakumari", "availability": 85},
    {"train_number": "12953", "name": "August Kranti Rajdhani", "from": "Mumbai", "to": "New Delhi", "availability": 50},
    {"train_number": "12050", "name": "Gatimaan Express", "from": "New Delhi", "to": "Agra", "availability": 40},
    {"train_number": "12839", "name": "Howrah Mail", "from": "Chennai", "to": "Kolkata", "availability": 60},
    {"train_number": "12297", "name": "Sampoorna Kranti", "from": "Patna", "to": "New Delhi", "availability": 70},
    {"train_number": "12137", "name": "Punjab Mail", "from": "Mumbai", "to": "Firozpur", "availability": 80},
    {"train_number": "12681", "name": "Manduadih Express", "from": "Chennai", "to": "Varanasi", "availability": 90},
    {"train_number": "12657", "name": "Chennai Express", "from": "Mumbai", "to": "Chennai", "availability": 45},
    {"train_number": "12101", "name": "Jnaneswari Super Deluxe", "from": "Mumbai", "to": "Kolkata", "availability": 55},
    {"train_number": "12851", "name": "Bilaspur Express", "from": "Bilaspur", "to": "Bhubaneswar", "availability": 65},
    {"train_number": "12663", "name": "Hazrat Nizamuddin Garib Rath", "from": "Chennai", "to": "New Delhi", "availability": 75},
    {"train_number": "12163", "name": "Chennai LTT Express", "from": "Lokmanya Tilak", "to": "Chennai", "availability": 85},
    {"train_number": "12303", "name": "Poorva Express", "from": "Kolkata", "to": "New Delhi", "availability": 50},
    {"train_number": "12280", "name": "Taj Express", "from": "New Delhi", "to": "Agra", "availability": 40},
    {"train_number": "12802", "name": "Purushottam Express", "from": "New Delhi", "to": "Puri", "availability": 60},
    {"train_number": "12150", "name": "Dadar Express", "from": "Dadar", "to": "Bhopal", "availability": 70},
    {"train_number": "12649", "name": "Sampark Kranti", "from": "Bangalore", "to": "Hazrat Nizamuddin", "availability": 80},
    {"train_number": "12617", "name": "Mangala Lakshadweep Express", "from": "Ernakulam", "to": "Hazrat Nizamuddin", "availability": 90},
    {"train_number": "12925", "name": "Paschim Express", "from": "Mumbai", "to": "Amritsar", "availability": 45},
    {"train_number": "12629", "name": "Karnataka Express", "from": "Bangalore", "to": "New Delhi", "availability": 55},
    {"train_number": "12647", "name": "Kongu Express", "from": "Coimbatore", "to": "Hazrat Nizamuddin", "availability": 65},
    {"train_number": "12631", "name": "Netravati Express", "from": "Thiruvananthapuram", "to": "Lokmanya Tilak", "availability": 75},
    {"train_number": "12701", "name": "Hussainsagar Express", "from": "Hyderabad", "to": "Mumbai", "availability": 85},
    {"train_number": "12655", "name": "Nizamuddin SF Express", "from": "Madurai", "to": "Hazrat Nizamuddin", "availability": 50},
    {"train_number": "12610", "name": "Navjeevan Express", "from": "Chennai", "to": "Ahmedabad", "availability": 40},
    {"train_number": "12723", "name": "Telangana Express", "from": "Hyderabad", "to": "New Delhi", "availability": 60},
    {"train_number": "12621", "name": "Tamil Nadu Express", "from": "Chennai", "to": "Mumbai", "availability": 70},
    {"train_number": "12603", "name": "Hyderabad Express", "from": "Hyderabad", "to": "Howrah", "availability": 80},
    {"train_number": "12781", "name": "Goa Express", "from": "Vasco Da Gama", "to": "Hazrat Nizamuddin", "availability": 90},
    {"train_number": "12833", "name": "Howrah Express", "from": "Ahmedabad", "to": "Howrah", "availability": 45},
    {"train_number": "12903", "name": "Golden Temple Mail", "from": "Mumbai", "to": "Amritsar", "availability": 55},
    {"train_number": "12313", "name": "Sealdah Rajdhani", "from": "Sealdah", "to": "New Delhi", "availability": 65},
    {"train_number": "12018", "name": "Dehradun Shatabdi", "from": "New Delhi", "to": "Dehradun", "availability": 75},
    {"train_number": "12904", "name": "Golden Temple Mail", "from": "Amritsar", "to": "Mumbai", "availability": 85},
    {"train_number": "12925", "name": "Paschim Express", "from": "Amritsar", "to": "Mumbai", "availability": 50},
    {"train_number": "12952", "name": "Mumbai Rajdhani", "from": "New Delhi", "to": "Mumbai", "availability": 40},
    {"train_number": "12301", "name": "Howrah Rajdhani", "from": "Howrah", "to": "New Delhi", "availability": 60},
    {"train_number": "12008", "name": "Shatabdi Express", "from": "Mysore", "to": "Chennai", "availability": 70},
    {"train_number": "12615", "name": "Grand Trunk Express", "from": "Chennai", "to": "New Delhi", "availability": 80},
    {"train_number": "12009", "name": "Shatabdi Express", "from": "Bangalore", "to": "Chennai", "availability": 90},
]


# Session store
sessions = {}

def extract_entities(message):
    doc = nlp(message)
    entities = {"GPE": [], "DATE": [], "CARDINAL": []}
    for ent in doc.ents:
        if ent.label_ in entities:
            entities[ent.label_].append(ent.text)
    return entities

def detect_intent(message):
    message = message.lower()
    if "book" in message:
        return "book_ticket"
    elif "availability" in message or "available" in message:
        return "check_availability"
    elif "cancel" in message:
        return "cancel_booking"
    elif "confirm" in message:
        return "confirm_booking"
    else:
        return "book_ticket"

@app.route('/api/chatbot', methods=['POST'])
def chatbot():
    user_message = request.json.get('message', '').lower()
    session_id = request.json.get('session_id')
    
    if not session_id or session_id not in sessions:
        session_id = str(len(sessions) + 1)  # Generate a new session ID
        sessions[session_id] = {"step": 0, "source": None, "destination": None}

    step = sessions[session_id]["step"]
    intent = detect_intent(user_message)

    if intent == "book_ticket":
        if step == 0:
            sessions[session_id]["step"] = 1
            return jsonify({"reply": "Sure, I can help you book a ticket. Please provide the source city (e.g., Chennai).", "session_id": session_id})
        elif step == 1:
            sessions[session_id]["source"] = user_message.capitalize()
            sessions[session_id]["step"] = 2
            return jsonify({"reply": "Got it. Please provide the destination city (e.g., Mumbai).", "session_id": session_id})
        elif step == 2:
            sessions[session_id]["destination"] = user_message.capitalize()
            source = sessions[session_id]["source"]
            print(source)
            destination = sessions[session_id]["destination"]
            available_trains = [train for train in train_data if train["from"].lower() == source.lower() and train["to"].lower() == destination.lower()]
            if available_trains:
                train_list = [f"{train['name']} ({train['train_number']})" for train in available_trains]
                sessions[session_id]["step"] = 0  # Reset for next interaction
                return jsonify({"reply": f"Available trains from {source} to {destination}: {', '.join(train_list)}.", "session_id": session_id})
            else:
                sessions[session_id]["step"] = 0  # Reset for next interaction
                return jsonify({"reply": f"No trains available from {source} to {destination}.", "session_id": session_id})
    else:
        return jsonify({"reply": "Sorry, I didn't understand that. Can you please clarify?", "session_id": session_id})

if __name__ == '__main__':
    app.run(debug=True)
