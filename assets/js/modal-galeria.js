const imagens = document.querySelectorAll('.galeria img');
    const lightbox = document.getElementById('lightbox');
    const imagemAmpliada = document.getElementById('imagem-ampliada');
    const fechar = document.getElementById('fechar');

    imagens.forEach((img) => {
      img.addEventListener('click', () => {
        imagemAmpliada.src = img.dataset.full || img.src;
        imagemAmpliada.alt = img.alt;
        lightbox.classList.add('ativo');
      });
    });

    fechar.addEventListener('click', () => {
      lightbox.classList.remove('ativo');
      imagemAmpliada.src = '';
    });

    lightbox.addEventListener('click', (e) => {
      if (e.target === lightbox) {
        lightbox.classList.remove('ativo');
        imagemAmpliada.src = '';
      }
    });

    document.addEventListener('keydown', (e) => {
      if (e.key === 'Escape') {
        lightbox.classList.remove('ativo');
        imagemAmpliada.src = '';
      }
    });