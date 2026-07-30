function refreshData() {
    const icon = document.getElementById('refresh-icon');
    if (!icon) return;
    
    icon.classList.add('animate-spin');
    setTimeout(() => {
        icon.classList.remove('animate-spin');
    }, 800);
}

function filterTable() {
    const input = document.getElementById('logSearch');
    const table = document.getElementById('auditTable');
    if (!input || !table) return;

    const filter = input.value.toLowerCase();
    const rows = table.getElementsByTagName('tr');

    for (let i = 1; i < rows.length; i++) {
        const cell = rows[i].getElementsByTagName('td')[1];
        if (cell) {
            const textValue = cell.textContent || cell.innerText;
            rows[i].style.display = textValue.toLowerCase().indexOf(filter) > -1 ? "" : "none";
        }
    }
}
