import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def main():
    data = np.random.randn(100, 3)
    df = pd.DataFrame(data, columns=['A', 'B', 'C'])
    
    print("DataFrame:")
    print(df.head())

    df.plot(kind='line')
    plt.title("Пример графика")
    plt.show()

if __name__ == '__main__':
    main()
