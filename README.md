}

# TinyMuse

## Video Demo

<PASTE YOUR YOUTUBE UNLISTED LINK HERE>

---

## Description

TinyMuse is a lightweight web application designed to generate, store, and manage creative prompts for writers, designers, and anyone involved in creative thinking. The main objective of this project is to provide users with instant inspiration while also allowing them to build a personal archive of favorite ideas and prompts. The project was developed as the final project for CS50 and demonstrates the practical use of backend development, database management, and frontend interaction.

The application allows users to randomly generate creative prompts, filter them using keywords, add their own prompts, save selected prompts to their favorites with optional notes, and search across all stored prompts. The system is designed to be minimal, fast, and easily extendable.

TinyMuse is built using Flask as the backend framework, SQLite as the database system, Bootstrap for styling, and vanilla JavaScript for frontend interactions. All components were chosen to maintain simplicity while ensuring full functionality.

---

## Motivation and Design Philosophy

The idea behind TinyMuse originated from the need for fast and reliable inspiration tools, especially for individuals who experience creative blocks. Many prompt generators exist online, but most are limited in customization, storage, and personalization features. TinyMuse solves this problem by allowing users not only to receive random inspiration but also to actively participate in expanding the prompt database and managing their favorite ideas.

The overall design philosophy focuses on clarity, simplicity, and usability. The interface avoids unnecessary complexity and ensures that users can interact with the application without any technical background. Every feature is implemented with a practical use-case in mind.

---

## Application Features

The main features of TinyMuse include:

1. **Random Prompt Generator**
   Users can generate a random creative prompt with a single click. If a keyword is entered, the generator tries to return a related prompt.

2. **Prompt Remixing**
   Some generated prompts are automatically modified with creative twists, such as changing the narrative perspective or converting the concept into a short poetic form.

3. **Prompt Submission**
   Users can submit their own prompts, which are immediately stored in the database and become part of the global prompt pool.

4. **Favorites System**
   Any generated prompt can be saved to the favorites list along with an optional personal note.

5. **Search Functionality**
   A search system allows users to find prompts containing specific words or themes.

6. **Recent Prompts Display**
   The most recently added prompts are displayed on the homepage.

---

## Technical Architecture

The backend of TinyMuse is implemented using Flask. The application follows a simple MVC-style structure, separating logic, layout, and client-side interaction. The SQLite database stores two primary tables:

* **prompts**: Stores all generated and user-submitted prompts.
* **favorites**: Stores user-selected favorite prompts along with optional notes.

The application exposes several API endpoints that allow interaction between the frontend and backend without reloading the page. These include endpoints for generating prompts, adding new prompts, saving favorites, and searching.

The frontend is built using Bootstrap for responsive layout and vanilla JavaScript for real-time interactivity without the use of heavy frameworks.

---

## File Structure and Responsibilities

* **app.py**
  The core Flask application. It contains all routing logic, database queries, and API endpoints.

* **init_db.py**
  Initializes the SQLite database and inserts a set of default prompts.

* **requirements.txt**
  Lists all Python dependencies required to run the project.

* **templates/base.html**
  The base template that defines the layout structure and loads CSS and JavaScript files.

* **templates/index.html**
  The main interface where users interact with the application.

* **static/style.css**
  Custom styling for the project.

* **static/script.js**
  Contains all frontend logic, including API requests, prompt generation, saving favorites, and searching.

---

## Installation and Execution

To run TinyMuse locally, follow these steps:

1. Create and activate a virtual environment.
2. Install the dependencies using `pip install -r requirements.txt`.
3. Initialize the database using `python init_db.py`.
4. Start the server using `python app.py`.
5. Open a browser and navigate to `http://127.0.0.1:5000`.

---

## Challenges and Learning Outcomes

One of the key challenges of this project was maintaining synchronization between the frontend interface and the backend API without relying on modern frontend frameworks. Implementing asynchronous requests using the Fetch API while ensuring database consistency required careful planning.

Another challenge was designing a flexible database structure that supports expansion, such as adding authentication or cloud-based prompt storage in future versions.

Through this project, practical skills in Flask routing, SQLite database design, REST-style APIs, and frontend-backend integration were significantly improved. Additionally, the project reinforced the importance of clean project structure and proper documentation.

---

## Future Improvements

Potential future improvements include:

* User authentication system.
* Cloud deployment with persistent storage.
* Tag-based classification of prompts.
* Public sharing system for curated prompt collections.

---

## Conclusion

TinyMuse successfully demonstrates a complete and functional web application that integrates backend logic, database operations, and frontend interaction. The project fulfills the objectives of the CS50 final project by showcasing independent problem-solving, design decisions, and full-stack development skills.
