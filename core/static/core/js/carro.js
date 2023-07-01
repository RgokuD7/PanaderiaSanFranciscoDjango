function anyadirProductoAlCarrito(usuario_rut, producto_id, cantidad) {
    // Realiza una solicitud HTTP POST al servidor utilizando Ajax
    fetch('/agregar_al_carrito/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': '{{ csrf_token }}'  // Asegúrate de incluir el token CSRF en la solicitud
        },
        body: JSON.stringify({
            usuario_rut: usuario_rut,
            producto_id: producto_id,
            cantidad: cantidad
        })
    })
    .then(response => response.json())
    .then(data => {
        console.log(data.mensaje);
        // Realiza las acciones necesarias después de agregar el producto al carrito
    })
    .catch(error => {
        console.error('Error:', error);
        // Maneja el error si la solicitud falla
    });
}