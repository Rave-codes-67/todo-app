

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

// CLOSING AND OPENING OF CONTAINERS
// --- OPENING
function openCon(conToOpen) {
    const closableCon = document.querySelectorAll('.closableCon')
    
    closableCon.forEach((con) => {
        if (con.classList.contains(conToOpen)) {
            con.classList.remove('hide-con');
            blockScreen('activate');
            return
        }
    });
};

// --- CLOSING
function closeCon(conToClose) {
    container = document.querySelector('.' + conToClose)
    
    container.classList.add('hide-con');
    blockScreen('disable');
    return
};

// --- CLOSING WITH 'ESC' KEY
const closableCon = document.querySelectorAll('.closableCon');

document.addEventListener('keydown', (event) => {
    if (event.key === 'Escape') {
        closableCon.forEach((con) => {
            if (!con.classList.contains('hide-con')) {
                con.classList.add('hide-con')
                blockScreen('disable')
            }
        });
    };
});

function blockScreen(option) {
    const screenBlocker = document.querySelector('.block-screen-beneath');
    const noScroll = document.querySelector('.body');
    
    if (option === 'activate') {
        screenBlocker.classList.add('active'); // Blur Screen
        noScroll.classList.add('no-scroll'); // Stop Scroll
        
    } else if (option === 'disable') {
        screenBlocker.classList.remove('active'); // Remove Screen Blur
        noScroll.classList.remove('no-scroll'); // RE-Activate Scrolling
    };
};