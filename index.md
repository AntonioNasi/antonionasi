---
layout: default
title: Início
---

{% for post in site.posts limit:5 %}

<article class="post-preview">

  {% if post.image %}
    <a href="{{ post.url | relative_url }}">
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

<section class="new-books">

    <h2>Últimas publicações</h2>

    <div class="cx-books">

      <div class="book">
        <div class="subcx">
          <img src="{{ '/assets/img/educação-ciência-e-formação-humana.png' | relative_url }}">
          <h3>Educação, ciência e formação humana: a produção de conhecimento a serviço da classe trabalhadora</h3>
          <p>Dr. Antonio Nasi - Dra. Júlia Bastos - Me. Layslância Santos (Lutas Anticapital, 2025)</p>
        </div>
        <a href="{{ '/assets/docs/iv-eniteessc-educação-ciência-e-formação-humana.pdf' | relative_url }}" download>Baixar</a>
      </div>

      <div class="book">
        <div class="subcx">
          <img src="{{ '/assets/img/marcadores-sociais-da-diferença.png' | relative_url }}">
          <h3>Arte e Religião: elementos para o processo de autonomia relativa do reflexo estético (cap)</h3>
          <p>Antonio Nasi - Adriano Lopes - Deribaldo Santos (Mentes Abertas - 2025)</p>
        </div>
        <a href="{{ '/assets/docs/Marcadores-sociais-da-diferença.pdf' | relative_url }}" download>Baixar</a>
      </div>

      <div class="book">
        <div class="subcx">
          <img src="{{ '/assets/img/lapps-marxismo-educação-e-formação-humana.png' | relative_url }}">
          <h3>LAPPS: Marxismo, educação e formação humana</h3>
          <p>Dr. Antonio Nasi - Me. Layslândia Santos - Me. Lailton Santos (Lutas Anticapital - 2025)</p>
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