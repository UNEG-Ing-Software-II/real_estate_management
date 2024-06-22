
function submitForm(areaId) {
    var checkboxes = document.querySelectorAll('#modificarAreaForm' + areaId + ' input[type="checkbox"]');
    var isChecked = false;

    for (var i = 0; i < checkboxes.length; i++) {
        if (checkboxes[i].checked) {
            isChecked = true;
            break;
        }
    }
    
    if (!isChecked) {
        alert('Debes marcar al menos una característica.');
        return;
    }
    document.getElementById('modificarAreaForm' + areaId).submit();
}