from g4f import set_cookies

set_cookies(".bing.com", {
    "_U": "cookie value"
})

from g4f.gui import run_gui

run_gui("0.0.0.0", 8080, debug=True)
