# quant-py

A collection of Python-based trading strategies and analysis tools for algorithmic trading, designed to integrate seamlessly with QuantConnect's Lean engine. This repository focuses on Python scripts and libraries that can be integrated into various trading platforms, research pipelines, and backtesting frameworks. Contributions are welcome!


## Table of Contents

- [quant-py](#quant-py)
  - [Table of Contents](#table-of-contents)
  - [Introduction](#introduction)
  - [Requirements](#requirements)
  - [Installation](#installation)
  - [Usage](#usage)
    - [Strategies and Indicators](#strategies-and-indicators)
    - [Integration with QuantConnect](#integration-with-quantconnect)
  - [Contributing](#contributing)
  - [License](#license)

## Introduction

`quant-py` provides ready-to-use Python scripts and modules that help traders and analysts build algorithmic trading systems, conduct technical analysis, and perform robust backtesting. By leveraging the flexibility and power of Python, you can easily integrate these tools into your existing workflow, whether it’s for live trading, paper trading, or historical market analysis.


## Requirements

- **Python 3.8+**
- **Dependencies:**  
  Common Python libraries such as `pandas`, `numpy`, `matplotlib`, `ta` (for technical analysis), and any other specified dependencies required by individual scripts.

## Installation

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/your-username/quant-python.git
   ```

2. **Install Dependencies:**
   ```bash
   cd quant-python
   pip install -r requirements.txt
   ```

3. **Install Pre-Commit Hooks**
   ```bash
   pre-commit install
   ```

4. **Run Tests**
   ```bash
   pytest tests/
   ```

5. **Run Linting**
   ```bash
   black .
   flake8 .
   isort .
   ```

## Usage

### Strategies and Indicators
Inside the strategies and indicators directories, you’ll find Python scripts and modules that you can run or import into your own projects.

### Integration with QuantConnect
To integrate your strategies with QuantConnect, follow these steps:

1. **Authenticate with QuantConnect**
   ```bash
   lean login
   ```

2. **Authenticate with QuantConnect**
   ```bash
   lean cloud push "algorithms/(portfolio)/(strategy).py"
   ```
   
3. **Run Backtests with QuantConnect Lean**
```bash
lean backtest "algorithms/(portfolio)/(strategy).py"
```

## Contributing
Contributions are welcome! If you have developed a Python strategy, indicator, or tool that you’d like to share:

1. Fork the repository and create a new branch.
2. Add your script along with a brief README in the appropriate directory.
3. Ensure your code is well-documented and follows the project’s coding standards.
4. Open a Pull Request, providing a clear description of what your contribution does and how it can be used.

## License
This repository is released under the MIT License. You are free to use, modify, and distribute the scripts as long as you comply with the license terms.
