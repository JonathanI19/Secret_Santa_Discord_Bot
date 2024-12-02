class SSUser():
    
    def __init__(self, member):
        
        self._name = member.name  # Private attribute
        self._id = member.id # Private attribute
        self._ssid = "" # Private attribute
        self._ssname = "" # Private attribute
        # print(self._name + ', ' + str(self._id))

    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name
    
    def get_id(self):
        return self._id

    def get_ssid(self):
        return self._ssid

    def set_ssid(self, ssid):
        self._ssid = ssid

    def get_ssname(self):
        return self._ssname

    def set_ssname(self, ssname):
        self._ssname = ssname