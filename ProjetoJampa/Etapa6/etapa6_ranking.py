import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

tabela = pd.read_csv("../Etapa5/tabela_final_jampa.csv", sep=";")

top10 = tabela.sort_values(by="TAXA_10K", ascending=False).head(10)

#Configurando o gráfico
plt.figure(figsize=(10, 6))
ax = sns.barplot(data=top10, x="TAXA_10K", y="NM_BAIRRO", palette="Reds_r", legend=False)

for p in ax.patches:
    width = p.get_width()
    ax.annotate(f"{width:.2f}",
                (width, p.get_y() + p.get_height() / 2.),
                ha = "left", va="center",
                xytext=(5, 0),
                textcoords="offset points",
                fontsize=9, fontweight="bold"
                )

plt.title("Top 10 Bairros por Taxa de CVLI (por 10.000 hab) - João Pessoa", fontsize=13, fontweight="bold", pad=15)
plt.xlabel("Taxa por 10.000 Habitantes", fontsize=11)
plt.ylabel("Bairro", fontsize=11)
plt.xlim(0, top10["TAXA_10K"].max() * 1.15)
plt.tight_layout()

plt.savefig("ranking_top10_jampa.png", dpi=300)
print("Gráfico gerado e salvo como 'ranking_top10_jampa.png' com sucesso!")
plt.show()