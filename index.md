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
    <div class="item-bv">
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
      
      <h2>Conheça algumas de nossas últimas publicações</h2>

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
  <div class="cx-galeria">
    <div class="item-galeria">
      <img src="https://www.56thparallel.com/wp-content/uploads/2020/04/Russian-village-tour-min-1.jpg">
    </div>
    <div class="item-galeria">
      <img src="https://upload.wikimedia.org/wikipedia/commons/0/0d/Russian_Landscape.jpg">
    </div>
    <div class="item-galeria">
      <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSxtS32WVQAqJzF2r_7J4TTFIXZRr0buJ3twQ&s">
    </div>
    <div class="item-galeria">
      <img src="https://mir-s3-cdn-cf.behance.net/project_modules/hd/dacf7659888371.5a32b938d8f57.jpg">
    </div>
    <div class="item-galeria">
      <img src="https://www.africanwildlifesafaris.com/wp-content/uploads/arctic-russian-highlights-landscapes.jpg">
    </div>
    <div class="item-galeria">
      <img src="https://i.redd.it/tiuhhf0kx5f51.jpg">
    </div>
    <div class="item-galeria">
      <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT99cHSEqApgLGigZZQx4_VJARe-9ZaCco-Bg&s">
    </div>
    <div class="item-galeria">
      <img src="https://www.expresstorussia.com/files/pages/016808.jpg">
    </div>
  </div>

  <script src="../assets/js/surgir.js"></script>

</section>