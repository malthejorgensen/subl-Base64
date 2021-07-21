import base64

import sublime_plugin


def subl_convert_case(view, edit, region, content, converter_func):
    new_content = converter_func(content).decode()

    view.replace(edit, region, new_content)


def base64_encode(self, content):
    return base64.b64encode(content.encode('utf-8'))


def base64_decode(self, content):
    return base64.b64decode(content.encode('utf-8'))


class BaseCommand:
    def run(self, edit):
        if self.view.sel()[0].empty() and len(self.view.sel()) == 1:
            # No selection
            return

        for region in self.view.sel():
            if region.empty():
                # Empty region
                continue
            else:
                subl_convert_case(
                    self.view,
                    edit,
                    region,
                    self.view.substr(region),
                    self.converter_func,
                )


class Base64Encode(BaseCommand, sublime_plugin.TextCommand):
    converter_func = base64_encode


class Base64Decode(BaseCommand, sublime_plugin.TextCommand):
    converter_func = base64_decode
