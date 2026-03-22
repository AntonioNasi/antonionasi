(() => {
  if (window.__CARROSSEL_INIT__) return;
  window.__CARROSSEL_INIT__ = true;

    const track = document.getElementById('track');
    let items = document.querySelectorAll('.item');

    // 🔁 CLONAR (loop infinito real)
    const primeiro = items[0].cloneNode(true);
    const ultimo = items[items.length - 1].cloneNode(true);

    track.appendChild(primeiro);
    track.insertBefore(ultimo, track.firstChild);

    // atualizar lista após clone
    items = document.querySelectorAll('.item');

    let index = 1;

    // 🎯 FUNÇÃO DE CENTRALIZAÇÃO CORRIGIDA
    function centralizarItem(i, animate = true) {
    const item = items[i];

    const containerWidth = track.parentElement.offsetWidth;
    const itemCenter = item.offsetLeft + item.offsetWidth / 2;

    const translateX = itemCenter - containerWidth / 2;

    track.style.transition = animate ? "transform 0.5s ease" : "none";
    track.style.transform = `translateX(-${translateX}px)`;
    }

    // 🔄 ATUALIZA ESTADO
    function atualizar(animate = true) {
    items.forEach(el => el.classList.remove('ativo'));
    items[index].classList.add('ativo');

    centralizarItem(index, animate);
    }

    // inicial (sem animação)
    window.addEventListener('load', () => {
    atualizar(false);
    });

    // ▶ PRÓXIMO
    function proximo() {
    index++;
    atualizar(true);

    // chegou no clone do primeiro
    if (index === items.length - 1) {
        setTimeout(() => {
        index = 1;
        atualizar(false);
        }, 500);
    }
    }

    // ◀ ANTERIOR (extra - útil)
    function anterior() {
    index--;
    atualizar(true);

    if (index === 0) {
        setTimeout(() => {
        index = items.length - 2;
        atualizar(false);
        }, 500);
    }
    }

    // ⏱ AUTOPLAY
    setInterval(proximo, 3000);

})();