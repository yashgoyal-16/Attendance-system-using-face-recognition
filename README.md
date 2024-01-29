</head>
<body>

<h1>Face Recognition Attendance System</h1>

<p>This is a simple face recognition attendance system written in Python using the <code>face_recognition</code> library and OpenCV. The script captures video from the default camera, detects faces, and matches them against a pre-registered list of students. It then logs the attendance of recognized students in a CSV file with their names and the timestamp.</p>

<h2>Prerequisites</h2>

<p>Before running the script, make sure you have the required libraries installed:</p>

<pre><code>pip install face_recognition opencv-python numpy</code></pre>

<h2>Usage</h2>

<ol>
    <li>Clone the repository:</li>
    <pre><code>git clone https://github.com/yourusername/your-repo.git
cd your-repo</code></pre>

Run the script:
python attendance_system.py

Follow the on-screen prompts to input the number of students and their names along with the corresponding image addresses
The script will start capturing video from the default camera and recognize faces. The recognized students' names will be displayed on the video feed, and attendance will be logged in a CSV file named with the current date.</li>

Press 'q' to exit the program.
</ol>

<h2>Note</h2>

<ul>
Ensure that the face images provided during setup are clear and have only one face per image for accurate recognition.
Make sure to run the script in an environment with a camera available.
The attendance log will be stored in a CSV file with the format <code>YY-MM-DD.csv</code>.
</ul>




</body>
</html>
