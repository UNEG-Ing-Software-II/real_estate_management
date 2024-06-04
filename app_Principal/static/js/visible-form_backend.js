// const Propietario = document.getElementById("Propietario");
const btn_special = document.getElementById("btn-special");
const Inputs = {
  Propiedad: document.getElementById("Tipo-Propiedad"),
  Estado: document.getElementById("InputEstado"),
  Precio: document.getElementById("InputPrecio"),
  Niveles: document.getElementById("InputNiveles"),
  M_Terrenos: document.getElementById("InputMetrosTerreno"),
  M_Construccion: document.getElementById("InputMetrosConstrucción"),
};

const visible = () => {
  if (Inputs.Propiedad.disabled === true) {
    btn_special.style.visibility = "visible";
    Inputs.Propiedad.disabled = false;
    Inputs.Estado.disabled = false;
    Inputs.Precio.disabled = false;
    Inputs.Niveles.disabled = false;
    Inputs.M_Terrenos.disabled = false;
    Inputs.M_Construccion.disabled = false;
  } else {
    btn_special.style.visibility = "hidden";
    Inputs.Propiedad.disabled = true;
    Inputs.Estado.disabled = true;
    Inputs.Precio.disabled = true;
    Inputs.Niveles.disabled = true;
    Inputs.M_Terrenos.disabled = true;
    Inputs.M_Construccion.disabled = true;
  }
};
