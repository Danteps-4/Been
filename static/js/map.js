// MAP COUNTRY SINGLE
if (document.getElementById('map')) {
    let point = JSON.parse(document.getElementById("point_json").textContent);
    var map = L.map('map').setView([point.latitude, point.longitude], 6);
    L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
        maxZoom: 19,
        attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>',
    }).addTo(map);
    L.marker([point.latitude, point.longitude]).addTo(map);
}

// MAP VISUALIZE con resalte de países seleccionados
if (document.getElementById('map2')) {
    let countries = JSON.parse(document.getElementById("countries_json").textContent);
    var map2 = L.map('map2').setView([0, 0], 2);

    // Añadir capa de mapa
    L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
        maxZoom: 19,
        attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>',
    }).addTo(map2);

    // Cargar GeoJSON y aplicar estilo a los países seleccionados
    fetch('/static/js/map.geojson')
        .then(response => response.json())
        .then(data => {
            L.geoJSON(data, {
                style: function (feature) {
                    // Verificar si el país está en la lista de seleccionados
                    let isSelected = countries.some(country => country.name === feature.properties.name);
                    return {
                        color: isSelected ? 'green' : 'gray',  // Resaltado en rojo para seleccionados
                        weight: isSelected ? 3 : 1,
                        fillOpacity: isSelected ? 0.5 : 0.1
                    };
                }
            }).addTo(map2);
        });
}
