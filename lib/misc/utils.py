class Config():
    @staticmethod
    def load_config(filename):
        with open(filename) as fd:
            config = fd.readlines()
        config_ = {}
        for line in config:
            if line.startswith("#"):
                continue
            if len(line.strip()) == 0:
                continue
            config_[line.split("=")[0].strip()] = line.split("=")[1].strip()
        return config_