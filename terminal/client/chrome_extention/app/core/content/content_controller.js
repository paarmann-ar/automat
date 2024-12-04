var target = null
var all_elements_pattern = []
var clicked_elements_pattern = []
var list_elements_pattern = []

var elements_object = {}

let vars = {
    all_elements_pattern,
    clicked_elements_pattern,
    list_elements_pattern
}

// --
// ... event listeners
// --

window.addEventListener('DOMContentLoaded', after_load_dom_event)
window.addEventListener('mousedown', mous_down_event, false)

// --
// ... message manager
// --

let received_message = (message, sender, sendResponse) => {
    if (message.contain === "Add me to your list") {
        list_elements_pattern.push(content_parser_controller(target))
    }

    config.package_contain.forEach((item) => {
        elements_object[item] = vars[item]
    })

    if (message.contain === "Give me your elements") {
        chrome.runtime.sendMessage(elements_object, () => { })
    }

    elements_object = {}
    clicked_elements_pattern.length=0
    all_elements_pattern.length=0
    list_elements_pattern.length=0
    
}

chrome.runtime.onMessage.addListener(received_message);

// --
// ... events
// --

function after_load_dom_event() {
    querySelectorAll = document.querySelectorAll('*')
    querySelectorAll.forEach(element => {
        target_element = content_parser_controller(element)
        if (target_element.length > 0) {
            all_elements_pattern.push(target_element)
        }
    })

}

function mous_down_event(ev) {
    target = ev.target
    clicked_elements_pattern.push(content_parser_controller(target))
    console.log("clicked_elements_pattern", clicked_elements_pattern)
}