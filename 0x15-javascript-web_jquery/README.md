## Javascript - Web jQuery
* [0-script.js](0-script.js) - Updates the text color of the `<header>` element to red `(#FF0000)` using `document.querySelector`

* [1-script.js](1-script.js) -  Updates the text color of the `<header>` element to red `(#FF0000)` using JQuery API

* [2-script.js](2-script.js) -  Updates the text color of the `<header>` element to red `(#FF0000)` when the user clicks the tag `DIV#red_header` using JQuery API

* [3-script.js](3-script.js) - Adds the class `red` to the `<header>` element when the user clicks the tag `DIV#red_header` using JQuery API

* [4-script.js](4-script.js) - toggles the class of the `<header>` element when the user clicks on the tag `DIV#toggle_header`
    - The `<header>` element always has one class: `red` or `green`, never both at the same time and never empty
    - The current class is `red`, when the user clicks on `DIV#toggle_header`, the class is updated to `green`; and the reverse
    - JQuery API is used

* [5-script.js](5-script.js) - adds a `<li>` element to a list when the user clicks on the tag `DIV#add_item`
    - The new element is `<li>Item</li>`
    - The new element is added to `UL.my_list`
    - JQuery API is used

* [6-script.js](6-script.js) - updates the text of the `<header>` element to `New Header!!!` when the user clicks on `DIV#update_header` using JQuery API

* [7-script.js](7-script.js) - fetches the character `name` from the [URL](https://swapi-api.hbtn.io/api/people/5/?format=json) and displays the name in the HTML tag `DIV#character` using JQuery API

* [8-script.js](8-script.js) - fetches and lists the `title` for all movies using the [URL](https://swapi-api.hbtn.io/api/films/?format=json) and lists the titles in the HTML tag `UL#list_movies` using JQuery API

* [9-script.js](9-script.js) - fetches from [here](https://fourtonfish.com/hellosalut/?lang=fr) and displayst he value of `hello` from the fetch in the HTML tag `DIV#hello`
    - The translation of 'hello' is displayed in the HTML tag `DIV#hello`
    - script works when it is imported from the `<head>` tag

* [100-script.js](100-script.js) - updates the text color of the `header` element to red and the script is imported from the `<head>` tag and not at the end of the HTML

* [101-script.js](101-script.js) - adds, removes ad clears `LI` elements from a list when the user clicks
    - The new element is `<li>Item</li>`
    - The new element is added to `UL.my_list`
    - When the user clicks on `DIV#add_item`: a new element is added to the list
    - When the user clicks on `DIV#remove_item`: the last element is removed from the list
    - When the user clicks on `DIV#clear_list`: all elements of the list are removed
    - The script works when imported from the `HEAD` tag

* [102-script.js](102-script.js) - fetches and prints how to say "Hello" depending on the language
    - Uses this [API service](https://www.fourtonfish.com/hellosalut/hello/)
    - language code is the value added in the tag `INPUT#language_code` eg `es`, `fr`, `en`
    - translation is fetched when the user clicks on `INPUT#btn_translate`
    - translation of "Hello" is displayed in the HTML tag `DIV#hello`
    - script works when imported from the `<head>` tag

* [103-script.js](103-script.js) - fetches and prints how to say "Hello" depending on the language
    - Uses this [API service](https://www.fourtonfish.com/hellosalut/hello/)
    - language code is the value added in the tag `INPUT#language_code` eg `es`, `fr`, `en`
    - translation is fetched when the user clicks on `INPUT#btn_translate` OR presses `ENTER` when the focus is on `INPUT#language_code`
    - translation of "Hello" is displayed in the HTML tag `DIV#hello`
    - script works when imported from the `<head>` tag