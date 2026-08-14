// Sync / Refresh Button Animation
function refreshData() {
    const icon = document.getElementById('refresh-icon');
    if (!icon) return;

    icon.classList.add('animate-spin');
    setTimeout(() => {
        icon.classList.remove('animate-spin');
    }, 800);
}

// Combined Framework Dropdown & Live Search Filter
function filterTable() {
    const searchInput = document.getElementById('logSearch');
    const dropdownFilter = document.getElementById('frameworkFilter');
    const table = document.getElementById('auditTable');
    
    if (!table) return;

    const searchText = searchInput ? searchInput.value.toLowerCase() : '';
    const selectedFramework = dropdownFilter ? dropdownFilter.value.toLowerCase() : '';
    const rows = table.getElementsByTagName('tr');

    for (let i = 1; i < rows.length; i++) {
        const ruleCell = rows[i].getElementsByTagName('td')[1]; // Rule / Vector column
        if (ruleCell) {
            const textValue = (ruleCell.textContent || ruleCell.innerText).toLowerCase();
            
            const matchesSearch = textValue.indexOf(searchText) > -1;
            const matchesFramework = selectedFramework === '' || textValue.indexOf(selectedFramework) > -1;

            if (matchesSearch && matchesFramework) {
                rows[i].style.display = "";
            } else {
                rows[i].style.display = "none";
            }
        }
    }
}

// Sidebar Navigation Tab Switching
document.addEventListener('DOMContentLoaded', () => {
    const sidebarLinks = document.querySelectorAll('aside a, .sidebar-nav-item, nav a');
    
    sidebarLinks.forEach(link => {
        link.addEventListener('click', function(e) {
            sidebarLinks.forEach(l => l.classList.remove('bg-gray-800', 'text-white'));
            this.classList.add('bg-gray-800', 'text-white');
        });
    });
});
