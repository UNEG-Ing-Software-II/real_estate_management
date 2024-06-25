var map;
var currentMarker = null;

document.addEventListener("DOMContentLoaded", function () {
  // Evento para mostrar el modal
  var myModal = document.getElementById("ModalRegistroInmueble");
  myModal.addEventListener("shown.bs.modal", function () {
    if (!map) {
      // Inicializa el mapa cuando se muestra el modal
      map = L.map("map").setView([51.505, -0.09], 13);

      // Añade el tile layer desde OpenStreetMap
      L.tileLayer("https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png", {
        attribution:
          '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors',
      }).addTo(map);

      // Añade el geocodificador
      var geocoder = L.Control.geocoder({
        defaultMarkGeocode: false,
      })
        .on("markgeocode", function (e) {
          var bbox = e.geocode.bbox;
          map.fitBounds([
            [bbox.getSouthWest().lat, bbox.getSouthWest().lng],
            [bbox.getNorthEast().lat, bbox.getNorthEast().lng],
          ]);
          var latlng = e.geocode.center;

          // Evento de clic en el mapa
          map.on("click", function (e) {
            // Elimina el marcador actual si existe
            if (currentMarker) {
              map.removeLayer(currentMarker);
            }

            // Agrega un nuevo marcador
            currentMarker = L.marker(e.latlng)
              .addTo(map)
              .bindPopup(e.latlng.toString())
              .openPopup();

            // Actualiza los valores del formulario
            document.getElementById("CreateLatitude").value = e.latlng.lat;
            document.getElementById("CreateAltitude").value = e.latlng.lng;
          });
        })
        .addTo(map);
    } else {
      // Si el mapa ya fue inicializado, simplemente ajusta su tamaño
      map.invalidateSize();
    }
  });
});
