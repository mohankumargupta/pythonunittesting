import os
import importlib
#from tests.BlackjackTest import *
alltests = [name for name in os.listdir("tests") if name.endswith(".py")]
alltests = [(name[:-3], "tests.{}".format(name[:-3])) for name in alltests if not name == "__init__.py"]
for i in alltests:
	test = importlib.import_module(i[1])
	globals().update({i[0]:getattr(test, i[0])})

