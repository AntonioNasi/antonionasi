---
layout: blog
title: Blog
---

{% for post in site.posts %}
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

    <p>{{ post.excerpt }}</p>

  </div>

</article>
{% endfor %}