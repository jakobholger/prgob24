class TV:
    def __init__(self, tv_name, max_channel, current_channel, max_volume, current_volume):
        self.tv_name = tv_name
        self.current_volume = current_volume
        self.current_channel = current_channel
        self.max_volume = max_volume
        self.max_channel = max_channel
        
    def change_channel(self, new_channel):
        if new_channel<1 or new_channel>self.max_channel:
            return False
        self.current_channel = new_channel
        return True

    def increase_volume(self):
        if self.current_volume == self.max_volume:
            return False
        self.current_volume+=1
        return True
    
    def decrease_volume(self):
        if self.current_channel == 0:
            return False
        self.current_volume-=1
        return True
    
    def __str__(self):
        return self.tv_name + "\nKanal: " + str(self.current_channel) + "\nLjudvolym: " + str(self.current_volume) + "\n"
    
    def str_for_file(self):
        return str(self.tv_name) + "," + str(self.max_channel) + "," + str(self.current_channel) + "," + str(self.max_volume) + "," + str(self.current_volume)
