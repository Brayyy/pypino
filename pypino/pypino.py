
from time import time
from socket import gethostname
from os import getpid
from json import dumps


class PyPino:
    __opts = None
    __level_threshold = 30
    __base = {}
    __level_map = {
        "trace": 10,
        "debug": 20,
        "info": 30,
        "warn": 40,
        "error": 50,
        "fatal": 60,
    }

    # def __init__(self, opts={}):
    def __init__(self, name=None, level=30, base=None, showVersion=None):
        if level is not None:
            self.level(level)
        base = {
            "hostname": gethostname(),
            "pid": getpid(),
        }
        if base is not None:
            self.__base = base
        if name is not None:
            self.__base["name"] = name
        if showVersion is not None:
            self.__base["v"] = showVersion

        # if "level" in opts:
        #     self.level(opts["level"])
        # base = {
        #     "hostname": gethostname(),
        #     "pid": getpid(),
        # }
        # if "base" in opts:
        #     base = opts["base"]
        # if "name" in opts:
        #     base["name"] = opts["name"]
        # if "showVersion" in opts:
        #     base["v"] = opts["showVersion"]
        # self.__base = base

    def __output(self, level, *args):
        args = list(args)
        if level < self.__level_threshold:
            return
        out = self.__base.copy()
        out["level"] = level
        out["time"] = int(1000 * time())
        for key in self.__base:
            if key not in out:
                out[key] = self.__base[key]

        if len(args) > 0:
            # If first is a dict, pop it from the list and add each k/v to out
            if isinstance(args[0], dict):
                obj_dict = args.pop(0)
                for arg in obj_dict:
                    out[arg] = obj_dict[arg]
            if len(args) > 0:
                msg = args[0]
                if isinstance(msg, int):
                    out["msg"] = msg
                elif isinstance(msg, str):
                    if len(args) == 1:
                        out["msg"] = msg
                    else:
                        # Handle string formatting
                        out["msg"] = msg % tuple(args[1:])
                elif isinstance(msg, BaseException):
                    out["msg"] = str(msg)
                elif msg is None:
                    out["msg"] = None

        print(dumps(out, separators=(",", ":")))

    def trace(self, *args): self.__output(10, *args)

    def debug(self, *args): self.__output(20, *args)

    def info(self, *args): self.__output(30, *args)

    def warn(self, *args): self.__output(40, *args)

    def error(self, *args): self.__output(50, *args)

    def fatal(self, *args): self.__output(60, *args)

    def level(self, new_level=None):
        if new_level is not None:
            if isinstance(new_level, int):
                self.__level_threshold = new_level
            if isinstance(new_level, str) and new_level in self.__level_map:
                self.__level_threshold = self.__level_map[new_level]
        return self.__level_threshold
