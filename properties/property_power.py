class Cricket:
    # """
    # this is a class about cricket modes
    # """
    _modes = {"TEST", "ODI", "T20"}

    def __init__(self, mode):
        self.set_mode(mode)

    def get_mode(self):
        """
        getting cricket mode
        """
        return self._mode

    def set_mode(self, mode):
        """
        setting cricket mode
        """
        if mode in self._modes:
            self._mode = mode
        else:
            raise ValueError("")

    def del_mode(self):
        """
        deleting cricket mode
        """
        del self._mode

    mode = property(fget=get_mode, fset=set_mode, fdel=del_mode)


t20 = Cricket("T20")
print(t20.__dict__)
t20.__dict__["mode"] = "ODI"
print(t20.__dict__)
# even though we have mode attr same as property attr, the property attr got invoked
t20.mode = "TEST"
print(t20.__dict__)
del t20.mode
print(t20.__dict__)
print("mode" in Cricket.__dict__, "mode" in t20.__dict__)
# the docstring of property always fetches from the getter function and if we provide doc value in property instance..then that will get prioritized.
# print(Cricket.mode.fget.__doc__)
# print(Cricket.mode.fset.__doc__)
# print(Cricket.mode.fdel.__doc__)
