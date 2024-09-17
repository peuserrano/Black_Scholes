# Black-Scholes Option Pricing Model

## Overview

This Python project provides an implementation of the Black-Scholes model, a fundamental tool in financial mathematics used for option pricing. The library calculates the prices of call and put options and their Greeks (Delta, Gamma, Theta, Vega, and Rho), offering essential insights into the behavior and sensitivity of options.

## Features

- **Option Pricing**: Compute prices for call and put options.
- **Greeks Calculation**: Evaluate Greeks—Delta, Gamma, Theta, Vega, and Rho—that measure the sensitivity of option prices to various factors.
- **Input Validation**: Ensure valid input parameters for accurate calculations.
- **Usage Example**: Demonstrate practical application of the Black-Scholes model.

## Installation

1. **Clone the Repository:**

    ```bash
    git clone https://github.com/peuserrano/Black_Scholes.git
    ```

2. **Navigate to the Project Directory:**

    ```bash
    cd Black_Scholes
    ```

3. **Install Dependencies:**

    Ensure you have Python 3 installed. Install the required libraries using pip:

    ```bash
    pip install scipy
    ```

## Usage

1. **Define Option Parameters and Create the Model:**

    ```python
    from src.black_scholes import BlackScholes

    # Define parameters
    s = 100       # Stock price
    k = 100       # Strike price
    t = 1         # Time to maturity (in years)
    r = 0.05      # Risk-free rate (annualized)
    sigma = 0.2   # Volatility (annualized)

    # Create Black-Scholes model instance
    model = BlackScholes(s, k, t, r, sigma)
    ```

2. **Calculate Option Prices and Greeks:**

    ```python
    # Calculate option prices
    call_price = model.call_option_price()
    put_price = model.put_option_price()

    # Print option prices
    print(f'Call option price: ${round(call_price, 2)}')
    print(f'Put option price: ${round(put_price, 2)}')

    # Calculate and print Greeks
    model.greeks()
    ```

## Example

Here’s a full example of using the Black-Scholes model:

```python
from src.black_scholes import BlackScholes

if __name__ == "__main__":
    s = 100
    k = 100
    t = 1
    r = 0.05
    sigma = 0.2

    model = BlackScholes(s, k, t, r, sigma)
    model.validate_inputs()

    call = model.call_option_price()
    put = model.put_option_price()

    print(f'''
          Call option price: ${round(call, 2)}
          Put option price: ${round(put, 2)}
          ''')

    model.greeks()
