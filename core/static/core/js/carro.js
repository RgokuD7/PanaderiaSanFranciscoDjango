var divisa = cargarDivisa().divisa;
var valorDivisa = cargarDivisa().valorDivisa;

$(document).ready(function () {
  anyadirProductoAlCarrito(0, "render");
});
function anyadirProductoAlCarrito(idProducto, opcion) {
  $.ajax({
    url: "/modificar_carrito/",
    data: { id_producto: idProducto, op: opcion },
    success: function (carrito) {
      var total = 0;
      if (carrito.length == 0) {
        $("#carrito").html("<h3 class='titulos'>El carrito está vacío.</h3>");
      } else {
        $("#carrito").html("");
      }
      carrito.forEach((producto) => {
        var precio = Math.round(valorDivisa * producto.precio * 100) / 100;
        precio = precio.toLocaleString("es-CL");
        total = total + producto.precio;
        $("#carrito").append(
          `<li class="item-carrito">
                <p>${producto.nombre} <span class="precio">${precio} ${divisa}</span></span></p>     
                <div class="cantidad">
                  <button class="btn-agregar fa-solid fa-plus" onclick="anyadirProductoAlCarrito(${producto.id_producto}, 'add')"></button>
                  <p>${producto.cantidad}</p>
                  <button class="btn-eliminar fa-solid fa-minus" onclick="anyadirProductoAlCarrito(${producto.id_producto}, 'del1')"></button>
                  <button class="btn-eliminar fa-solid fa-trash" onclick="anyadirProductoAlCarrito(${producto.id_producto}, 'del')"></button>
                </div>
              </li>`
        );
      });
      total = Math.round(valorDivisa * total * 100) / 100;
      total = total.toLocaleString("es-CL");
      $('#total').html(
        `Total: ${total} ${divisa}`
      )
    },
  });
}