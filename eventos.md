---
layout: single-page
title: Eventos acadêmicos
permalink: /eventos/
---

# Eventos acadêmicos

<div class="cx-eventos">
    {% assign eventos = site.eventos | sort:"date" | reverse %}

    {% if eventos.size > 0 %}

    {% for evento in eventos %}

    <article>

        {% if evento.image %}

        <img
        src="{{evento.image}}"
        alt="{{evento.title}}"
        style="
        width:100%;
        max-height:250px;
        object-fit:cover;
        border-radius:8px;
        ">

        {% endif %}

        <h2>
        <a href="{{evento.url}}">
        {{evento.title}}
        </a>
        </h2>

        <small>
        {{evento.date | date:"%d/%m/%Y"}}
        </small>

        <p>

        {{evento.excerpt}}

        </p>

         {% endfor %}

        {% else %}

        Nenhum evento encontrado.

        {% endif %}

    </article>

</div>