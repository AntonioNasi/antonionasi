const elementos = document.querySelectorAll('.bloco');

    const observer = new IntersectionObserver((entries) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          entry.target.classList.add('aparecer');
        }
      });
    }, {
      threshold: 0.2
    });

    elementos.forEach((elemento) => {
      observer.observe(elemento);
    });