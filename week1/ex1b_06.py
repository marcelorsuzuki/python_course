# http://www.codeskulptor.org/#user2-nUdgvrf9fUAmdF0-0.py

def future_value(present_value, annual_rate, periods_per_year, years):
    rate_per_period = annual_rate / periods_per_year
    periods = periods_per_year * years
    
    # Put your code here.
    #  FV = PV (1+rate)periods
    
    fv = present_value * (1 + rate_per_period) ** periods
    
    return fv
    
# 745.317442823934.    
print "$1000 at 2% compounded daily for 3 years yields $", future_value(1000, .02, 365, 3)