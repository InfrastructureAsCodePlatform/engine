class TerragruntLogs:
    def __init__(self, logs):
        self.logs = logs

    def get_outputs(self):
        lines = self.logs.splitlines()
        position = None
        for index, line in enumerate(lines):
            if line == "Outputs:":
                position = index + 2
                break

        result = {}

        if position is None:
            return result

        for line in lines[position:]:
            key, value = line.split(" = ")
            result[key] = value.replace('"', "")
        return result
