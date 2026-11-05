from pathlib import Path
from urllib.request import Request, urlopen
import json
root=Path(__file__).parent
out=root/'datos_publicos'
out.mkdir(exist_ok=True)
fuentes=[
 dict(id='publica01', titulo='Shakira 2014.jpg', nombre='Shakira', autor='Marcello Casal Jr/Agência Brasil', fecha='2014-07-12', licencia='CC BY 3.0 BR', licencia_url='https://creativecommons.org/licenses/by/3.0/br/', pagina='https://commons.wikimedia.org/wiki/File:Shakira_2014.jpg', url='https://upload.wikimedia.org/wikipedia/commons/7/79/Shakira_2014.jpg'),
 dict(id='publica02', titulo='Juanes ZMF 2015 jm49211.jpg', nombre='Juanes', autor='Jörgens.Mi/Wikipedia', fecha='2015-07-18', licencia='CC BY-SA 3.0', licencia_url='https://creativecommons.org/licenses/by-sa/3.0/', pagina='https://commons.wikimedia.org/wiki/File:Juanes_ZMF_2015_jm49211.jpg', url='https://upload.wikimedia.org/wikipedia/commons/d/d0/Juanes_ZMF_2015_jm49211.jpg'),
 dict(id='publica03', titulo='Carlos Vives.jpg', nombre='Carlos Vives', autor='b r e n t; retoque de Resize', fecha='2005-09-16', licencia='CC BY 2.0', licencia_url='https://creativecommons.org/licenses/by/2.0/', pagina='https://commons.wikimedia.org/wiki/File:Carlos_Vives.jpg', url='https://upload.wikimedia.org/wikipedia/commons/0/07/Carlos_Vives.jpg')
]
for f in fuentes:
    p=out/(f['id']+'.jpg')
    if not p.exists():
        url = 'https://raw.githubusercontent.com/sofiadelcal/karen-calidad-imagenes-publicas-s10/main/' + f['id'] + '.jpg'
        with urlopen(Request(url,headers={'User-Agent':'AcademicImageQuality/1.0'}),timeout=45) as respuesta: p.write_bytes(respuesta.read())
    print(f['id'],p.stat().st_size,flush=True)
(root/'fuentes_publicas.json').write_text(json.dumps(fuentes,indent=2,ensure_ascii=False),encoding='utf8')

