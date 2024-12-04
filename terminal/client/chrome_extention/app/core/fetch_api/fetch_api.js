import { config } from '../../config/config.js'

export function fetch_api(fetch_package = { url: null, method: null, attach_json: null }) {
    if (fetch_package?.url == null) {
        fetch_package.url = config.api_host
    }
    if (fetch_package?.method == null) {
        fetch_package.method = "GET"
    }

    if (fetch_package.method === 'GET') {
        fetch(fetch_package.url,)
            .then(res => {
                if (res.ok) {
                    console.log(res)
                    res.json()
                        .then(data => {
                            console.log(data)
                        })
                }
            })
            .catch(error => {
                console.log(error)
            })
    } else if (fetch_package.method === 'POST') {
        fetch(fetch_package.url, {
            method: 'POST',
            headers: {
                'Content-type': 'application/data',
                'accept': 'application/json',
                'User-agent': 'learning app',
            },
            body: JSON.stringify(fetch_package.attach_json)
        })
            .then(res => {
                return res.json()
            })
            .then(data => {
                console.log(data)
            })
            .catch(error => { console.log(error) })
    }
}