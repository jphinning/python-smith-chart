## Comentários do Algoritmo:

    ### Importação das Bibliotecas:
        numpy para operações matemáticas.
        matplotlib.pyplot para desenhar gráficos.

    ### Definição da Função plot_smith_chart:
        fig, ax = plt.subplots(subplot_kw={'projection': 'polar'}): Cria uma figura e um eixo com projeção polar.
        impedance_circle_radius: Array de raios dos círculos de impedância.
        reflection_coefficient_circle_radius: Array de raios dos círculos de coeficiente de reflexão.
        theta: Array de ângulos de 0 a 2π para desenhar os círculos.

    ### Desenhar Círculos de Impedância e Coeficiente de Reflexão:
        Para cada raio em impedance_circle_radius, desenha um círculo no plano polar.
        Para cada raio em reflection_coefficient_circle_radius, desenha um círculo no plano polar.

    ### Configurações Adicionais da Carta de Smith:
        Define os limites dos eixos e remove as marcações.
        Define o título do gráfico.

    ### Mostrar o Gráfico:
        plt.show(): Exibe o gráfico.
