// Obtain all draggable elements and the containers which house them
const units = document.querySelectorAll('.unit');
const containers = document.querySelectorAll('.container');

// Attach event listeners for every unit div which will make it transparent when it is being dragged
units.forEach(unit => {
    unit.addEventListener('dragstart', () => {
        unit.classList.add("dragging");
    });
    unit.addEventListener("dragend", () => {
        unit.classList.remove("dragging");
    });
});

containers.forEach(container => {
    container.addEventListener("dragover", e => {                               // Prevents the "blocked" cursor from showing
        e.preventDefault();
        const afterElement = getDragAfterElement(container, e.clientX);         // Calls the getDragAfterElement function that returns the closest horizontal element to the cursor
        const draggable = document.querySelector('.dragging');                  // Variable that contains the element that the user is dragging
        if (container.childElementCount < 4) {                                  // Sets max amount of units in a semester
            if (container.parentElement.classList[0] == draggable.classList[1] || container.parentElement.classList[0] == draggable.classList[2]) {         //Checks if the unit is allowed in that year
                if (container.parentElement.classList[1] == draggable.classList[3] || container.parentElement.classList[1] == draggable.classList[4]) {     //Checks if the unit is allowed in that semester
                    if(draggable.innerHTML in prereqs){                         // Checks if the unit being dragged has prerequisites; If not, then just drop it in
                        let nameslist = [];
                        let names = document.querySelectorAll('.main');         // The for loops will parse through and generate an array of all units currently dropped in main containers
                        for(let i = 0; i < names.length; i++){
                            for(let j = 0; j< names[i].children.length; j++){
                                nameslist.push(names[i].children.item(j).innerHTML);
                            }
                        }
                        if (nameslist.includes(prereqs[draggable.innerHTML])){  // Checks if the prerequisite of the unit has already been dropped in or not previously
                            if (afterElement == null) { 
                                container.appendChild(draggable);               // Drops it in the last position of the container (No closest unit to the right)
                                nameslist = [];
                            } else {
                                container.insertBefore(draggable, afterElement);// Drops it before the closest unit to the right
                                nameslist = [];
                            }
                        }
                    } else{
                        if (afterElement == null) { 
                            container.appendChild(draggable);
                        } else {
                            container.insertBefore(draggable, afterElement);
                        }
                    }
                }
            }
        }
    });
});

function getDragAfterElement(container, x) {                                            // Function that takes the current container that is being dragged over, and the x coordinates of the cursor
    const draggableElements = [...container.querySelectorAll(".unit:not(.dragging)")];  // Obtains all elements that are already in the container

    return draggableElements.reduce((closest, child) => {                               
    const box = child.getBoundingClientRect();                                               
        const offset = x - box.left - box.width / 2;                                     // Computes the distance between the middle of the box and the x of the cursor
        if (offset <0 && offset > closest.offset) {
            return { offset: offset, element: child};                                    //Returns the offset to the closest element, and that element
        } else {
            return closest;                                                              //returns null
        }
    }, {offset: Number.NEGATIVE_INFINITY}).element;                                      // Sets an arbitrary base amount for offset
}

