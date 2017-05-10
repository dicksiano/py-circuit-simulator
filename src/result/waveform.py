#CONSTANTS

PORT_WIDTH = 100
LINE_WIDTH = 3
PORT_COLOR = (255,0,0)
WAVEFORM_COLOR = (50,50,170)

class Waveform:
    def __init__(self, result=[], gate_list=[]):
        self.is_result = False
        self.result = result
        self.gate_list = gate_list

    def render(self, screen):
        if len(self.result) != 0 and len(self.result[0]) != 0:
            step_width = 700/len(self.result)
            step_height = min(50, 545/len(self.result[0]))
            height_high = 0.8*step_height
            height_low = 0.1*step_height
            pin_counter = 1
            for gate in self.gate_list:
                if gate["type"] == 'in':
                    screen.fill_rect(PORT_COLOR, (0, step_height * pin_counter + 5, PORT_WIDTH, step_height))
                    screen.draw_text_centered(gate["id"], (0, 0, 0), (0, step_height * pin_counter + 5, PORT_WIDTH, step_height))
                    pin_counter += 1

                    actual_x = 0
                    for line in self.result:
                        for keys in line.keys():
                            if keys == gate["id"]:
                                if line[keys] == '0':
                                    screen.fill_rect(WAVEFORM_COLOR, (PORT_WIDTH + actual_x * step_width, step_height * pin_counter + 5 - height_low, step_width, height_low))
                                elif line[keys] == '1':
                                    screen.fill_rect(WAVEFORM_COLOR, (PORT_WIDTH + actual_x * step_width, step_height * pin_counter + 5 - height_high, step_width, height_high))
                        actual_x += 1

            for gate in self.gate_list:
                if gate["type"] == 'out':
                    screen.fill_rect(PORT_COLOR, (0, step_height * pin_counter + 5, PORT_WIDTH, step_height))
                    screen.draw_text_centered(gate["id"], (0, 0, 0),
                                              (0, step_height * pin_counter + 5, PORT_WIDTH, step_height))
                    pin_counter += 1

                    actual_x = 0
                    for line in self.result:
                        for keys in line.keys():
                            if keys == gate["id"]:
                                if line[keys] == '0':
                                    screen.fill_rect(WAVEFORM_COLOR, (PORT_WIDTH + actual_x * step_width, step_height * pin_counter + 5 - height_low, step_width, height_low))
                                elif line[keys] == '1':
                                    screen.fill_rect(WAVEFORM_COLOR, (PORT_WIDTH + actual_x * step_width, step_height * pin_counter + 5 - height_high, step_width, height_high))
                        actual_x += 1


