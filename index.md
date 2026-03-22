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

<section class="sec-pesqDestaq">

  <div class="intro-pd">
    <h2>Pesquisadores Parceiros</h2>
    <p>Conheça alguns pesquisadores que colaboram com nosso trablho</p>
  </div>

  <div class="carrossel">
    <div class="linha"></div>
    <div class="track" id="track">
      <div class="item">
        <a href="https://lattes.cnpq.br/1153130807459034" target="_blank">
          <img src="{{ '/assets/img/kdantas.jpeg' | relative_url }}">
          <h3>Ma. Karollynne Dantas</h3>
          <p>Desenvolve pesquisa sobre o rebaixamento da personalidade a partir da ontologia marxiana-lukacsiana.</p>
        </a>
      </div>
      <div class="item">
        <a href="https://lattes.cnpq.br/1317529947912305" target="_blank">
          <img src="https://i.ytimg.com/vi/ZgbeLeSIWOg/maxresdefault.jpg">
        <h3>Dr. Deribaldo Santos</h3>
        <p>Densenvolve pesquisas sobre Estética lukacsiana e sobre educação técnico-profissionalizante.</p>
        </a>
      </div>
      <div class="item">
        <a href="https://lattes.cnpq.br/1027375323372139" target="_blank">
          <img src="https://scontent-for2-2.cdninstagram.com/v/t51.82787-15/622455229_18111117157632015_4597719095643964146_n.jpg?stp=dst-jpg_e35_tt6&_nc_cat=105&ig_cache_key=MjQxMjU1OTM0MTA0NTc2MDgzNQ%3D%3D.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjEwODB4MTA4MC5zZHIuQzMifQ%3D%3D&_nc_ohc=DkxssuaBF1IQ7kNvwGPudpF&_nc_oc=Adq-_RRT0lFf93GqPe89Dz_GU-h8OzLDLMkypuDuyREZTsKfxsml8pcKrlLmBpx3W_0&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-for2-2.cdninstagram.com&_nc_gid=2a-LLEAWiIeykw2RGbDs5Q&_nc_ss=7a32e&oh=00_AfyJ1Xrt3etHZsu8ejTK9CInJuQWfD8_1tG8BD68hVrnPQ&oe=69C60012">
        <h3>Dra. Layslândia Santos</h3>
        <p>Desenvolve pesquisa na área de educação, formação humana, trabalho e legislação educacional.</p>
        </a>
      </div>
      <div class="item">
        <a href="https://lattes.cnpq.br/0729806328978216" target="_blank">
          <img src="https://scontent-for2-2.cdninstagram.com/v/t51.82787-15/622048351_18191111734346695_7837215070876282784_n.jpg?stp=dst-jpg_e35_tt6&_nc_cat=105&ig_cache_key=MjM5MjQ4MjQwMzUyNTY0NjE3Mg%3D%3D.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjkzN3gxMTcxLnNkci5DMyJ9&_nc_ohc=dlLOauGqUj4Q7kNvwGTzTBT&_nc_oc=Adrnn6GY5g41Y4_7oWtfVHoicVn7slmCzfvjMqVizAmof77irJ31td5wmPCHFSgB6oU&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-for2-2.cdninstagram.com&_nc_gid=r1-9atn5QiQ97pIbLWjdMA&_nc_ss=7a32e&oh=00_Afy0qGVG8S27Hzr1Z0bjYhW7xGp1qBNv9UhGPfrmRfbfdw&oe=69C5E344">
        <h3>Ma. Janaira Teixeira</h3>
        <p>Desenvolve pesquisa sobre a formação da personalidade a partir da ontologia lukacsiana.</p>
        </a>
      </div>
      <div class="item">
        <a href="https://lattes.cnpq.br/0834231585359453" target="_blank">
          <img src="https://scontent-for2-1.cdninstagram.com/v/t51.82787-15/654578556_18092514047027944_5568926914562200003_n.jpg?stp=dst-jpg_e35_p1080x1080_tt6&_nc_cat=111&ig_cache_key=Mjc3MTUwNTgyMjQ3Nzg5NTQ0MQ%3D%3D.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjE0NDB4MTgwMC5zZHIuQzMifQ%3D%3D&_nc_ohc=3m2jD404gfwQ7kNvwHL58P5&_nc_oc=AdopCCCpJJLIf2qpsfHazH4syUWyULc4d9kFyFtHMlboxZgb7ik5E3Pv68s15K9dl4c&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-for2-1.cdninstagram.com&_nc_gid=w-0B-X0wAe0Sqaa10TnkaQ&_nc_ss=7a32e&oh=00_Afy8KznKeWacaQg940cXVCicfoG5VetpFy0OoNXNaqwffQ&oe=69C605ED">
        <h3>Dra. Betânia Moraes</h3>
        <p>Desenvolve pesquisa sobre formação humana, individualidade, aprendizagem e desenvolvimento humano-social.</p>
        </a>
      </div>
      <div class="item">
        <a href="https://lattes.cnpq.br/5700823644219229" target="_blank">
          <img src="https://scontent-for2-1.cdninstagram.com/v/t51.82787-15/541583185_18477891496072586_3976205061785408945_n.webp?_nc_cat=106&ig_cache_key=MzcxMTM1MjY2ODY1NzkzMTM3Ng%3D%3D.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjE0NDB4MTQ0MC5zZHIuQzMifQ%3D%3D&_nc_ohc=10EmvaZVAqQQ7kNvwFovyVz&_nc_oc=Ados8KtK0dGctRuFpQ63baS_jkc6I6MA8WtMkO-QCyScmcN32zciKDE1_dEY3NDhQt4&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-for2-1.cdninstagram.com&_nc_gid=OJAvFmnICMIENQCTX5T2rw&_nc_ss=7a32e&oh=00_AfzL75u4b-2aV7uuUsJCSzJRku4eC9EWO3CYxLMBmgrYkg&oe=69C60DC0">
        <h3>Dr. George Amaral</h3>
        <p>Desenvolve pesquisa sobre ensino profissional a partir do referencial marxista.</p>
        </a>
      </div>
    </div>
  </div>

  <script src="../assets/js/pesqdestaq.js" defer></script>

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