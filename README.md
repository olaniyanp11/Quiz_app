# Flask Quiz App

This is a Flask-based Quiz App that allows users to answer questions based on different topics and difficulty levels. The app consists of three main pages: question selection, difficulty and username page, and the preview page.

## Features

- Question Selection: Users can choose the specific topic or category of questions they want to answer.
- Difficulty and Username Page: Users can select the difficulty level of the questions and provide their username before starting the quiz.
- Preview Page: Users can preview the selected options (topic, difficulty, and username) before starting the quiz.
- Main Quiz Page: Users will be presented with a series of questions based on their selected options. If the user selects a wrong answer, the window will turn red until the correct answer is chosen.

## Setup and Installation

1. Clone the repository:

```bash
git clone https://github.com/your-username/quiz-app.git
```

2. Change into the project directory:

```bash
cd quiz-app
```

3. Create and activate a virtual environment (optional but recommended):

```bash
python3 -m venv venv
source venv/bin/activate
```

4. Install the required dependencies:

```bash
pip install -r requirements.txt
```

## Usage

1. Run the Flask application:

```bash
python app.py
```

2. Access the Quiz App in your web browser at `http://localhost:5000`.

3. Select the topic, difficulty level, and provide your username on the respective pages.

4. Preview the selected options and click "Start Quiz" to begin.

5. Answer the questions on the main quiz page. If you select a wrong answer, the window will turn red until the correct answer is chosen.


## Customization

- You can choose to restructure it by changing the api serving the questions
- Additional CSS styles or templates can be added or modified in the `templates` and `static` directories.
- To extend the functionality, you can modify the Flask routes and add new routes to handle different pages or actions.

## Contributing

Contributions are welcome! If you find any issues or want to enhance the Quiz App, feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Acknowledgements

- This app was built using the Flask framework, which is a micro web framework for Python.
- The project structure and code organization were inspired by best practices and recommendations for Flask applications.

---
# Built by Permac
