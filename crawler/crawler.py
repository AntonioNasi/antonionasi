from urllib.parse import (
    urlparse,
    urljoin
)

from collections import deque
from concurrent.futures import ThreadPoolExecutor

from ddgs import DDGS
from bs4 import BeautifulSoup

import requests
import json

from dateparser.search import search_dates

from datetime import datetime
from pathlib import Path


# -------------------------
# CONFIG
# -------------------------

ALL_KEYWORDS=[

    "marxismo",
    "marx",
    "comunismo",
    "socialismo",
    "lukács",
    "revolução socialista",
    "revolução comunista",
    "revolução",
    "revolucao"

]


EVENT_TERMS=[

    "evento",
    "seminário",
    "seminario",
    "congresso",
    "colóquio",
    "coloquio",
    "mesa",
    "jornada",
    "debate",
    "simpósio",
    "simposio",
    "encontro"

]


SEARCH_SITES=[

    "site:ufac.br",
    "site:ufal.br",
    "site:unifap.br",
    "site:ufam.edu.br",
    "site:ufba.br",
    "site:ufob.edu.br",
    "site:ufrb.edu.br",
    "site:ufc.br",
    "site:ufca.edu.br",
    "site:unb.br",
    "site:ufes.br",
    "site:ufg.br",
    "site:ufj.edu.br",
    "site:ufcat.edu.br",
    "site:ufma.br",
    "site:ufmt.br",
    "site:ufms.br",
    "site:ufmg.br",
    "site:ufvjm.edu.br",
    "site:ufjf.br",
    "site:ufla.br",
    "site:ufop.br",
    "site:ufsj.edu.br",
    "site:ufu.br",
    "site:ufv.br",
    "site:ufpa.br",
    "site:ufpb.br",
    "site:ufcg.edu.br",
    "site:ufpe.br",
    "site:ufrpe.br",
    "site:univasf.edu.br",
    "site:ufpi.br",
    "site:ufpr.br",
    "site:utfpr.edu.br",
    "site:ufrj.br",
    "site:unirio.br",
    "site:uff.br",
    "site:ufrrj.br",
    "site:ufrn.br",
    "site:ufersa.edu.br",
    "site:ufrgs.br",
    "site:furg.br",
    "site:ufpel.edu.br",
    "site:unipampa.edu.br",
    "site:ufsm.br",
    "site:ufsc.br",
    "site:uffs.edu.br",
    "site:ufscar.br",
    "site:unifesp.br",
    "site:ufabc.edu.br",
    "site:ufs.br",
    "site:uft.edu.br",
    "site:ufopa.edu.br",
    "site:unifesspa.edu.br",
    "site:ufra.edu.br",
    "site:unilab.edu.br",
    "site:unila.edu.br",
    "site:ufape.edu.br",
    "site:ufr.edu.br",
    "site:ufdpar.edu.br",
    "site:ufnt.edu.br",
    "site:ufrr.br",
    "site:unifal-mg.edu.br",
    "site:ufcspa.edu.br",
    "site:ufpam.edu.br",
    "site:uece.br",
    "site:eventos.uece.br",
    "site:siseventos.uece.br",
    "site:uvanet.br",
    "site:urca.br",
    "site:usp.br",
    "site:unicamp.br",
    "site:unesp.br",
    "site:uerj.br",
    "site:uenf.br",
    "site:uemg.br",
    "site:unimontes.br",
    "site:uel.br",
    "site:uem.br",
    "site:uepg.br",
    "site:unioeste.br",
    "site:unicentro.br",
    "site:unespar.edu.br",
    "site:uneb.br",
    "site:uefs.br",
    "site:uesb.br",
    "site:uesc.br",
    "site:uea.edu.br",
    "site:uepa.br",
    "site:udesc.br",
    "site:uepb.edu.br",
    "site:upe.br",
    "site:uern.br",
    "site:uema.br",
    "site:uemasul.edu.br",
    "site:uespi.br",
    "site:ueg.br",
    "site:unitins.br",
    "site:uerr.edu.br",
    "site:unemat.br",
    "site:even3.com.br",
    "site:doity.com.br"

]


MAX_PAGES=30
MAX_EVENTS=25


IGNORAR=[

".pdf",
".jpg",
".jpeg",
".png",
".gif",
".zip",

"/tag/",
"/feed/",
"/author/",
"/wp-content/",

"#"

]


BASE_DIR=Path(
    __file__
).resolve().parent.parent


results=[]
urls_visitadas=set()


# -------------------------
# sessão
# -------------------------

session=requests.Session()

session.headers.update({

"User-Agent":
"Mozilla/5.0"

})


# -------------------------
# logo fallback
# -------------------------

def university_logo(url):

    p=urlparse(url)

    return (

        p.scheme+
        "://"+
        p.netloc+
        "/favicon.ico"

    )


# -------------------------
# extrai título
# -------------------------

def extract_title(soup):

    h1=soup.find(
        "h1"
    )

    if h1:

        return h1.get_text(
            strip=True
        )


    og=soup.find(

        "meta",

        property=
        "og:title"

    )

    if og:

        return og.get(
            "content",
            ""
        )


    if soup.title:

        return soup.title.text.strip()


    return ""


# -------------------------
# crawl interno
# -------------------------

def crawl_internal(

    seed_url,
    max_depth=2

):

    visitados=set()

    encontrados=[]

    try:

        dominio=urlparse(
            seed_url
        ).netloc

    except:

        return []


    fila=deque([

        (
            seed_url,
            0
        )

    ])


    while fila:


        if len(
            visitados
        )>=MAX_PAGES:

            break


        url,depth=fila.popleft()


        if depth>max_depth:

            continue


        if url in visitados:

            continue


        visitados.add(
            url
        )


        try:


            r=session.get(

                url,
                timeout=4

            )


            soup=BeautifulSoup(

                r.text,
                "lxml"

            )


            titulo=extract_title(
                soup
            ).lower()


            if any(

                termo in titulo

                for termo in ALL_KEYWORDS

            ):

                encontrados.append(
                    url
                )


            for a in soup.find_all(

                "a",
                href=True

            ):


                link=urljoin(

                    url,
                    a["href"]

                )


                if any(

                    x in link.lower()

                    for x in IGNORAR

                ):

                    continue


                p=urlparse(
                    link
                )


                if p.netloc!=dominio:

                    continue


                if any(

                    termo in link.lower()

                    for termo in EVENT_TERMS

                ):

                    fila.append(

                        (
                            link,
                            depth+1
                        )

                    )


        except:

            continue


    return encontrados


# -------------------------
# processa URL
# -------------------------

def process_url(url,r):

    global results


    try:


        if len(
            results
        )>=MAX_EVENTS:

            return


        if url in urls_visitadas:

            return


        urls_visitadas.add(
            url
        )


        page=session.get(

            url,
            timeout=4

        )


        soup=BeautifulSoup(

            page.text,
            "lxml"

        )


        text=soup.get_text(

            " ",
            strip=True

        ).lower()


        if not any(

            termo in text

            for termo in EVENT_TERMS

        ):

            return


        titulo=extract_title(
            soup
        ).lower()


        if not any(

            termo in titulo

            for termo in ALL_KEYWORDS

        ):

            return


        image=None


        og=soup.find(

            "meta",

            property="og:image"

        )


        if og:

            image=og.get(
                "content"
            )


        if not image:


            tw=soup.find(

                "meta",

                attrs={

                    "name":
                    "twitter:image"

                }

            )


            if tw:

                image=tw.get(
                    "content"
                )


        if not image:

            image=university_logo(
                url
            )


        texto_data=[]


        for linha in text.split("."):


            if any(

                x in linha

                for x in [

                    "data",
                    "evento",
                    "realização",
                    "acontece",
                    "ocorre",
                    "inscrição"

                ]

            ):

                texto_data.append(
                    linha
                )


        datas=search_dates(

            " ".join(
                texto_data
            ),

            languages=["pt"]

        )


        if not datas:

            return


        agora=datetime.now()

        limite=agora.replace(
            year=
            agora.year+2
        )


        futura=None


        for d in datas:


            data=d[1]


            if (

                agora
                <=data
                <=limite

            ):

                futura=data

                break


        if not futura:

            return


        results.append({

            "title":
            titulo,

            "date":
            futura.strftime(
                "%Y-%m-%d"
            ),

            "url":
            url,

            "excerpt":

            r.get(
                "body",
                ""
            ),

            "image":
            image

        })


        print(
            "Encontrado:",
            titulo
        )


    except:

        pass


# -------------------------
# BUSCA PRINCIPAL
# -------------------------

keywords_query=" OR ".join(

    [f'"{k}"' for k in ALL_KEYWORDS]

)


with DDGS() as ddgs:


    for site in SEARCH_SITES:


        if len(
            results
        )>=MAX_EVENTS:

            break


        query=(

            f'{site} ({keywords_query})'

        )


        print(
            "\nBuscando:",
            query
        )


        try:


            busca=ddgs.text(

                query,

                max_results=5

            )


            tarefas=[]


            for r in busca:


                url=r.get(
                    "href"
                )


                if not url:

                    continue


                urls=[url]


                internas=crawl_internal(

                    url,

                    max_depth=2

                )


                urls.extend(
                    internas
                )


                for u in urls:

                    tarefas.append(
                        (u,r)
                    )


            with ThreadPoolExecutor(

                max_workers=10

            ) as executor:


                executor.map(

                    lambda x:
                    process_url(
                        x[0],
                        x[1]
                    ),

                    tarefas

                )


        except:

            continue


# -------------------------
# remove duplicados
# -------------------------

unique={

x["url"]:x

for x in results

}


events=sorted(

unique.values(),

key=lambda x:
x["date"]

)


# -------------------------
# salva json
# -------------------------

arquivo=(

BASE_DIR/
"_data"/
"eventos.json"

)


arquivo.parent.mkdir(

parents=True,

exist_ok=True

)


with open(

arquivo,

"w",

encoding="utf8"

) as f:


    json.dump(

        events,

        f,

        ensure_ascii=False,

        indent=2

    )


print(
"\nEventos encontrados:",
len(events)
)

print(
    "Salvo em:",
    arquivo
)