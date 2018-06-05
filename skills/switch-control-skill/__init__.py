from adapt.intent import IntentBuilder
from mycroft import MycroftSkill, intent_file_handler


class SwitchControl(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('control.switch.intent')
    def handle_control_switch(self, message):
        self.speak("Before speaking, writing. Control switch will be printed after speak dialog")
        self.speak_dialog('control.switch')
        self.speak("Controlling Switch!!!!!!!!!!!!!!!!!!!!!!!!")


def create_skill():
    return SwitchControl()
