document.addEventListener("DOMContentLoaded", function () {
    var toastElement = document.getElementById("liveToast");
    if (toastElement) {  // Exibe o toast apenas se houver mensagens
      var toast = new bootstrap.Toast(toastElement, {
        delay: 3000  // Tempo de exibição do toast (3 segundos)
      });
      toast.show();
    }
  });