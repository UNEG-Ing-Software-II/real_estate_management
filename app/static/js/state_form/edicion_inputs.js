const btn_special = document.getElementById("btn-special");
        const Inputs = {
            Nombre: document.getElementById("InputNombre"),
            Propiedad: document.getElementById("Tipo-Propiedad"),
            Estado: document.getElementById("InputEstado"),
            Precio: document.getElementById("InputPrecio"),
            Niveles: document.getElementById("InputNiveles"),
            M_Terrenos: document.getElementById("InputMetrosTerreno"),
            M_Construccion: document.getElementById("InputMetrosConstrucción"),
            Bathroom: document.getElementById("InputBathroom"),
            CuartoServicio: document.getElementById("InputCuartoServicio"),
            Oficina: document.getElementById("InputOficina"),
            Estacionamiento: document.getElementById("InputEstacionamiento"),
            HalfBath: document.getElementById("InputHalfBath"),
            Terraza: document.getElementById("InputTerraza"),
            Habitacion: document.getElementById("InputHabitacion"),
            Maletero: document.getElementById("InputMaletero"),
            Direccion: document.getElementById("InputDireccion"),
            Latitud: document.getElementById("InputLatitud"),
            Longitud: document.getElementById("InputLongitud"),
            Fotos: document.getElementById("InputFotos"), 
            deleteButtons: document.querySelectorAll('.btn-img')
        };
    
        const visible = () => {
            const isDisabled = Inputs.Propiedad.disabled;
            Object.keys(Inputs).forEach(key => {
                Inputs[key].disabled = !isDisabled;
            });
    
            Inputs.deleteButtons.forEach(button => {
                button.hidden = !isDisabled;
            });
                
            btn_special.style.visibility = isDisabled ? "visible" : "hidden";
        };
        
        const deletedImages = [];

        function deleteImage(imageId) {
            const imageContainer = document.getElementById(`image-${imageId}`);
            if (imageContainer) {
                imageContainer.remove();
                deletedImages.push(imageId);
                console.log(deletedImages);
                const deletedImagesInput = document.getElementById('deletedImagesInput');
                const deletedImagesJSON = JSON.stringify(deletedImages);
                deletedImagesInput.value = deletedImagesJSON;
                //console.log(deletedImagesInput);
            }
        }
    