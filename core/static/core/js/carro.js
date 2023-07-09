const miLocalStorage = window.localStorage;
$(document).ready(function () {
  var divisa = cargarDivisa().divisa;
  var valorDivisa = cargarDivisa().valorDivisa;
  console.log(divisa, valorDivisa);
  $(".precio").each(function () {
    var precioTexto = $(this).text();
    var precioEntero = parseInt(precioTexto, 10);
    var precio = Math.round(valorDivisa * precioEntero * 100) / 100;
    var precioFinal = precio.toLocaleString("en-IN");
    $(this).html(precioFinal + " " + divisa);
  });
});
function anyadirProductoAlCarrito(usuario_rut, producto_id, op) {
  const formData = new FormData();
  formData.append("usuario_rut", usuario_rut);
  formData.append("producto_id", producto_id);
  formData.append("op", op);

  fetch("/modificar_carrito/", {
    method: "POST",
    headers: {
      "X-CSRFToken": getCookie("csrftoken"), // Asegúrate de tener la función getCookie para obtener el valor del CSRF token
    },
    body: formData,
  })
    .then((response) => response.json())
    .then((data) => {
      console.log("Respuesta del servidor:", data);
      // Hacer algo con la respuesta del servidor si es necesario
    })
    .catch((error) =>
      console.error("Error al agregar el producto al carrito:", error)
    );
  location.reload();
}

function getCookie(name) {
  let cookieValue = null;
  if (document.cookie && document.cookie !== "") {
    const cookies = document.cookie.split(";");
    for (let i = 0; i < cookies.length; i++) {
      const cookie = cookies[i].trim();
      if (cookie.substring(0, name.length + 1) === name + "=") {
        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
        break;
      }
    }
  }
  return cookieValue;
}

$(".divisas").on("change", function () {
  var selectedOption = $(this).children("option:selected");
  divisa = selectedOption.text();
  valorDivisa = $(this).val();
  guardarDivisa();
  location.reload();
});

function guardarDivisa() {
  miLocalStorage.setItem("divisa", JSON.stringify(divisa));
  miLocalStorage.setItem("valorDivisa", JSON.stringify(valorDivisa));
}

function cargarDivisa() {
  if (miLocalStorage.getItem("divisa") !== null) {
    // Carga la información
    var divisa = JSON.parse(miLocalStorage.getItem("divisa"));
  } else {
    var divisa = "CLP";
  }
  if (miLocalStorage.getItem("valorDivisa") !== null) {
    // Carga la información
    var valorDivisa = JSON.parse(miLocalStorage.getItem("valorDivisa"));
  } else {
    var valorDivisa = 1;
  }
  return { divisa, valorDivisa };
}
