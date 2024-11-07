document.addEventListener("DOMContentLoaded", function () {
    var toastElement = document.getElementById("liveToast");
    if (toastElement) {  // Exibe o toast apenas se houver mensagens
      var toast = new bootstrap.Toast(toastElement, {
        delay: 6000  // Tempo de exibição do toast (6 segundos) 
      });
      toast.show();
    }
  });