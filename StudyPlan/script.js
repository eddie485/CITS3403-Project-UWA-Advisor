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
        if (afterElement == null) {
            container.appendChild(draggable)
        } else {
            container.insertBefore(draggable, afterElement)
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

