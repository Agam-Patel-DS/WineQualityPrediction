
# Wine Quality Prediction

This repository contains a machine learning project for predicting wine quality based on its chemical properties. 

## Table of Contents
- [Project Overview](#project-overview)
- [Dataset](#dataset)
- [Modeling](#modeling)
- [Web Application](#web-application)
- [Installation](#installation)
- [Usage](#usage)
- [Results](#results)
- [Contributing](#contributing)
- [License](#license)

## Project Overview

The goal of this project is to predict the quality of wine based on various chemical features such as acidity, sugar, pH, and alcohol content. The prediction model is implemented using machine learning techniques, and the results are presented through a Streamlit-based web application.

## Dataset

The dataset used for this project is the **Wine Quality Dataset**, which contains 1,599 red wine samples with 12 features each. These features are:
- Fixed Acidity
- Volatile Acidity
- Citric Acid
- Residual Sugar
- Chlorides
- Free Sulfur Dioxide
- Total Sulfur Dioxide
- Density
- pH
- Sulphates
- Alcohol
- Quality (Target variable)

You can find the dataset [here](https://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-red.csv).

## Installation

To run this project locally, follow these steps:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/Agam-Patel-DS/WineQualityPrediction.git
   cd WineQualityPrediction
   ```

2. **Install the required dependencies**:
   Make sure you have Python installed, then run:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

To run the Flask app, use the following command:
```bash
python run app.py
```
To run the Streamlit app, use the following command:
```bash
streamlit run app.py
```

This will launch a local web server, and you can access the application in your browser by navigating to `http://localhost:8501`.

## Results

The model achieves a good accuracy in predicting wine quality, making it a useful tool for exploring the relationships between different chemical properties and wine quality. 

## Contributing

Contributions are welcome! If you have any ideas or improvements, feel free to fork the repository and submit a pull request.

## License

This project is open-source and available under the MIT License. See the [LICENSE](LICENSE) file for more details.
```

This `README.md` provides an overview of the project, installation instructions, usage details, and other important information. Be sure to adjust any sections based on the specific content of your repository.
