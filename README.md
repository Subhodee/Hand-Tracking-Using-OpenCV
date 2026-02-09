# Hand-Tracking-Using-Opencv and mediapipe
Real-time hand landmark detection using Mediapipe and OpenCV.

This Python script utilizes OpenCV and MediaPipe to perform real-time hand tracking using a webcam. The code captures video input from the default camera, processes the frames to detect and track hand landmarks using the MediaPipe Hands module, and subsequently visualizes the landmarks on the live feed. For each detected hand, the script identifies and prints the coordinates of the landmarks, with a distinctive filled circle highlighting the first landmark (index 0). The frame rate is calculated and displayed in the corner, providing insights into the processing speed. Overall, this script combines the power of computer vision libraries to create a hands-on experience, quite literally, by bringing hand-tracking capabilities to your fingertips. It's a practical demonstration of the intersection between software and real-world interaction, opening doors to diverse applications such as virtual reality, gaming, and accessibility interface.


<video controls src="Hand_gestures.mp4" title="Title"></video>

Built With
Opencv
Mediapipe
Getting Started
This will help you understand how you may give instructions on setting up your project locally. To get a local copy up and running follow these simple example steps.

Installation Steps
Option 1: Installation from GitHub
Follow these steps to install and set up the project directly from the GitHub repository:

Clone the Repository

Open your terminal or command prompt.
Navigate to the directory where you want to install the project.
Run the following command to clone the GitHub repository:
git clone https://github.com/KalyanMurapaka45/Hand-Tracking-Using-Opencv.git
Create a Virtual Environment (Optional but recommended)

It's a good practice to create a virtual environment to manage project dependencies. Run the following command:
conda create -p <Environment_Name> python==<python version> -y
Activate the Virtual Environment (Optional)

Activate the virtual environment based on your operating system:
conda activate <Environment_Name>/
Install Dependencies

Navigate to the project directory:
cd [project_directory]
Run the following command to install project dependencies:
pip install -r requirements.txt
Run the Project
Load the model hand_landmaker.task by:
>> Invoke-WebRequest -Uri "https://storage.googleapis.com/mediapipe-models/hand_landmarker/hand_landmarker/float16/1/hand_landmarker.task" -OutFile "hand_landmarker.task"
Start the project by running the appropriate command.
python app.py
Also
python Hand-Tracking-For-Media.py 
if want to detect hands from media in local system
Access the Project

Open a web browser or the appropriate client to access the project.
Contributing
Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are greatly appreciated.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement". Don't forget to give the project a star! Thanks again!

Fork the Project
Create your Feature Branch
Commit your Changes
Push to the Branch
Open a Pull Request
License
Distributed under the MIT License. See LICENSE.txt for more information.

Contact
Subhodeep Hazra -s.subhodeephazra@gmail.com

Acknowledgements
We'd like to extend our gratitude to all individuals and organizations who have played a role in the development and success of this project. Your support, whether through contributions, inspiration, or encouragement, has been invaluable. Thank you for being a part of our journey.