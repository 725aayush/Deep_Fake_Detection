## Installation

1. **Clone the repository:**
    ```bash
    git clone https://github.com/yourusername/deepfake-detection.git
    cd deepfake-detection
    ```

2. **Set up a virtual environment:**
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4. **Apply migrations:**
    ```bash
    python manage.py migrate
    ```

5. **Run the development server:**
    ```bash
    python manage.py runserver
    ```

6. **Access the application:**
    Open your web browser and navigate to `http://localhost:8000`.
