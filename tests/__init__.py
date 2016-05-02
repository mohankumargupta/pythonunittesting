import os

__all__ = [name for name in os.listdir(os.path.dirname(os.path.realpath(__file__))) if name.endswith(".py")]
__all__ = [name[:-3] for name in __all__ if not name == "__init__.py"]
#print(__all__)



