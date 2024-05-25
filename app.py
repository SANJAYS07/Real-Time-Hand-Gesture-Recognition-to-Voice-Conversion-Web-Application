import os
import re
from flask import Flask, render_template, Response, request, jsonify, send_from_directory, session
import cv2
import mediapipe as mp
import numpy as np
import pickle

app = Flask(__name__, static_folder='pictures')
app.secret_key = 'your_secret_key'  # Necessary for session management

# Load the hand gesture recognition model
with open('./model.p', 'rb') as file:
    model_dict = pickle.load(file)
    model = model_dict['model']

# Initialize MediaPipe Hands
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(static_image_mode=False, min_detection_confidence=0.5, max_num_hands=2)
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles

labels_dict = {0: 'hello',1:'goodbye',2:'stop',3:'Thankyou',4:'love',5:'i',6:'you',7:'okay',8:'water',9:'think',10:'why',11:'what',12:'how',13:'where',14:'when',15:'sleep',16:'name',17:'name',18:'Bad',19:'happy',20:'good',21:'friend',22:'home',23:'need',24:'hate',25:'which',26:'big',27:'food',28:'morning',29:'speak',30:'Go',31:'Learn',32:'Read',33:'Touch',34:'Hear',35:'Feel',36:'Understand',37:'Forget',38:'Funny',39:'Small',40:'Strong',41:'Excited',42:'Beautiful',43:'Silence',44:'Wait',45:'Help',46:'Finish',47:'Angry',48:'Believe',49:'Dream',50:'See'}
stored_sentence = ""
last_predicted_label = ""

def gen_frames():  # Generate frame by frame from camera
    global last_predicted_label
    cap = cv2.VideoCapture(0)
    while True:
        success, frame = cap.read()
        if not success:
            break
        else:
            frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            results = hands.process(frame_rgb)
            if results.multi_hand_landmarks:
                for hand_landmarks in results.multi_hand_landmarks:
                    mp_drawing.draw_landmarks(
                        frame,
                        hand_landmarks,
                        mp_hands.HAND_CONNECTIONS,
                        mp_drawing_styles.get_default_hand_landmarks_style(),
                        mp_drawing_styles.get_default_hand_connections_style())

                    data_aux = []
                    x_ = []
                    y_ = []
                    for landmark in hand_landmarks.landmark:
                        x = landmark.x
                        y = landmark.y
                        x_.append(x)
                        y_.append(y)

                    for landmark in hand_landmarks.landmark:
                        x = landmark.x
                        y = landmark.y
                        data_aux.append(x - min(x_))
                        data_aux.append(y - min(y_))

                    data_aux_subset = data_aux[:42]
                    prediction = model.predict([np.asarray(data_aux_subset)])
                    last_predicted_label = labels_dict.get(int(prediction[0]), '')

                    cv2.putText(frame, last_predicted_label, (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)

            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/get_current_label')
def get_current_label():
    global last_predicted_label
    return jsonify(current_label=last_predicted_label)

@app.route('/append_label', methods=['POST'])
def append_label():
    global stored_sentence, last_predicted_label
    if last_predicted_label and last_predicted_label not in stored_sentence.split()[-5:]:
        stored_sentence += last_predicted_label + " "
    return jsonify(status="success", sentence=stored_sentence)

@app.route('/correct_and_speak', methods=['POST'])
def correct_and_speak():
    global stored_sentence
    corrected_sentence = correct_grammar(stored_sentence.strip())
    return jsonify(status="success", corrected_sentence=corrected_sentence)

def correct_grammar(sentence):
    # Add your custom sentence transformations here
    if sentence.lower().strip() == 'stop think you speak':
        return 'Stop, think before you speak'
    if sentence.lower().strip() == 'how you':
        return 'How are you?'
    if sentence.lower().strip() == 'what you name':
        return 'what is your name?'
    if sentence.lower().strip() == 'what you think':
        return 'what do you think?'
    if sentence.lower().strip()=='i think you speak':
        return 'I Think You can Speak Now'
    if sentence.lower().strip() == 'you happy home':
        return 'Are you happy at home?'
    if sentence.lower().strip() == 'thank you food':
        return 'Thank you for the food.'
    if sentence.lower().strip() == 'why you hate mornings':
        return 'Why do you hate mornings?'
    if sentence.lower().strip() == 'water feel good':
        return 'Water makes me feel good.'
    if sentence.lower().strip() == 'how i help you':
        return 'How can I help you?'
    if sentence.lower().strip() == 'when you finish':
        return 'When will you finish?'
    if sentence.lower().strip() == 'what you name':
        return 'What is your Name?'
    if sentence.lower().strip() == 'you need water':
        return 'Do you need Water?'
    if sentence.lower().strip() == 'i need think':
        return 'I Need to think'
    if sentence.lower().strip() == 'i speak':
        return 'Shall I Speak'
    if sentence.lower().strip() == 'i need speak':
        return 'I Need to Speak'
    else:
        return sentence

   # for ungrammatical, grammatical in corrections.items():
      #  if ungrammatical in sentence:
     #       sentence = sentence.replace(ungrammatical, grammatical)
     #       break
    #return sentence

@app.route('/reset_sentence', methods=['POST'])
def reset_sentence():
    global stored_sentence
    stored_sentence = ""
    return jsonify(status="success", sentence="")

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/options', methods=['POST'])
def options():
    username = request.form['username']
    session['username'] = username  # Storing username in session
    return render_template('options.html', username=username)

@app.route('/option')
def option():
    username = session.get('username', 'Guest')  # Assuming you store username in session
    return render_template('options.html', username=username)

@app.route('/camera')
def camera():
    username = session.get('username', 'Guest')  # Retrieve username from session
    labels_dict[17] = username 
    return render_template('camera.html', username=username)

@app.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
         # Retrieve user input and normalize it
        raw_image_name = request.form['image_name']
        # Normalize by removing non-alphanumeric characters and converting to lower case
        normalized_image_name = re.sub(r'[^a-zA-Z0-9]', '', raw_image_name).lower()

        # Search directory for matching files ignoring case and non-alphanumeric characters
        for filename in os.listdir(app.static_folder):
            # Normalize filenames in the directory similarly
            normalized_filename = re.sub(r'[^a-zA-Z0-9]', '', filename).lower()
            if normalized_filename.startswith(normalized_image_name):
                # If a match is found, send the file
                return send_from_directory(app.static_folder, filename)

        # If no file is found after checking all files, return an error message
        return "Image not found", 404

    return render_template('help.html')

@app.route('/video_feed')
def video_feed():
    return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/help')
def help_page():
    # Render a help page or return help information
    return render_template('help.html')

if __name__ == '__main__':
    app.run(debug=True, threaded=True)
