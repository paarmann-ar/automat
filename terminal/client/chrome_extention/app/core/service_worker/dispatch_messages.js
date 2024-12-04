// --
// ... send message to forground controller
// --

export function dispatch_messages_controller(tab = null, contain = null) {


    let tab_id = tab?.id
    let msg = contain

    let message_to_dispatch = {
        tab_id: tab_id,
        contain: msg
    }

    if (message_to_dispatch.tab_id) {
        send_message(tab_id, message_to_dispatch)
    }
}

// --
// ... send message to forground
// --

function send_message(tab_id, message) {
    chrome.tabs.sendMessage(tab_id, message, () => { console.log("Message sended") })
}