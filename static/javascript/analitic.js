document.getElementById("sumForm").addEventListener("submit", function (event) {
    event.preventDefault(); // Evitar que se recargue la página

    var num1 = parseFloat(document.getElementById("num1").value);
    var num2 = parseFloat(document.getElementById("num2").value);

    // Enviar los datos al servidor usando AJAX
    fetch("/calcular-suma", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ num1: num1, num2: num2 })
    })
    .then(response => response.json())
    .then(data => {
        // Mostrar el resultado en la página
        document.getElementById("result").textContent = data.result;
    });
});
