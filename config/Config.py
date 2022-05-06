class Config :
    def getPins(self, name):
        arrayLine = []
        pins = []
        found = False
        with open('/home/pi/Sunfounder/config/config.txt', "r") as tf:
            lines = tf.read().split('\n')
            
        for line in lines:
            if name == line :
                found = True

            if line == '':
                found = False

            if found :
                arrayLine.append(line)
            
        arrayLine.pop(0)

        for i in range(len(arrayLine)):
            pins.append(arrayLine[i].split(' = ')[1])

        return pins

        