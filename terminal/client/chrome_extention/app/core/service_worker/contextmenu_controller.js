import { extention_status } from './service_worker_controller.js'
import { dispatch_messages_controller } from './dispatch_messages.js'

// --
// ... controller
// --

export function contextmenu_controller(info, tab) {
    if (!extention_status.is_contextmenu_created) {
        create_contextmenu()
        extention_status.is_contextmenu_created = true
    }

    dispatch_messages_controller(tab, 'Add me to your list')

    get_element_that_has_been_clicked(info)
}

// --
// ... create contextmenu
// --

function create_contextmenu() {
    chrome.contextMenus.create(
        {
            "id": "RDC_chrome_elements_detector",
            "title": "Add me to your list",
            "contexts": ["all"]
        }
    )
}

// --
// ... get element after click
// --

function get_element_that_has_been_clicked(info) {
}