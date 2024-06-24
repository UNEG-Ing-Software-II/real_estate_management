document.addEventListener("DOMContentLoaded", function() {
    var mapElement = document.getElementById('mapestate');
    var latitude = mapElement.getAttribute('data-latitude');
    var altitude = mapElement.getAttribute('data-altitude');

    var mapestate = L.map('mapestate').setView([latitude, altitude], 16);
    L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png').addTo(mapestate);
    L.marker([latitude, altitude]).addTo(mapestate).bindPopup('Inmueble').openPopup();
});