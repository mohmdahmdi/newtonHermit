def fact(n):
    if n == 1:
        return 1
    return n * fact(n - 1)

def getInput():
    x = []
    n = []
     
    m = int(input("the number of points: "))
    for i in range(m):
        x_in = float(input(f'value of x_{i}: '))
        x.append(x_in)
    
    for i in range(m):
        n_in = int(input(f'enter the n_{i}: '))
        n.append(n_in)
         
    alpha = float(input("enter alpha value: "))  
    
    datas = [[0 for _ in range(n[i])] for i in range(len(x))]
    
    for i in range(len(datas)):
        for j in range(len(datas[i])):
            d_in = float(input(f'value of f{"'"*j}_{i}: ' ))
            datas[i][j] = d_in
            
    return x, n, alpha, datas
 
def calcDiffTable(x, n, datas):
    x_t = []
    datas_t = []

    for i, val in enumerate(n):
        for _ in range(val):
            x_t.append(x[i])
            datas_t.append(datas[i])

    diff_table = [[0 for _ in range(i)] for i in range(len(x_t), 0, -1)]

    for i in range(len(diff_table[0])):
        diff_table[0][i] = datas_t[i][0]

    for i in range(1, len(diff_table), 1):
        for j in range(len(diff_table[i])):
            if x_t[j] == x_t[j + i]: 
                diff_table[i][j] = datas_t[j][i] / fact(i)
            else:
                diff_table[i][j] = (diff_table[i - 1][j + 1] - diff_table[i - 1][j]) / (x_t[j + i] - x_t[j])
    
    return x_t, diff_table
    
def interpolation(diff_table, x_t, alpha):
    f_alpha = 0
    for i, val in enumerate(diff_table):
        p = 1
        for j in range(i):
            p = (alpha - x_t[j]) * p
            
        f_alpha += p * val[0]
    
    return f_alpha

def singleDerivatives(diff, h):
    derivatives = []
    f_vals = diff[0]
    for i in range(len(f_vals)):
        if i >= 1 :
            derivatives.append((f_vals[i] - f_vals[i - 1]) / h)
    return derivatives
    
def doubleDerivatives(diff, h):
    derivatives = []
    f_vals = diff[0]
    for i in range(len(f_vals)):
        if i >= 2:
            derivatives.append((4 * f_vals[i - 1] - 3 * f_vals[i - 2] - f_vals[i]) / (2 * h))
    return derivatives
            
def printDerivatives(diff, h):
    singles = singleDerivatives(diff, h)
    doubles = doubleDerivatives(diff, h)
    print('singles:')
    for i, val in enumerate(singles):
        print(f"f'_{i} = {val}")
    print('singles:')
    for i, val in enumerate(doubles):
        print(f"f'_{i} = {val}")
    
def main():
    x, n, alpha, datas = getInput()
    x_t, diffTable = calcDiffTable(x, n, datas)
    f_alpha = interpolation(diffTable, x_t, alpha)
    print("f(alpha) = ",f_alpha)
    h = x[1] - x[0] if len(x) > 1 else None
    printDerivatives(diffTable, h)

if __name__ == "__main__":
    main()
