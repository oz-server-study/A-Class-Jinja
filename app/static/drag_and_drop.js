function allowDrop(ev) {
    ev.preventDefault();
}

function drag(ev) {
    ev.dataTransfer.setData("text", ev.target.rowIndex);
    ev.target.classList.add("dragging");
}

function drop(ev) {
    ev.preventDefault();
    var data = ev.dataTransfer.getData("text");
    var sourceRow = document.getElementById("todo-table").rows[data];
    var targetRow = ev.target.closest("tr");
    if (targetRow && sourceRow !== targetRow) {
        var targetIndex = targetRow.rowIndex;
        if (data < targetIndex) {
            targetRow.parentNode.insertBefore(sourceRow, targetRow.nextSibling);
        } else {
            targetRow.parentNode.insertBefore(sourceRow, targetRow);
        }
        updateOrder();
    }
    sourceRow.classList.remove("dragging");
}

function updateOrder() {
    var table = document.getElementById("todo-table");
    for (var i = 1, row; row = table.rows[i]; i++) {
        row.cells[1].innerText = i;  // Update order number
    }
}