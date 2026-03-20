---
layout: default
title: Início
---

<section class="sec-bvindo">
  <div class="cx-bvindo">
    <div class="item-bv">
      <a href="https://lattes.cnpq.br/6014284170206157" target="_blank">
        <img src="{{ '/assets/img/icone-formacao.png' | relative_url }}">
        <h4>Formação</h4>
        <hr>
        <p>Cão que Lattes, não morde. Dito isso, você pode conferir aqui o meu currículo.</p>
      </a>
    </div>
    <div class="item-bv" id="bordas">
      <a href="{{ '/publicados/' | relative_url }}">
        <img src="{{ '/assets/img/icone-publicacoes.png' | relative_url }}">
        <h4>Livros/Artigos</h4>
        <hr>
        <p>Algumas publicações, a maioria delas em parceria. Acesse e baixe grauitamente.</p>
      </a>
    </div>
    <div class="item-bv">
      <a href="{{ '/blog/' | relative_url }}">
        <img src="{{ '/assets/img/icone-postagens.png' | relative_url }}">
        <h4>Blog</h4>
        <hr>
        <p>Reflexões, opiniões, nada acadêmico. Sem periodicidade, escrevo quando posso.</p>
      </a>
    </div>
  </div>
</section>

<section class="sec-preview">

  <div class="cx-preview">

    {% for post in site.posts limit:5 %}

    <article class="post-preview">
        
      {% if post.image %}
        <a class="a-img" href="{{ post.url | relative_url }}">
              <img src="{{ post.image }}" alt="{{ post.title }}" class="post-thumb">
        </a>
      {% endif %}

      <div class="cx-txt-preview">

      <h2>
        <a href="{{ post.url | relative_url }}">{{ post.title }}</a>
      </h2>

      <p class="post-meta">
        {{ post.date | date: "%d/%m/%Y" }}
      </p>

      <p>{{ post.excerpt | strip_html | truncatewords: 15 }}</p>

      </div>
        
    </article>
    {% endfor %}

  </div>
  
</section>

<section class="new-books bloco">

    <div class="intro-sec-nb">
      
      <h2>Livros e Artigos</h2>
      <p>Conheça algumas de nossas últimas publicações</p>

    </div>

    <div class="cx-books">

      <div class="book">
        <div class="subcx">
          <img src="{{ '/assets/img/educação-ciência-e-formação-humana.png' | relative_url }}">
          <h3>Educação, ciência e formação humana: a produção de conhecimento a serviço da classe trabalhadora</h3>
          <p>Dr. Antonio Nasi - Dra. Júlia Bastos - Dra. Layslândia Santos (Lutas Anticapital, 2025)</p>
        </div>
        <a href="{{ '/assets/docs/iv-eniteessc-educação-ciência-e-formação-humana.pdf' | relative_url }}" download>Baixar</a>
      </div>

      <div class="book">
        <div class="subcx">
          <img src="{{ '/assets/img/marcadores-sociais-da-diferença.png' | relative_url }}">
          <h3>Arte e Religião: elementos para o processo de autonomia relativa do reflexo estético (cap)</h3>
          <p>Dr. Antonio Nasi - Dr. Adriano Lopes - Dr. Deribaldo Santos (Mentes Abertas - 2025)</p>
        </div>
        <a href="{{ '/assets/docs/Marcadores-sociais-da-diferença.pdf' | relative_url }}" download>Baixar</a>
      </div>

      <div class="book">
        <div class="subcx">
          <img src="{{ '/assets/img/lapps-marxismo-educação-e-formação-humana.png' | relative_url }}">
          <h3>LAPPS: Marxismo, educação e formação humana</h3>
          <p>Dr. Antonio Nasi - Dra. Layslândia Santos - Me. Lailton Santos (Lutas Anticapital - 2025)</p>
        </div>
        <a href="{{ '/assets/docs/lapps-marxismo-educação-e-formação-humana.pdf' }}" download >Baixar</a>
      </div>

      <div class="book">
        <div class="subcx">
          <img src="{{ '/assets/img/estética-educação-e-sociedade.png' | relative_url }}">
          <h3>Princípios básicos da diferenciação entre magia e religião (cap)</h3>
          <p>Dr. Antonio Nasi - Dra. Betânea Moraes - Dr. Deribaldo Santos (Acadêmica Editorial - 2022)</p>
        </div>
        <a href="{{ '/assets/docs/educação-estética-e-sociedade.pdf' }}" download >Baixar</a>
      </div>

      <div class="book">

        <div class="subcx">
          <img src="{{ '/assets/img/marx-e-a-crítica-ao-programa-de-gotha.png' | relative_url }}">
          <h3>Marx e a crítica ao Programa de Gotha</h3>
          <p>Dr. Antonio Nasi - Dr. Deribaldo Santos (Lutas Anticapital, 2021)</p>
        </div>
        
        <a href="{{ '/assets/docs/marx-e-a-crítica-ao-programa-de-gotha.pdf' }}" download >Baixar</a>

      </div>

    </div>

    <a id="button-books" href="https://antonionasi.com.br/publicados/">Mais publicações</a>

  </section>

<section class="sec-galeria bloco">
  <h2>Galeria de imagens</h2>
  <p>Momentos aleatórios, trabalho, pesquisa, mundo!</p>
  <div class="cx-galeria galeria">
    <div class="item-galeria">
      <img src="{{ '/assets/img/gl-1.jpeg' | relative_url }}">
    </div>
    <div class="item-galeria">
      <img src="{{ '/assets/img/gl-2.jpeg' | relative_url }}">
    </div>
    <div class="item-galeria">
      <img src="{{ '/assets/img/gl-3.jpeg' | relative_url }}">
    </div>
    <div class="item-galeria">
      <img src="{{ '/assets/img/gl-4.jpeg' | relative_url }}">
    </div>
    <div class="item-galeria">
      <img src="{{ '/assets/img/gl-5.jpeg' | relative_url }}">
    </div>
    <div class="item-galeria">
      <img src="{{ '/assets/img/gl-6.jpeg' | relative_url }}">
    </div>
    <div class="item-galeria">
      <img src="{{ '/assets/img/gl-7.jpeg' | relative_url }}">
    </div>
    <div class="item-galeria">
      <img src="{{ '/assets/img/gl-8.jpeg' | relative_url }}">
    </div>
  </div>

  <div class="lightbox" id="lightbox">
    <button class="fechar" id="fechar">&times;</button>
    <img id="imagem-ampliada" src="" alt="">
  </div>

  <script src="../assets/js/modal-galeria.js"></script>

  <script src="../assets/js/surgir.js"></script>

</section>