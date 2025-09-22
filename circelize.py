from pycirclize import Circos
import matplotlib.pyplot as plt
from matplotlib.patches import Patch

# Werte bestimmen die Sektorbreite
values = {"A": 40, "B": 70, "C": 90}
sectors = values
circos = Circos(sectors, space=2)

# Farben pro Sektor
colors = {"A": "skyblue", "B": "lightgreen", "C": "salmon"}

# Für die Legende sammeln wir später Patches
legend_patches = []

for s in circos.sectors:
    tr = s.add_track((0, 100))          # voller Radiusbereich
    x0, x1 = getattr(s, "xlim", (s.start, s.end))
    tr.rect(x0, x1, facecolor=colors[s.name], edgecolor="black")
    s.text(s.name, r=110, size=12)

    # Patch für die Legende
    legend_patches.append(Patch(facecolor=colors[s.name], edgecolor="black", label=s.name))

# Plot zeichnen und Legende platzieren
circos.plotfig()
plt.legend(
    handles=legend_patches,
    title="Sektoren",
    loc="center left",
    bbox_to_anchor=(1.02, 0.5),
    borderaxespad=0.0,
)
plt.tight_layout()
plt.show()
