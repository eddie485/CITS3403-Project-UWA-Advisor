
//Obtain all draggable elements and the containers which house them
const units = document.querySelectorAll('.unit')
const containers = document.querySelectorAll('.container')

units.forEach(unit => {
    unit.addEventListener('dragstart', () => {
        unit.classList.add("dragging")
    })
    unit.addEventListener("dragend", () => {
        unit.classList.remove("dragging")
    })
})

containers.forEach(container => {
    container.addEventListener("dragover", e => {
        e.preventDefault()
        const afterElement = getDragAfterElement(container, e.clientX)
        const draggable = document.querySelector('.dragging')
        if (container.childElementCount < 4) {
            if (container.parentElement.classList[0] == draggable.classList[1] || container.parentElement.classList[0] == draggable.classList[2]) {
                if (container.parentElement.classList[1] == draggable.classList[3] || container.parentElement.classList[1] == draggable.classList[4]) {
                    if(draggable.innerHTML in prereqs){
                        const nameslist = []
                        let names = document.querySelectorAll('.main')
                        for(let i = 0; i < names.length; i++){
                            for(let j = 0; j< names[i].children.length; j++){
                                nameslist.push(names[i].children.item(j).innerHTML)
                            }
                        }
                        if (nameslist.includes(prereqs[draggable.innerHTML])){
                            if (afterElement == null) { 
                                container.appendChild(draggable)
                                nameslist = []
                            } else {
                                container.insertBefore(draggable, afterElement)
                                nameslist = []
                            }
                        }
                    } else{
                        if (afterElement == null) { 
                            container.appendChild(draggable)
                        } else {
                            container.insertBefore(draggable, afterElement)
                        }
                    }
                }
            }
        }
    })
})

function getDragAfterElement(container, x) {
    const draggableElements = [...container.querySelectorAll(".unit:not(.dragging)")]

    return draggableElements.reduce((closest, child) => {
        const box = child.getBoundingClientRect()
        const offset = x - box.left - box.width / 2
        if (offset <0 && offset > closest.offset) {
            return { offset: offset, element: child}
        } else {
            return closest
        }
    }, {offset: Number.NEGATIVE_INFINITY}).element
}

