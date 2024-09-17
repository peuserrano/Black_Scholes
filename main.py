
from src.black_scholes import BlackScholes

if __name__ == "__main__":

    s = 100
    k = 100
    t = 1
    r = 0.05
    sigma = 0.2
    market_price = 12.5

    model = BlackScholes(s,k,t,r,sigma)
    model.validate_inputs()

    call = model.call_option_price()
    put = model.put_option_price()

    print(f'''
          Call option price: ${round(call,2)}\n
          Put option price: ${round(put,2)}
          ''')
    
    model.greeks()