import httplib2


def scrub_orig_urls(orig_urls):
    active_urls = []

    for url in orig_urls:
        url.print_url_string()
        if is_url_still_active(url.get_url_string()):
            print("active")
        else:
            print("!!!!not active!!!!")


def is_url_still_active(orig_url_string):
    h = httplib2.Http()
    response = h.request("http://google.com", "HEAD")
    if int(response[0]['status']) < 400:
        return 1
    else:
        return 0
