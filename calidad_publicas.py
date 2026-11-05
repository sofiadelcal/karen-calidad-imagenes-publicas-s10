from pathlib import Path
import csv, json
import numpy as np
from PIL import Image, ImageOps
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parent
OUT = ROOT / "resultados_publicos"
OUT.mkdir(exist_ok=True)
fuentes = json.loads((ROOT/"fuentes_publicas.json").read_text(encoding="utf8"))
filas, figuras = [], []
for f in fuentes:
    with Image.open(ROOT/"datos_publicos"/(f["id"]+".jpg")) as archivo:
        im = ImageOps.exif_transpose(archivo).convert("RGB")
    reducida = ImageOps.contain(im, (320,320), Image.Resampling.LANCZOS)
    gris = np.asarray(reducida.convert("L"), dtype=np.float64)
    hist = np.bincount(gris.astype(np.uint8).ravel(), minlength=256)
    probs = hist[hist>0] / gris.size
    lap = gris[:-2,1:-1]+gris[2:,1:-1]+gris[1:-1,:-2]+gris[1:-1,2:]-4*gris[1:-1,1:-1]
    filas.append(dict(id=f["id"], ancho=im.width, alto=im.height,
        ancho_analisis=reducida.width, alto_analisis=reducida.height,
        brillo=float(gris.mean()), contraste=float(gris.std()),
        sombras_pct=float((gris<=10).mean()*100),
        luces_pct=float((gris>=245).mean()*100),
        entropia=float(-(probs*np.log2(probs)).sum()),
        var_laplaciano=float(lap.var())))
    figuras.append((reducida,gris))
with (OUT/"calidad_publicas.csv").open("w",newline="",encoding="utf8") as archivo:
    escritor=csv.DictWriter(archivo,fieldnames=filas[0])
    escritor.writeheader()
    escritor.writerows(filas)
(OUT/"calidad_publicas.json").write_text(json.dumps(filas,indent=2),encoding="utf8")
fig,axs=plt.subplots(2,3,figsize=(9,6))
for i,(f,(rgb,gris)) in enumerate(zip(fuentes,figuras)):
    axs[0,i].imshow(rgb)
    axs[0,i].set_title(f["id"]+" · "+f["nombre"],fontsize=10)
    axs[1,i].imshow(gris,cmap="gray",vmin=0,vmax=255)
    axs[1,i].set_title("Escala de grises",fontsize=10)
    axs[0,i].axis("off")
    axs[1,i].axis("off")
fig.tight_layout()
fig.savefig(OUT/"publicas_panel.png",dpi=160)
plt.close(fig)
fig,ax=plt.subplots(figsize=(8,3))
for f,(_,gris) in zip(fuentes,figuras):
    ax.hist(gris.ravel(),bins=32,range=(0,256),density=True,histtype="step",label=f["id"])
ax.set(xlabel="Intensidad (0–255)",ylabel="Densidad")
ax.legend()
fig.tight_layout()
fig.savefig(OUT/"publicas_histogramas.png",dpi=160)
plt.close(fig)
print(json.dumps(filas,indent=2))

