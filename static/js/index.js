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

function NewTaskCon() {
    const conToHide = document.querySelector('.new-todo-con-con');


    if (conToHide.classList.contains('hide-new-todo-con')) {
        conToHide.classList.remove('hide-new-todo-con');
        blockScreen('activate');
    } else {
        conToHide.classList.add('hide-new-todo-con');
        blockScreen('remove');
    };
};

function blockScreen(choice) {
    const screenBlocker = document.querySelector('.block-screen-beneath');
    const noScroll = document.querySelector('.body');
    
    if (choice === 'activate') {
        screenBlocker.classList.add('active'); // Blur Screen
        noScroll.classList.add('no-scroll'); // Stop Scroll
        
    } else if (choice === 'remove') {
        screenBlocker.classList.remove('active'); // Remove Screen Blur
        noScroll.classList.remove('no-scroll'); // RE-Activate Scrolling
    };
};