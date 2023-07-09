function updateComunas() {
  $('#selectRegion').prop("disabled", true);
  var regionId = $("#id_region").val();
  $.ajax({
    url: "/obtener_comunas/",
    data: { region_id: regionId },
    success: function (data) {
      $("#id_comuna").html("");
      data.forEach(function (comuna) {
        $("#id_comuna").append(
          `<option value="${comuna.id_comuna}">${comuna.comuna}</option>`
        );
      });
    },
  });
}
