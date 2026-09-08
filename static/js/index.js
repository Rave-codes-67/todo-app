// const rowIdentifyer = document.querySelector('.checker');
// const rowIndex = Number(rowIdentifyer.id);

// if (rowIndex % 2 === 0) {
//     rowIndex.classList.add('row-checker-dark');
// } 


// In-line td status changer
function inlineChangeStatus(task) {
    const taskID = task.id
    const taskStatus = task.className

    fetch('/update-status', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ id: taskID, status: taskStatus })
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            task.innerHTML = data.new_status;

            task.className = data.new_status;
        } else {
            alert("STATUS CHANGE FAILED");
        }
    })
}
