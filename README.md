# bmi_calculator



# BMI Calculator App - Comprehensive Health Assistant

[![Windows Build](https://img.shields.io/badge/Platform-Windows-blue)](https://github.com/genomicinvader/bmi_calculator/releases)
[![Python Version](https://img.shields.io/badge/Python-3.10%2B-green)](https://python.org)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

[![Screenshot-2025-08-01-062210.png](https://i.postimg.cc/15y7SBjD/Screenshot-2025-08-01-062210.png)](https://postimg.cc/DmYPdrFz)


## About the Project

**BMI Calculator App** is a comprehensive health application created in August 1, 2025 that calculates your Body Mass Index (BMI), provides ideal weight recommendations, and offers personalized diet and exercise plans. This project combines health science with practical software engineering to help users maintain a healthy lifestyle.

**Key Features:**
- 🧮 BMI calculation with unit conversion (cm/inches, kg/lbs)
- 💡 Ideal weight recommendation
- 🥗 Personalized diet plans based on BMI category
- 🏃 Exercise recommendations with duration and types
- 📊 Clean, user-friendly interface
- 📦 Easy installation for Windows users

## How It Works

The application uses sophisticated algorithms to provide accurate health recommendations:

### Core Algorithms
```python
# BMI Calculation
def calculate_bmi(height, height_unit, weight, weight_unit):
    # Convert to metric units
    if height_unit == "inches":
        height_m = height * 0.0254
    else:
        height_m = height / 100
    
    if weight_unit == "lbs":
        weight_kg = weight * 0.453592
    else:
        weight_kg = weight
    
    return weight_kg / (height_m ** 2)

# Ideal Weight Calculation
def calculate_ideal_weight(height_m, weight_unit):
    ideal_weight_kg = 22 * (height_m ** 2)  # 22 is considered ideal BMI
    if weight_unit == "lbs":
        return ideal_weight_kg * 2.20462
    return ideal_weight_kg


```




# Installation
### For End Users
1. Download the installer from Releases Section
2. Run BMI_Calculator_Setup.exe
3. Follow the installation wizard
4. Launch from Start Menu or Desktop shortcut

### For Developers

```Bash
# Clone the repository
git clone https://github.com/genomicinvader/bmi-calculator.git

# Install dependencies
pip install -r requirements.txt

# Run the application
python bmi_calculator.py
```


# Technology Stack
1. Frontend: Tkinter (Python GUI)
2. Packaging: PyInstaller
3. Installer: Inno Setup
4. Dependencies: Pillow (Icon generation)

# Join the Development!
I invite software engineers worldwide to contribute to this project and help improve health technology for everyone. There are endless possibilities for enhancement:

## Potential Improvements
[![deepseek-mermaid-20250801-b32c8e.png](https://i.postimg.cc/sXzyR8G5/deepseek-mermaid-20250801-b32c8e.png)](https://postimg.cc/d75g25B0)

graph TD
    A[Current Features] --> B[Multilingual Support]
    A --> C[Mobile Versions]
    A --> D[Fitness Tracker Integration]
    A --> E[Machine Learning Recommendations]
    A --> F[Progress Tracking]
    A --> G[Nutrition Database Integration]

## How to Contribute
1. Fork the repository
2. Create your feature branch (git checkout -b feature/AmazingFeature)
3. Commit your changes (git commit -m 'Add some AmazingFeature')
4. Push to the branch (git push origin feature/AmazingFeature)
5. Open a Pull Request

### Let's build a healthier world together through technology! 🌍💻

## License
Distributed under the MIT License. See LICENSE for more information.

# Contact
Genomic Invader - [@genomicinvader](https://github.com/genomicinvader) (/br)
Project Link: https://github.com/genomicinvader/bmi_calculator
