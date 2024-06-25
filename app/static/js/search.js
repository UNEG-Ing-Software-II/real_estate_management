document.getElementById('searchForm').addEventListener('submit', function(event) {
    var searchInput = document.getElementById('searchInput').value;
    if (!searchInput.trim()) {
        event.preventDefault(); // Previene el envío del formulario
        alert('Por favor, introduce un término de búsqueda.'); // Muestra un mensaje de alerta
    }
});