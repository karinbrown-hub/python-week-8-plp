import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt

class WeatherApp(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle("Weather App")
        self.setGeometry(100, 100, 400, 300)
        self.setStyleSheet("background-color: #87CEEB;")  # light blue background

        layout = QVBoxLayout()
        self.setLayout(layout)

        font = QFont("Arial", 14)  # changed font to Arial

        label = QLabel("Enter location:")
        label.setFont(font)
        label.setStyleSheet("color: #FFFFFF;")  # white text color
        layout.addWidget(label)

        self.location_entry = QLineEdit()
        self.location_entry.setFont(font)
        self.location_entry.setStyleSheet("background-color: #FFFFFF; color: #000000;")  # white background and black text color
        layout.addWidget(self.location_entry)

        button = QPushButton("Get Weather")
        button.setFont(font)
        button.setStyleSheet("background-color: #4CAF50; color: #FFFFFF;")  # green button color and white text color
        button.clicked.connect(self.get_weather)
        layout.addWidget(button)

        self.weather_label = QLabel()
        self.weather_label.setFont(font)
        self.weather_label.setStyleSheet("color: #000000;")  # black text color
        layout.addWidget(self.weather_label)

    def get_weather(self):
        location = self.location_entry.text()
        # Get weather data from API
        weather_data = {"temperature": 25, "condition": "Sunny"}
        self.weather_label.setText(f"Weather in {location}: {weather_data['temperature']}°C, {weather_data['condition']}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = WeatherApp()
    ex.show()
    sys.exit(app.exec_())