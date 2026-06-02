// Așteaptă încărcarea completă a paginii
$(document).ready(function () {

    // Ascunde/afișează tabelul de taskuri
    $("#toggleTasks").click(function () {
        $("#tasksTable").fadeToggle();
    });

    // Confirmare înainte de ștergere
    $(".delete-link").click(function () {
        return confirm("Sigur vrei să ștergi acest task?");
    });

});