import { fetch_api } from '../fetch_api/fetch_api.js'
import { contextmenu_controller } from './contextmenu_controller.js'
import { dispatch_messages_controller } from './dispatch_messages.js'

// --
// ... extention status data structur
// --

export var extention_status = {
  resived_message: {},
  current_tab: null,
  is_contextmenu_created: false
}

// --
// ... initial
// --

console.clear()
console.log("service_background_wortker is start at ", Date().toLocaleString())

contextmenu_controller()

// --
// ... add listeners
// --

chrome.action.onClicked.addListener(() => {
  chrome.tabs.query({},
    function (tabs) {

      tabs.forEach((tab)=>{
        dispatch_messages_controller(tab, 'Give me your elements')
        extention_status.current_tab = tab
      })
      extention_status.current_tab = tab
    }
  )
})


chrome.contextMenus.onClicked.addListener((info, tab) => {
  contextmenu_controller(info, tab)
  extention_status.current_tab = tab

})

chrome.runtime.onMessage.addListener((message, sender, sendResponse) => {
  message['URL']=extention_status.current_tab.url
  message['Title']=extention_status.current_tab.title

  extention_status.resived_message = message
  console.log(extention_status.resived_message)

  fetch_api({ method: "POST", attach_json: extention_status.resived_message })

  extention_status.resived_message={}
})

