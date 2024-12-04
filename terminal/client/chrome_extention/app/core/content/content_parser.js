function content_parser_controller(element) {
    return parse_dom(element)
}

// --
// ... logic methods
// --

function parse_dom(element) {
    let elment_patterns_count = []
    let elements_with_unique_pattern = []

    Array.from(element.attributes).forEach(attribute => {
        if (attribute) {
            elment_patterns_count.push({
                tagName: element.tagName.toLowerCase(),
                attribute_name: attribute.name,
                xpath: get_pattern_to_identify(element, attribute),
                count_of_findet_element: find_pattern_in_dom(pattern),
                xpath_: get_pattern_with_contains_to_identify(element, attribute),
            })
        }
    });

    elment_patterns_count.forEach(element => {
        if (element.length != 0) {
            if (element.count_of_findet_element == 1) {
                elements_with_unique_pattern.push({
                    xpath: element.xpath,
                    xpath_: element.xpath_,
                })
            }
        }
    })

    return elements_with_unique_pattern
}


function get_pattern_to_identify(element, attribute) {
    tagName = element.tagName.toLowerCase()
    pattern = `//${tagName}[@${attribute.name}="${attribute.value}"]`
    return pattern
}

function get_pattern_with_contains_to_identify(element, attribute) {
    tagName = element.tagName.toLowerCase()

    attribute_value = attribute.value
    if (attribute_value === "") {
        return ""
    }
    if (attribute_value.match(/\d/) === null) {
        return ""
    }
    if (!attribute_value.includes('_')) {
        return ""
    }

    selected_word = []
    words = attribute_value.split('_')
    words.forEach((word) => {
        if (word.match(/\d/) === null) {
            selected_word.push(word)
        }
    })

    container = ""
    selected_word.forEach(word => {
        container = `contains(@${attribute.name},"${word}") and ${container}`
    });

    pattern_ = `//${tagName}[${container} 1]`

    try { count_pattern_ = find_pattern_in_dom(pattern_) }
    catch (err) { count_pattern_ = 100 }

    if (count_pattern_ == 1) { return pattern_ } else { return "" }
}


function find_pattern_in_dom(pattern) {
    return document.evaluate(`count(${pattern})`, document, null, XPathResult.ANY_TYPE, null).numberValue
}