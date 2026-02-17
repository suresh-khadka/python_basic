
def find_corelation_coff():
    import pandas as pd
    import numpy as np
    import matplotlib.pyplot as plt

    # Load Excel file
    # df = pd.read_excel("your_file.xlsx")  

    # # Assuming your x and y columns are named 'X' and 'Y'
    # x = df['X'].values
    # y = df['Y'].values


    # for testing we calculate randon 1000 values of x. also finf value of y with the help of equations y = 3 * x + 5 + np.random.normal(0, 5, size=1000)

    np.random.seed(0)
    x = np.linspace(0, 10, 1000)
    y = 3 * x + 5 + np.random.normal(0, 5, size=1000) 

    #  for linear data function
    from scipy.stats import linregress
    slope, intercept, r_value, p_value, std_err = linregress(x, y)
    print("Linear Model:")
    print("  Slope:", slope)
    print("  Intercept:", intercept)
    print("  R-squared:", r_value**2)

    # for exponential function
    # Ensure y > 0 (log can't handle zero or negative)
    x_exp = x[y > 0]
    y_exp = y[y > 0]

    log_y = np.log(y_exp)
    slope_exp, intercept_exp, r_value_exp, _, _ = linregress(x_exp, log_y)

    print("Exponential Model:")
    print("  R-squared (log-transformed):", r_value_exp**2)

    # for polynimial function
    coeffs = np.polyfit(x, y, 2)
    y_pred = np.polyval(coeffs, x)

    ss_res = np.sum((y - y_pred)**2)
    ss_tot = np.sum((y - np.mean(y))**2)
    r_squared_poly = 1 - (ss_res / ss_tot)

    print("Polynomial Model (Degree 2):")
    print("  R-squared:", r_squared_poly)



    # for visualition
    # data set import matplotlib.pyplot as plt
    import matplotlib.pyplot as plt
    plt.scatter(x, y, label="Data", alpha=0.5)

    # Linear Fit
    plt.plot(x, slope * x + intercept, label="Linear Fit", color="blue")

    # Exponential Fit
    plt.plot(x_exp, np.exp(intercept_exp) * np.exp(slope_exp * x_exp), label="Exponential Fit", color="green")

    # Polynomial Fit
    plt.plot(x, y_pred, label="Polynomial Fit (deg 2)", color="red")

    plt.legend()
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.title("Model Fits")
    plt.show()

    return r_value**2,r_value_exp**2,r_squared_poly



def find_greatest(a,b,c):
    if(a>b and a>c):
        print("we conclude the the best fitting line equation is linear")
        return a
    
    elif(b>a and b>c):
        print("we conclude the the best fitting line equation is exponential")
        return b
    
    else:
        print("we conclude the the best fitting line equation is polynomial(degree 2)")
        return c
    


linear_r,exp_r,poly_r=find_corelation_coff()

greatest=find_greatest(linear_r,exp_r,poly_r)

print(f"and highest value of r is : {greatest}")