---
layout: single-page
title: Eventos acadêmicos
permalink: /eventos/
---

<h1 id="titulo-pgEvento">Esta página está em fase de teste.</h1>

<div class="eventos-grid">
    {% assign eventos = site.data.eventos %}
    {% for evento in eventos %}
    <article class="evento-card">
        <a href="{{ evento.url }}" target="_blank" rel="noopener noreferrer">
            <img src="{{ evento.image }}"
                alt="{{ evento.title }}">
            <h2>{{ evento.title }}</h2>
            <p class="data">{{ evento.date | date: "%d/%m/%Y" }}</p>
            <p>{{ evento.excerpt | strip_html | truncatewords: 15 }}</p>
        </a>
    </article>
    {% endfor %}
</div>