import math
from scipy.stats import norm

class BlackScholes:
    
    def __init__(self, s,k,t,r,sigma):
        
        """
        s: underlying stock spot price
        k: strike price
        t: time to maturity (in years)
        r: risk-free rate (annualized)
        sigma: volatility (annualized)
        """

        self.s = s
        self.k = k
        self.t = t
        self.r = r
        self.sigma = sigma

    def d1(self):
        return (math.log(self.s/self.k)+(self.r + 0.5*(self.sigma**2))*self.t)/(self.sigma * math.sqrt(self.t))
    
    def d2(self):
        return self.d1() - self.sigma*math.sqrt(self.t)

    def call_option_price(self):
        return (self.s*norm.cdf(self.d1())) - (self.k*math.exp(-self.r*self.t)*norm.cdf(self.d2()))
    
    def put_option_price(self):
        return (self.k*math.exp(-self.r*self.t)*norm.cdf(-self.d2())) - (self.s*norm.cdf(-self.d1()))
    
    def validate_inputs(self):
        
        if self.s<=0 or self.k<=0:
            raise ValueError('Stock and Strike prices must be positive numbers')
        
        if self.t<=0:
            raise ValueError('Time to maturity of the option must be a positive number')
        
        if self.sigma<0:
            raise ValueError('The option volatility must be a positive number')

    def delta(self, option_type='call'):
        # option price's sensibility to the stock price's variation

        if option_type=='call':
                return norm.cdf(self.d1())
        
        elif option_type=='put':
                return norm.cdf(self.d1()) - 1
        
        else:
             raise ValueError('option_type must be either put or call')
        
    def gamma(self, option_type='call'):
        # delta's sensibility to the stock price's variation

        return norm.pdf(self.d1())/(self.s*self.sigma*math.sqrt(self.t))
    
    def theta(self, option_type='call'):
        # option price's sensibility to the passing of time

        first_term = -(self.s*norm.pdf(self.d1())*self.sigma)/(2*math.sqrt(self.t))

        if option_type=='call':
            second_term = self.r*self.k*math.exp(-self.r*self.t)*norm.cdf(self.d2())
            return first_term - second_term

        elif option_type=='put':
            second_term = self.r*self.k*math.exp(-self.r*self.t)*norm.cdf(-self.d2())
            return first_term + second_term
        
        else:
             raise ValueError('option_type must be either put or call')
        
    def vega(self):
        # option price's sensibility to the stock price's volatility
        
        return self.s * norm.pdf(self.d1()) * math.sqrt(self.t)
    
    def rho(self, option_type='call'):
        # option price's sensibility to the risk-free rate variation

        if option_type=='call':
            return self.k*self.t*math.exp(-self.r*self.t)*norm.cdf(self.d2())

        elif option_type=='put':
            return -self.k*self.t*math.exp(-self.r*self.t)*norm.cdf(-self.d2())

        else:
            raise ValueError('option_type must be either put or call')

    def greeks(self):
        
        print(f'''
              
              Greeks for the Call option:\n
              Delta: {round(self.delta(),2)}
              Gamma: {round(self.gamma(),2)}
              Theta: {round(self.theta(),2)}
              Vega: {round(self.vega(),2)}
              Rho: {round(self.rho(),2)}
              ''')
        

            
