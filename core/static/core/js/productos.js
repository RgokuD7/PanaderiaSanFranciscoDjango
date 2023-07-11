var divisa = cargarDivisa().divisa;
var valorDivisa = cargarDivisa().valorDivisa;
$(document).ready(function () {
  renderProductos();
});
function renderProductos() {
  if (productos.length == 0) {
    $("#items").html("<h1 class='titulos'>No hay productos disponibles.</h1>");
  } else {
    $("#items").html("");
  }
  productos.forEach((producto) => {
    var precio = Math.round(valorDivisa * producto.precio * 100) / 100;
    var precio = precio.toLocaleString("es-CL");
    $("#items").append(
      `<div class="producto">
            <img src="${producto.img}" alt="${producto.nombre}">
            <h4 class="titulo_producto">${producto.nombre}</h4>
            <div class="agregar">
              <h5 class="preciodiv">${precio} ${divisa}</h5>
              <button class="btn-agregar fa-solid fa-cart-arrow-down" <button
                onclick="anyadirProductoAlCarrito(${producto.producto_id}, 'add')">Agregar</button>
              </button>
            </div>
          </div>`
    );
  });
}
