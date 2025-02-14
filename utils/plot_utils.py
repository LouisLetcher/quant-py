import matplotlib.pyplot as plt

def plot_time_series(data, title='Time Series'):
    plt.figure(figsize=(10, 5))
    plt.plot(data)
    plt.title(title)
    plt.show()
