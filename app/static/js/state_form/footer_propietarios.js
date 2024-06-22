document.addEventListener('DOMContentLoaded', function() {
    // Pestañas
    const buscarTab = document.getElementById('buscar-tab');
    const registrarTab = document.getElementById('registrar-tab');
    const eliminarTab = document.getElementById('eliminar-tab')

    // Botones
    const guardarBtn = document.getElementById('guardarBtn');
    const registrarBtn = document.getElementById('registrarBtn');
    const eliminarBtn = document.getElementById('eliminarBtn');
    
    // Funcion para el cambio de pestaña
    function toggleButtons() {
        if (buscarTab.classList.contains('active')) {
            guardarBtn.classList.remove('d-none');
            registrarBtn.classList.add('d-none');
            eliminarBtn.classList.add('d-none');
        } else if (registrarTab.classList.contains('active')) {
            guardarBtn.classList.add('d-none');
            registrarBtn.classList.remove('d-none');
            eliminarBtn.classList.add('d-none');
        } else if (eliminarTab.classList.contains('active')){
            guardarBtn.classList.add('d-none');
            registrarBtn.classList.add('d-none');
            eliminarBtn.classList.remove('d-none');
        }
    }
    
    toggleButtons();
    // Cambio de pestaña
    buscarTab.addEventListener('click', toggleButtons);
    registrarTab.addEventListener('click', toggleButtons);
    eliminarTab.addEventListener('click', toggleButtons);
});