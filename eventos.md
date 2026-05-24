---
layout: single-page
title: Eventos acadêmicos
permalink: /eventos/
---

# Esta página está em fase de teste.

<div class="eventos-grid">

    {% assign eventos = site.eventos | sort: "date" | reverse %}

    {% for evento in eventos %}

    <article class="evento-card">

        {% if evento.image %}
        <img
            src="{{ evento.image }}"
            alt="{{ evento.title }}"
        >
        {% endif %}

        <h2>
            <a href="{{ evento.url }}">
                {{ evento.title }}
            </a>
        </h2>

        <small>
            {{ evento.date | date: "%d/%m/%Y" }}
        </small>

        <p>
            {{ evento.excerpt | strip_html | truncatewords: 15 }}
        </p>

    </article>

    {% endfor %}

</div>