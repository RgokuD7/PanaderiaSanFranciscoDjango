var miLocalStorage = window.localStorage;
var divisa = cargarDivisa().divisa;
var valorDivisa = cargarDivisa().valorDivisa;
$(document).ready(function () {
  $.get(
    "https://api.apilayer.com/exchangerates_data/latest?&base=clp&apikey=ZdkhQ3Q9PVN5OR8yPF55kZKHWhCcpPHp",
    function (data) {
      $.each(data.rates, function (i, item) {
        if (i == divisa) {
          $(".divisas").append(
            '<option value="' + item + '"selected>' + i + "</option>"
          );
        } else {
          $(".divisas").append(
            '<option value="' + item + '">' + i + "</option>"
          );
        }
      });
    }
  );
});
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

function guardarDivisa(divisa, valorDivisa) {
  miLocalStorage.setItem("divisa", JSON.stringify(divisa));
  miLocalStorage.setItem("valorDivisa", JSON.stringify(valorDivisa));
}

$(".divisas").on("change", function () {
  var selectedOption = $(this).children("option:selected");
  divisa = selectedOption.text();
  valorDivisa = $(this).val();
  guardarDivisa(divisa, valorDivisa);
  anyadirProductoAlCarrito(0, 'render');
});

function renderDivisa() {
  $(".preciodiv").each(function () {
    var precioTexto = $(this).text();
    var precioEntero = parseFloat(precioTexto.split(" ")[0]);
    console.log(precioTexto.split(" ")[0], precioEntero);
    var precio = Math.round(valorDivisa * precioEntero * 100) / 100;
    var precioFinal = precio.toLocaleString("en-IN");
    $(this).html(precioFinal + " " + divisa);
  });
}