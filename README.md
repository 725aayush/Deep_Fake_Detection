# Deepfake Detection Project

## Overview

This project is a Django-based web application designed to detect deepfake videos. Utilizing advanced machine learning techniques such as Long Short-Term Memory (LSTM) networks and ResNeXt Convolutional Neural Networks (CNN), the application provides a robust solution for identifying manipulated videos.

## Objective

The primary objective of this project is to develop a reliable and efficient tool to combat the spread of deepfake content. By leveraging state-of-the-art machine learning models, we aim to create a system that can accurately distinguish between authentic and manipulated videos.

## Technologies Used

- **Django:** A high-level Python web framework that encourages rapid development and clean, pragmatic design.
- **LSTM (Long Short-Term Memory):** A type of recurrent neural network (RNN) capable of learning long-term dependencies, particularly useful in sequence prediction problems.
- **ResNeXt CNN:** A variant of the traditional Convolutional Neural Network that uses grouped convolutions to enhance performance and accuracy.

## Features

- **User Authentication:** Secure login and registration system.
- **Upload Videos:** Users can upload videos to be analyzed for deepfake detection.
- **Real-time Analysis:** The system processes the uploaded videos and provides a detailed report on the likelihood of manipulation.
- **Dashboard:** A user-friendly interface to view analysis results and manage uploaded videos.
## Usage

1. **Register or log in to your account.**
2. **Upload a video** for deepfake analysis.
3. **View the results** on the dashboard.

## Model Training

The models used for deepfake detection are trained using the following steps:

1. **Data Collection:** Gather a dataset of authentic and deepfake videos.
2. **Preprocessing:** Convert videos into frames and preprocess the data.
3. **Model Training:** Train the LSTM and ResNeXt CNN models using the preprocessed data.
4. **Evaluation:** Evaluate the models' performance and fine-tune as necessary.
5. **Integration:** Integrate the trained models into the Django application.

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/your-feature`).
3. Commit your changes (`git commit -am 'Add your feature'`).
4. Push to the branch (`git push origin feature/your-feature`).
5. Create a new Pull Request.
