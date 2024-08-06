import numpy as np
import matplotlib.pyplot as plt


def plot_smith_chart():
    """
    Função para desenhar a Carta de Smith usando matplotlib.
    """
    fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})
    ax.set_aspect('equal')

    # Parâmetros da Carta de Smith
    impedance_circle_radius = np.linspace(0.1, 2, 20)
    reflection_coefficient_circle_radius = np.linspace(0, 1, 10)
    
    theta = np.linspace(0, 2 * np.pi, 500)

    # Desenhar círculos de impedância
    for r in impedance_circle_radius:
        real = r * np.cos(theta)
        imag = r * np.sin(theta)
        ax.plot(real, imag, 'b', linewidth=0.5)

    # Desenhar círculos de coeficiente de reflexão
    for r in reflection_coefficient_circle_radius:
        ax.plot(r * np.cos(theta), r * np.sin(theta), 'r', linewidth=0.5)

    # Configurações adicionais da Carta de Smith
    ax.set_ylim(-1.1, 1.1)
    ax.set_xlim(-1.1, 1.1)
    ax.set_xticks([])
    ax.set_yticks([])
    ax.grid(False)
    ax.set_title('Carta de Smith')

    plt.show()

if __name__ == "__main__":
    plot_smith_chart()