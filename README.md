# **REAL TIME HAND GESTURE RECOGNITION TO VOICE CONVERSION WEB APP**
# _TABLE OF CONTENTS_
- *OVERVIEW*
- *OBJECTIVE*
- *WORKFLOW*
- *SCREENSHOTS and FEATURES*
- *TECHNOLOGIES AND TOOLS*
- *SETUP*
- *PROCESS*
- *RESULTS AND ACCURACY*
- *FUTURE WORKS*
### _OVERVIEW_
The "Hand Gesture Recognition to Voice Conversion Application"
represents a groundbreaking advancement in assistive technology, aimed at
facilitating seamless communication for individuals with hearing and speech
impairments. This innovative application harnesses the power of computer
vision and machine learning algorithms to translate sign language gestures into
synthesized speech in real-time3

## _OBJECTIVE_
The main objective of this work is to build a web application that enables
individuals with hearing and speech impairments to communicate effectively
and independently

## _WORKFLOW_
![Screenshot 2024-05-25 201758](https://github.com/SANJAYS07/Real-Time-Hand-Gesture-Recognition-to-Voice-Conversion-Web-Application/assets/126813962/cc36a9c3-553f-4315-abc8-ea5140becf29)

## _SCREENSHOTS and FEATURES_

### _LOGIN PAGE_
![Screenshot 2024-05-25 202036](https://github.com/SANJAYS07/Real-Time-Hand-Gesture-Recognition-to-Voice-Conversion-Web-Application/assets/126813962/68651577-0de4-425c-8d16-9552e124086c)
### _AFTER LOGGING IN_
![image](https://github.com/SANJAYS07/Real-Time-Hand-Gesture-Recognition-to-Voice-Conversion-Web-Application/assets/126813962/6060606b-fcf0-427d-bca4-0e3f768a903f)

### PREDICTION OF A SINGLE WORD AND AUDIO CONVERSION(PRESS START BUTTON)
![Screenshot 2024-05-13 195704](https://github.com/SANJAYS07/Real-Time-Hand-Gesture-Recognition-to-Voice-Conversion-Web-Application/assets/126813962/d56e8c04-4483-4ce3-9e93-58f169540dba)

### PREDICTION OF MULTIPLE WORDS , FORMING IT INTO A SENTENCE THEN MAKING IT GRAMMATICALLY CORRECT

##### EXAMPLE
- show gesture for *HOW* press _store words_ button
- Then show gesture for *YOU* press _store words_ button
- In stored sentences you have _HOW YOU_
- Now press __SPEAK__ button to speak . Here audio output will be generated additionaaly the **HOW YOU**  sentences will be grammatically corrected to **HOW ARE YOU** (* as shown in below screenshot) before the audio output
![Screenshot 2024-05-25 205110](https://github.com/SANJAYS07/Real-Time-Hand-Gesture-Recognition-to-Voice-Conversion-Web-Application/assets/126813962/69dcf9ea-8e90-43dc-9054-3ccfa4181790)

### __If you don't know gesture for a particular word press **HELP** button__
##### This is the web page view after pressing **HELP** button
![image](https://github.com/SANJAYS07/Real-Time-Hand-Gesture-Recognition-to-Voice-Conversion-Web-Application/assets/126813962/e9628ae2-e55c-4653-9c31-cfaf1593e5ba)

## _TECHNOLOGIES and TOOLS USED_
- Python
- opencv
- Tensorflow
- Mediapipe
- Pyttsx3
> ALGORITHM USED
- RANDOM FOREST CLASSIFIER
> __For Web Application__
- Python Flask
- HTML
- CSS
- Javascript
> __IDE__
- Visual Studio Code Text Editor

## _SETUP_
- Download Necessary Packages in VS code terminal
```
pip install opencv-python
pip install tensorflow
pip install mediapipe
pip install Flask
pip install pyttsx3
```
## _PROCESS_
> __Collecting images for creating Dataset__
- Run `collect_imgs.py` for collecting images through webcam using _opencv_
- The collected images will be stored in _Data_ Folder
> __Create a Dataset contains hand land marks using the collected images__
- Run `create_dataset.py`
- A `data.pickle` file will be created after running `create_dataset.py` file.
> __Training and Testing of Dataset__
- Run `training.py` file.
- Both training and testing is done using __RANDOM FOREST CLASSIFIER__ Algorithm
- **Workflow of _Random Forest classifier_ Algorithm**
  ![Screenshot 2024-05-25 214421](https://github.com/SANJAYS07/Real-Time-Hand-Gesture-Recognition-to-Voice-Conversion-Web-Application/assets/126813962/232f3270-8510-4916-8aff-41306aa1d135)

- A `model.p` file will be created after running `training.py` file.
> __Running project in local server(WEB APP)__
- Run `app.py` file.
- `http://127.0.0.1:5000/` Paste the address in chrome or Microsoft Edge.
- This will open up the gesture recognition window in the webpage.
## _RESULTS and ACCURACY_
#### __Our model was able to predict the 50 Words in the Dataset with a prediction accuracy >93%.__
![Screenshot 2024-05-25 215615](https://github.com/SANJAYS07/Real-Time-Hand-Gesture-Recognition-to-Voice-Conversion-Web-Application/assets/126813962/2a3a236a-fbaa-4153-b0c3-6453d859cf53)
## _FUTURE WORKS_
- Deploy the project on cloud and create an API for using it.
- Developing a video processing application.
- Incorporate feedback mechanism to make the model more robust
- Add more sign languages

  


