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

      👁️ <span class="busuanzi_value_page_pv"
           data-url="{{ post.url | absolute_url }}">0</span>
    </p>

    <p>{{ post.excerpt | strip_html | truncatewords: 15 }}</p>

  </div>

</article>
{% endfor %}