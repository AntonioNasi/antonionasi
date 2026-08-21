from dotenv import load_dotenv
import os
from urllib.parse import urlparse, urljoin
from collections import deque
from concurrent.futures import ThreadPoolExecutor, as_completed
from ddgs import DDGS
from bs4 import BeautifulSoup
import requests
import json
from dateparser.search import search_dates
from datetime import datetime, timedelta
from pathlib import Path
import time
import re
from typing import List, Dict, Set, Tuple, Optional
import logging
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

# Carrega variáveis de ambiente
load_dotenv()

# -------------------------
# CONFIGURAÇÃO DE LOGGING
# -------------------------

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('event_scraper.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

# -------------------------
# CONFIGURAÇÕES
# -------------------------

ALL_KEYWORDS = [
    "marxismo", "marx", "comunismo", "socialismo", "lukács", "lukacs", 
    "revolução socialista", "revolucao socialista", "revolução comunista", 
    "revolucao comunista", "eniteessc", "ENITEESSC", "materialismo histórico", 
    "materialismo historico", "materialismo histórico-dialético", 
    "materialismo historico-dialetico", "gramsci", "althusser", "teoria crítica"
]

INSTAGRAM_SEARCHES = [

    'site:instagram.com "marxismo"',
    'site:instagram.com "marx"',
    'site:instagram.com "socialismo"',
    'site:instagram.com "comunismo"',
    'site:instagram.com "ENITEESSC"',
    'site:instagram.com "materialismo histórico"',
    'site:instagram.com "seminário marxismo"',
    'site:instagram.com "encontro marxismo"',
    'site:instagram.com "seminário lukács"',
    'site:instagram.com "congresso lukács"',
    'site:instagram.com "encontro lukács"',
    'site:instagram.com "simpósio lukács"',
    'site:instagram.com "simpósio marxismo"',
    'site:instagram.com "simpósio marx"',
    'site:instagram.com "congresso marxismo"',
    'site:instagram.com "evento marxismo"',
]

EVENT_TERMS = [
    "evento", "eventos", "agenda", "seminario", "seminário",
    "congresso", "simposio", "simpósio", "coloquio", "colóquio",
    "encontro", "jornada", "conferência", "conferencia",
    "workshop", "oficina", "mesa redonda", "painel",
    "ciclo de debates", "debates", "lançamento", "lancamento"
]

SEARCH_SITES = [
    "site:ufac.br", "site:ufal.br", "site:unifap.br", "site:ufam.edu.br",
    "site:ufba.br", "site:ufob.edu.br", "site:ufrb.edu.br", "site:ufc.br",
    "site:ufca.edu.br", "site:unb.br", "site:ufes.br", "site:ufg.br",
    "site:ufj.edu.br", "site:ufcat.edu.br", "site:ufma.br", "site:ufmt.br",
    "site:ufms.br", "site:ufmg.br", "site:ufvjm.edu.br", "site:ufjf.br",
    "site:ufla.br", "site:ufop.br", "site:ufsj.edu.br", "site:ufu.br",
    "site:ufv.br", "site:ufpa.br", "site:ufpb.br", "site:ufcg.edu.br",
    "site:ufpe.br", "site:ufrpe.br", "site:univasf.edu.br", "site:ufpi.br",
    "site:ufpr.br", "site:utfpr.edu.br", "site:ufrj.br", "site:unirio.br",
    "site:uff.br", "site:ufrrj.br", "site:ufrn.br", "site:ufersa.edu.br",
    "site:ufrgs.br", "site:furg.br", "site:ufpel.edu.br", "site:unipampa.edu.br",
    "site:ufsm.br", "site:ufsc.br", "site:uffs.edu.br", "site:ufscar.br",
    "site:unifesp.br", "site:ufabc.edu.br", "site:ufs.br", "site:uft.edu.br",
    "site:ufopa.edu.br", "site:unifesspa.edu.br", "site:ufra.edu.br",
    "site:unilab.edu.br", "site:unila.edu.br", "site:ufape.edu.br",
    "site:ufr.edu.br", "site:ufdpar.edu.br", "site:ufnt.edu.br",
    "site:ufrr.br", "site:unifal-mg.edu.br", "site:ufcspa.edu.br",
    "site:ufpam.edu.br", "site:uece.br", "site:eventos.uece.br",
    "site:siseventos.uece.br", "site:uvanet.br", "site:urca.br",
    "site:usp.br", "site:unicamp.br", "site:unesp.br", "site:uerj.br",
    "site:uenf.br", "site:uemg.br", "site:unimontes.br", "site:uel.br",
    "site:uem.br", "site:uepg.br", "site:unioeste.br", "site:unicentro.br",
    "site:unespar.edu.br", "site:uneb.br", "site:uefs.br", "site:uesb.br",
    "site:uesc.br", "site:uea.edu.br", "site:uepa.br", "site:udesc.br",
    "site:uepb.edu.br", "site:upe.br", "site:uern.br", "site:uema.br",
    "site:uemasul.edu.br", "site:uespi.br", "site:ueg.br", "site:unitins.br",
    "site:uerr.edu.br", "site:unemat.br", "site:even3.com.br", "site:doity.com.br"
]

# Lista de perfis do Instagram (será usada apenas se login funcionar)
INSTAGRAM_PROFILES = [
    "ueceoficial", "feclescoficial", "boitempoeditorial", "eniteessc",
    "esquerdadiario", "marxismo21", "escolanacionalflorestanfernandes",
    "ufac_oficial", "unifapoficial", "ufam", "ufpa_oficial", "ufopaoficial",
    "unir_oficial", "ufrroficial", "uftoficial", "ufaloficial", "ufba",
    "ufrb_edu", "ufsb_oficial2", "ufoboficial", "univasf", "ufcinforma",
    "ufcaoficial", "ufmaoficial", "ufpb.oficial", "ufcg_oficial", "ufpe",
    "ufrpe", "ufape.oficial", "ufpi", "ufdpar.br", "ufrn", "ufsoficial",
    "ufesoficial", "unifalmg", "unifei_oficial", "ufjf", "uflabr", "ufmg",
    "minhaufop", "ufsjbr", "ufu_oficial", "ufvbroficial", "uftm_oficial",
    "unirio_oficial", "ufrj_oficial", "uff.br", "ufrrj", "ufabc", "ufscaroficial",
    "unifespoficial", "ufpr_oficial", "utfpr_oficial", "instaunila",
    "escolhiseruffs", "oficialfurg", "ufrgs", "ufcspaoficial", "ufpeloficial",
    "ufsm.br", "unipampa", "universidadeufsc"
]

# URLs de feeds de eventos alternativos
ALTERNATIVE_FEEDS = [
    "https://www.instagram.com/explore/tags/marxismo/",
    "https://www.instagram.com/explore/tags/socialismo/",
    "https://www.instagram.com/explore/tags/eventoacademico/",
    "https://www.instagram.com/explore/tags/congressomarx/",
]

MAX_PAGES = 30
MAX_EVENTS = 50
MAX_WORKERS = 5
REQUEST_TIMEOUT = 10
RETRY_COUNT = 3
CRAWL_DELAY = 0.5
MAX_INSTAGRAM_POSTS_PER_PROFILE = 20

IGNORAR = [
    ".pdf", ".jpg", ".jpeg", ".png", ".gif", ".zip", ".doc", ".docx",
    "/tag/", "/feed/", "/author/", "/wp-content/", "/wp-includes/",
    "/noticia/", "/noticias/", "/news/", "/article/", "/artigo/",
    "/materia/", "/blog/", "/post/", "/categoria/", "/category/",
    "#", "javascript:", "mailto:", "tel:", "/pdf/", "/download/"
]

BASE_DIR = Path(__file__).resolve().parent.parent

# -------------------------
# SESSÃO CONFIGURADA
# -------------------------

def create_session() -> requests.Session:
    """Cria uma sessão com retry e timeouts configurados"""
    session = requests.Session()
    
    retry_strategy = Retry(
        total=RETRY_COUNT,
        backoff_factor=1,
        status_forcelist=[429, 500, 502, 503, 504],
    )
    
    adapter = HTTPAdapter(
        max_retries=retry_strategy,
        pool_connections=10,
        pool_maxsize=20
    )
    
    session.mount("http://", adapter)
    session.mount("https://", adapter)
    
    session.headers.update({
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "Accept-Language": "pt-BR,pt;q=0.9,en;q=0.8",
        "Accept-Encoding": "gzip, deflate",
        "Connection": "keep-alive",
    })
    
    return session

session = create_session()

# -------------------------
# FUNÇÕES AUXILIARES
# -------------------------

def university_logo(url: str) -> str:
    """Retorna URL do logo/favicon da universidade"""
    try:
        p = urlparse(url)
        logo_paths = [
            "/favicon.ico",
            "/logo.png",
            "/images/logo.png",
            "/assets/logo.png",
            "/static/logo.png"
        ]
        
        for path in logo_paths:
            logo_url = f"{p.scheme}://{p.netloc}{path}"
            try:
                response = session.head(logo_url, timeout=3)
                if response.status_code == 200:
                    return logo_url
            except:
                continue
        
        return f"{p.scheme}://{p.netloc}/favicon.ico"
    except:
        return "https://via.placeholder.com/300x200?text=Evento+Acadêmico"

def extract_title(soup: BeautifulSoup) -> str:
    """Extrai título da página com múltiplas estratégias"""
    h1 = soup.find("h1")
    if h1 and h1.get_text(strip=True):
        title = h1.get_text(strip=True)
        if len(title) > 10:
            return title
    
    og = soup.find("meta", property="og:title")
    if og and og.get("content"):
        title = og.get("content").strip()
        if len(title) > 10:
            return title
    
    if soup.title and soup.title.string:
        title = soup.title.string.strip()
        if len(title) > 10:
            return title
    
    h2 = soup.find("h2")
    if h2 and h2.get_text(strip=True):
        title = h2.get_text(strip=True)
        if len(title) > 10:
            return title
    
    return "Evento Acadêmico"

def extract_description(soup: BeautifulSoup, url: str = "") -> str:
    """Extrai descrição/resumo da página"""
    meta_desc = soup.find("meta", attrs={"name": "description"})
    if meta_desc and meta_desc.get("content"):
        desc = meta_desc.get("content").strip()
        if len(desc) > 20:
            return desc
    
    og_desc = soup.find("meta", property="og:description")
    if og_desc and og_desc.get("content"):
        desc = og_desc.get("content").strip()
        if len(desc) > 20:
            return desc
    
    tw_desc = soup.find("meta", attrs={"name": "twitter:description"})
    if tw_desc and tw_desc.get("content"):
        desc = tw_desc.get("content").strip()
        if len(desc) > 20:
            return desc
    
    description_classes = ["description", "desc", "abstract", "resumo", "sobre", "about"]
    for class_name in description_classes:
        desc_div = soup.find("div", class_=re.compile(class_name, re.I))
        if desc_div:
            text = desc_div.get_text(strip=True)
            if len(text) > 50:
                return text[:300]
    
    for p in soup.find_all("p"):
        text = p.get_text(strip=True)
        if len(text) > 80:
            text = re.sub(r'\s+', ' ', text)
            return text[:300] + "..." if len(text) > 300 else text
    
    body_text = soup.get_text(" ", strip=True)
    if len(body_text) > 200:
        return body_text[:200] + "..."
    
    return ""

def extract_image(soup: BeautifulSoup, url: str) -> str:
    """Extrai URL da imagem do evento"""
    og_img = soup.find("meta", property="og:image")
    if og_img and og_img.get("content"):
        return make_absolute_url(og_img.get("content"), url)
    
    tw_img = soup.find("meta", attrs={"name": "twitter:image"})
    if tw_img and tw_img.get("content"):
        return make_absolute_url(tw_img.get("content"), url)
    
    schema_img = soup.find("meta", attrs={"itemprop": "image"})
    if schema_img and schema_img.get("content"):
        return make_absolute_url(schema_img.get("content"), url)
    
    img_tags = soup.find_all("img", src=True)
    priority_keywords = ["banner", "header", "evento", "logo", "destaque", "featured"]
    
    for img in img_tags:
        src = img.get("src")
        alt = img.get("alt", "").lower()
        class_name = img.get("class", [])
        class_str = " ".join(class_name).lower()
        
        is_relevant = any(keyword in alt or keyword in class_str for keyword in priority_keywords)
        
        if src and (is_relevant or len(img_tags) <= 3):
            img_url = make_absolute_url(src, url)
            if img_url and not any(x in img_url.lower() for x in ["icon", "avatar", "thumb"]):
                return img_url
    
    return university_logo(url)

def make_absolute_url(url: str, base_url: str) -> str:
    """Converte URL relativa para absoluta"""
    if not url:
        return ""
    
    if url.startswith("//"):
        return f"https:{url}"
    elif url.startswith("/"):
        return urljoin(base_url, url)
    elif not url.startswith("http"):
        return urljoin(base_url, url)
    return url

def extract_dates_from_text(text: str) -> List[datetime]:
    """Extrai datas do texto com validação melhorada"""
    if not text:
        return []
    
    text = re.sub(r'http\S+', '', text)
    text = re.sub(r'[^\w\s.,/:/-]', ' ', text)
    
    patterns = [
        r'(\d{1,2}[/-]\d{1,2}[/-]\d{4})',
        r'(\d{1,2}\s+de\s+\w+\s+de\s+\d{4})',
        r'(\d{1,2}[/-]\d{1,2}[/-]\d{2,4})',
        r'(\d{1,2}\s+/\s+\d{1,2}\s+/\s+\d{4})',
    ]
    
    dates = []
    
    for pattern in patterns:
        matches = re.findall(pattern, text.lower())
        for match in matches:
            parsed = search_dates(match, languages=["pt"])
            if parsed:
                dates.extend([d[1] for d in parsed])
    
    if not dates:
        date_keywords = ["data", "dia", "quando", "realização", "acontecerá", "ocorrerá"]
        sentences = text.split(".")
        for sentence in sentences:
            if any(keyword in sentence.lower() for keyword in date_keywords):
                parsed = search_dates(sentence, languages=["pt"])
                if parsed:
                    dates.extend([d[1] for d in parsed])
    
    return dates

def is_relevant_event(titulo: str, text: str) -> bool:
    """Verifica se o evento é relevante para os temas buscados"""
    titulo_lower = titulo.lower()
    text_lower = text.lower()

    if "instagram.com" in text_lower:

        if any(
            kw.lower() in text_lower
            for kw in ALL_KEYWORDS
        ):

            return True
    
    has_event_term = any(termo in titulo_lower for termo in EVENT_TERMS)
    if not has_event_term:
        has_event_term = any(termo in text_lower for termo in EVENT_TERMS[:10])
    
    if not has_event_term:
        return False
    
    main_keywords = ALL_KEYWORDS[:5]
    has_main_keyword = any(kw in titulo_lower or kw in text_lower for kw in main_keywords)
    
    if has_main_keyword:
        return True
    
    has_secondary_keyword = any(kw in titulo_lower or kw in text_lower for kw in ALL_KEYWORDS[5:15])
    
    return has_secondary_keyword

def clean_url(url: str) -> Optional[str]:
    """Limpa e valida URL"""
    if not url:
        return None
    
    url = url.split('#')[0]
    
    if any(ign in url.lower() for ign in IGNORAR):
        return None
    
    return url

# -------------------------
# BUSCA ALTERNATIVA (SEM LOGIN)
# -------------------------

def search_instagram_public_posts() -> List[dict]:
    """
    Busca posts públicos do Instagram sem necessidade de login
    Usa métodos alternativos como pesquisa por hashtags via scraping básico
    """
    eventos = []
    
    # Hashtags relevantes para busca
    hashtags = [
        "marxismo", "socialismo", "eventoacademico", 
        "seminariomarx", "congressocomunismo", "eniteessc", "lukacs", "encontro", "congressomarxismo"
    ]
    
    # URLs públicas do Instagram (acessíveis sem login)
    for hashtag in hashtags:
        try:
            # URL pública da hashtag
            url = f"https://www.instagram.com/explore/tags/{hashtag}/"
            
            # Nota: O Instagram bloqueia scraping simples, mas podemos tentar
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                'Accept-Language': 'pt-BR,pt;q=0.9,en;q=0.8',
            }
            
            response = requests.get(url, headers=headers, timeout=10)
            
            if response.status_code == 200:
                logger.info(f"Hashtag #{hashtag} acessada com sucesso")
                # Nota: O conteúdo é carregado via JavaScript, então scraping direto é limitado
                # Esta é uma solução parcial - recomendamos usar APIs pagas ou serviços especializados
                
        except Exception as e:
            logger.debug(f"Erro ao acessar hashtag #{hashtag}: {e}")
    
    return eventos

# -------------------------
# CRAWLER
# -------------------------

def crawl_internal(seed_url: str, max_depth: int = 2) -> List[str]:
    """Crawl interno melhorado com delay e validação"""
    visited = set()
    found_urls = []
    
    try:
        dominio = urlparse(seed_url).netloc
        if not dominio:
            return []
    except:
        return []
    
    queue = deque([(seed_url, 0)])
    
    while queue and len(visited) < MAX_PAGES:
        url, depth = queue.popleft()
        
        if depth > max_depth or url in visited:
            continue
        
        visited.add(url)
        
        try:
            time.sleep(CRAWL_DELAY)
            response = session.get(url, timeout=REQUEST_TIMEOUT)
            response.raise_for_status()
            
            soup = BeautifulSoup(response.text, "lxml")
            
            titulo = extract_title(soup).lower()
            text = soup.get_text(" ", strip=True).lower()
            
            if is_relevant_event(titulo, text):
                found_urls.append(url)
            
            for a in soup.find_all("a", href=True):
                link = urljoin(url, a["href"])
                link = clean_url(link)
                
                if not link:
                    continue
                
                link_parsed = urlparse(link)
                if link_parsed.netloc != dominio:
                    continue
                
                link_lower = link.lower()
                event_indicators = ["evento", "seminario", "congresso", "simpósio", "encontro"]
                if any(indicator in link_lower for indicator in event_indicators):
                    if link not in visited and link not in [u for u, _ in queue]:
                        queue.append((link, depth + 1))
        
        except Exception as e:
            logger.debug(f"Erro em {url}: {e}")
            continue
    
    return found_urls

# -------------------------
# PROCESSAMENTO DE URL
# -------------------------

def process_url(url: str, search_result: dict = None) -> Optional[dict]:
    """Processa URL individual e retorna evento se válido"""
    
    try:
        logger.info(f"Processando: {url}")
        time.sleep(CRAWL_DELAY)
        
        response = session.get(url, timeout=REQUEST_TIMEOUT)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.text, "lxml")
        
        titulo = extract_title(soup)
        descricao = extract_description(soup, url)
        texto_completo = soup.get_text(" ", strip=True).lower()
        
        if not is_relevant_event(titulo, texto_completo):
            logger.debug(f"Irrelevante: {titulo}")
            return None
        
        # Extrai datas
        date_areas = []
        
        meta_date_fields = [
            ("article:published_time", "content"),
            ("date", "content"),
            ("event_date", "content"),
            ("startDate", "content")
        ]
        
        for meta_name, attr in meta_date_fields:
            meta = soup.find("meta", attrs={"name": meta_name})
            if not meta:
                meta = soup.find("meta", attrs={"property": meta_name})
            if meta and meta.get(attr):
                date_areas.append(meta.get(attr))
        
        time_tags = soup.find_all("time")
        for time_tag in time_tags:
            datetime_attr = time_tag.get("datetime")
            if datetime_attr:
                date_areas.append(datetime_attr)
            elif time_tag.string:
                date_areas.append(time_tag.string)
        
        lines = texto_completo.split(".")
        for i, line in enumerate(lines):
            date_keywords = ["data:", "realização:", "quando:", "período:", "acontecerá:", "ocorrerá:"]
            if any(keyword in line for keyword in date_keywords):
                context = " ".join(lines[i:min(i+3, len(lines))])
                date_areas.append(context)
        
        date_areas.append(texto_completo[:800])
        
        all_dates = []
        for area in date_areas:
            if area:
                dates = extract_dates_from_text(area)
                all_dates.extend(dates)
        
        if not all_dates:
            logger.debug(f"Sem datas encontradas: {titulo[:50]}")
            return None
        
        agora = datetime.now()
        limite_futuro = agora + timedelta(days=365*2)
        datas_validas = [d for d in all_dates if agora <= d <= limite_futuro]
        
        if not datas_validas:

            if "instagram.com" in url:

                data_evento = (
                    datetime.now()
                    + timedelta(days=30)
                )

            else:

                return None

        else:

            data_evento = min(datas_validas)
        
        
        imagem = extract_image(soup, url)
        
        if not descricao or len(descricao) < 20:
            paragraphs = soup.find_all("p")
            for p in paragraphs:
                text = p.get_text(strip=True)
                if len(text) > 80:
                    descricao = text[:300] + "..." if len(text) > 300 else text
                    break
            if not descricao:
                descricao = texto_completo[:200] + "..." if len(texto_completo) > 200 else texto_completo
        
        evento = {
            "title": titulo,
            "date": data_evento.strftime("%Y-%m-%d"),
            "date_display": data_evento.strftime("%d/%m/%Y"),
            "url": url,
            "excerpt": descricao,
            "image": imagem,
            "source_domain": urlparse(url).netloc
        }
        
        logger.info(f"✓ Evento: {titulo[:60]} - {data_evento.strftime('%d/%m/%Y')}")
        return evento
        
    except requests.exceptions.Timeout:
        logger.warning(f"Timeout: {url}")
    except requests.exceptions.RequestException as e:
        logger.warning(f"Erro HTTP {url}: {e}")
    except Exception as e:
        logger.warning(f"Erro: {url} - {e}")
    
    return None

# -------------------------
# FUNÇÃO PRINCIPAL
# -------------------------

def main():
    """Função principal orquestrando a busca"""
    logger.info("=" * 60)
    logger.info("Iniciando busca por eventos acadêmicos")
    logger.info("=" * 60)
    
    all_events = []
    processed_urls = set()
    
    # Tentativa de busca no Instagram (sem login)
    logger.info("\n📸 Verificando possibilidade de busca no Instagram...")
    logger.info("⚠️  O Instagram requer autenticação para scraping. Pulando busca no Instagram.")
    logger.info("💡 Recomendações para incluir Instagram:")
    logger.info("   1. Use o Apify (apify.com) - serviço especializado")
    logger.info("   2. Configure uma conta Instagram dedicada")
    logger.info("   3. Use a API oficial do Instagram (requer aprovação)")
    
    # Busca nos sites acadêmicos (principal fonte)
    keywords_query = " OR ".join([f'"{k}"' for k in ALL_KEYWORDS[:10]])
    
    with DDGS() as ddgs:

        logger.info("Buscando Instagram indexado")

        for query in INSTAGRAM_SEARCHES:

            try:

                resultados = list(
                    ddgs.text(
                        query,
                        max_results=20
                    )
                )

                for r in resultados:

                    url = r.get("href")

                    if not url:
                        continue

                    if url in processed_urls:
                        continue

                    processed_urls.add(url)

                    evento = process_url(url, r)

                    if evento:

                        all_events.append(evento)

                        logger.info(
                            f"Instagram: {evento['title']}"
                        )

            except Exception as e:

                logger.warning(
                    f"Erro Instagram: {e}"
                )

        for site in SEARCH_SITES:
            if len(all_events) >= MAX_EVENTS:
                break
            
            query = f'{site} ({keywords_query})'
            logger.info(f"\n🔍 Buscando: {query}")
            
            try:
                search_results = list(ddgs.text(query, max_results=10))
                logger.info(f"Encontrados {len(search_results)} resultados iniciais")
                
                for result in search_results:
                    if len(all_events) >= MAX_EVENTS:
                        break
                    
                    url = result.get("href")
                    if not url or url in processed_urls:
                        continue
                    
                    processed_urls.add(url)
                    
                    logger.info(f"Explorando: {urlparse(url).netloc}")
                    internas = crawl_internal(url, max_depth=2)
                    todas_urls = [url] + internas
                    todas_urls = list(dict.fromkeys(todas_urls))[:MAX_PAGES]
                    
                    logger.info(f"Processando {len(todas_urls)} URLs do domínio")
                    
                    with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
                        future_to_url = {
                            executor.submit(process_url, u, result): u 
                            for u in todas_urls
                            if u not in processed_urls
                        }
                        
                        for future in as_completed(future_to_url):
                            evento = future.result()
                            if evento:
                                all_events.append(evento)
                                processed_urls.add(evento["url"])
                                logger.info(f"Progresso: {len(all_events)}/{MAX_EVENTS}")
                            
                            if len(all_events) >= MAX_EVENTS:
                                break
            
            except Exception as e:
                logger.error(f"Erro na busca para {site}: {e}")
                continue
    
    # Remove duplicatas
    unique_events = {}
    for event in all_events:
        if event["url"] not in unique_events:
            unique_events[event["url"]] = event
    
    # Ordena por data
    events_sorted = sorted(
        unique_events.values(),
        key=lambda x: x["date"]
    )
    
    # Prepara JSON
    output_data = events_sorted
    
    # Salva resultados
    data_dir = BASE_DIR / "_data"
    data_dir.mkdir(parents=True, exist_ok=True)
    
    output_file = data_dir / "eventos.json"
    
    with open(output_file, "w", encoding="utf8") as f:
        json.dump(output_data, f, ensure_ascii=False, indent=2)
    
    # Backup com metadados
    backup_file = data_dir / "eventos_backup.json"
    backup_data = {
        "total_events": len(events_sorted),
        "instagram_events": len([e for e in events_sorted if "instagram" in e.get("source_domain", "")]),
        "web_events": len([e for e in events_sorted if "instagram" not in e.get("source_domain", "")]),
        "last_update": datetime.now().isoformat(),
        "events": events_sorted
    }
    with open(backup_file, "w", encoding="utf8") as f:
        json.dump(backup_data, f, ensure_ascii=False, indent=2)
    
    # Relatório final
    logger.info("\n" + "=" * 60)
    logger.info(f"✅ Busca concluída!")
    logger.info(f"📊 Total de eventos: {len(events_sorted)}")
    logger.info(f"🌐 Sites acadêmicos: {len([e for e in events_sorted if 'instagram' not in e.get('source_domain', '')])}")
    logger.info(f"📁 JSON salvo em: {output_file}")
    logger.info("=" * 60)
    
    # Mostra próximos eventos
    if events_sorted:
        logger.info("\n📅 Próximos eventos:")
        for i, event in enumerate(events_sorted[:5], 1):
            logger.info(f"{i}. {event['title'][:80]}")
            logger.info(f"   📍 Data: {event['date_display']}")
            logger.info(f"   🔗 {event['url'][:80]}...\n")

if __name__ == "__main__":
    main()