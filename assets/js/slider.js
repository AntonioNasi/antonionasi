const slider = document.getElementById("featuredSlider");
        const slides = slider.children;
        const dotsContainer = document.getElementById("sliderDots");

        let index = 0;
        let interval = 5000; // 5 segundos

        // Criar dots
        [...slides].forEach((_, i) => {
        const dot = document.createElement("span");
        dot.onclick = () => goToSlide(i);
        dotsContainer.appendChild(dot);
        });

        function updateDots() {
        [...dotsContainer.children].forEach(dot => dot.classList.remove("active"));
        dotsContainer.children[index].classList.add("active");
        }

        function goToSlide(i) {
        index = i;
        slider.style.transform = `translateX(-${index * 100}%)`;
        updateDots();
        }

        function nextSlide() {
        index = (index + 1) % slides.length;
        goToSlide(index);
        }

        updateDots();
        setInterval(nextSlide, interval);