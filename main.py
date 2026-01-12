import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

np.random.seed(42)
dados_formaldeido = np.random.normal(loc=0.015, scale=0.003, size=1000)

media_amostra = np.mean(dados_formaldeido)
print(f"Estimativa Pontual Média da Amostra:{media_amostra:.5f} ppb")

confianca = 0.95
tamanho_amostra = len(dados_formaldeido)
erro_padrao = stats.sem(dados_formaldeido)

ic = stats.t.interval(
    confidence = confianca,
    df = tamanho_amostra,
    loc = media_amostra,
    scale = erro_padrao,
)

limite_inferior = ic[0]
limite_superior = ic[1]

print("-" * 10)
print(f"Nível de confiança: {confianca * 100:.0f}%")
print(f"Limite do IC: [{limite_inferior} ppb, {limite_superior} ppb]")
print("-" * 10)

plt.figure(figsize=(10, 5))
plt.errorbar(
    x = media_amostra,
    y = 0.5,
    xerr =[[media_amostra - limite_inferior], [limite_superior - media_amostra]],
    fmt ='o',
    capsize = 5,
    label = 'Intervalo de confiança 95%',
    color = 'purple'
)
plt.axvline(
    x = limite_inferior,
    color = 'red',
    linestyle = '--',
    linewidth = 0.8,
    label = 'Limite Inferior'
)
plt.axvline(
    x = limite_superior,
    color = 'red',
    linestyle = '--',
    linewidth = 0.8,
    label = 'Limite Superior'
)
plt.yticks([0.5], ['Concentração Média (ppb)'])
plt.title('Representação de Intervalo de Confiança de 95% para Formaldeído')
plt.xlabel('Concentração de Formaldeído (ppb)')
plt.grid(axis = 'x', linestyle = ':')
plt.legend(loc = 'upper right')
plt.show()