// main.js
document.addEventListener('DOMContentLoaded', () => {
    const totalCountries = 195;
    const visitedCountriesElement = document.querySelector('[data-visited-countries]');
    const visitedCountries = parseInt(visitedCountriesElement.dataset.visitedCountries, 10);
    const percentage = Math.round((visitedCountries / totalCountries) * 100);

    function updateProgress() {
        document.getElementById('countries-visited').innerText = visitedCountries;
        document.getElementById('percentage').innerText = `${percentage}%`;
        document.querySelector('.progress-circle').style.background = `conic-gradient(
            #ffbb33 ${percentage * 3.6}deg,
            #222 0deg
        )`;
    }

    // Llama a la función para inicializar los valores en la página
    updateProgress();
});

