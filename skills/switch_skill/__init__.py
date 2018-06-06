# TODO: Add an appropriate license to your skill before publishing.  See
# the LICENSE file for more information.

# Below is the list of outside modules you'll be using in your skill.
# They might be built-in to Python, from mycroft-core or from external
# libraries.  If you use an external library, be sure to include it
# in the requirements.txt file so the library is installed properly
# when the skill gets installed later by a user.

from adapt.intent import IntentBuilder
from mycroft.skills.core import MycroftSkill, intent_handler
from mycroft.util.log import LOG

#os module for shell commands in python
import os

# Each skill is contained within its own class, which inherits base methods
# from the MycroftSkill class.  You extend this class as shown below.

# TODO: Change "Template" to a unique name for your skill
class TemplateSkill(MycroftSkill):

    # The constructor of the skill, which calls MycroftSkill's constructor
    def __init__(self):
        super(TemplateSkill, self).__init__(name="TemplateSkill")

        # Initialize working variables used within the skill.
        self.count = 0

    # The "handle_xxxx_intent" function is triggered by Mycroft when the
    # skill's intent is matched.  The intent is defined by the IntentBuilder()
    # pieces, and is triggered when the user's utterance matches the pattern
    # defined by the keywords.  In this case, the match occurs when one word
    # is found from each of the files:
    #    vocab/en-us/Hello.voc
    #    vocab/en-us/World.voc
    # In this example that means it would match on utterances like:
    #   'Hello world'
    #   'Howdy you great big world'
    #   'Greetings planet earth'
    
    # @intent_handler(IntentBuilder("").require("Hello").require("World"))
    # def handle_hello_world_intent(self, message):
    #     # In this case, respond by simply speaking a canned response.
    #     # Mycroft will randomly speak one of the lines from the file
    #     #    dialogs/en-us/hello.world.dialog
    #     #self.speak_dialog("hello.world")
    #     dir = os.popen("ls").readlines()
    #     #ls_str = ''.join(dir)
    #     self.speak("yogesh")
    #     self.speak("the files in current folder are :")
    #     #self.speak(ls_str.split(" "))
    #     for ls_file in dir:
    #         self.speak(ls_file)

    # @intent_handler(IntentBuilder("").require("Count").require("Dir"))
    # def handle_count_intent(self, message):
    #     if message.data["Dir"] == "up":
    #         self.count += 1
    #     else:  # assume "down"
    #         self.count -= 1
    #     self.speak_dialog("count.is.now", data={"count": self.count})

    #scan for devices
    @intent_handler(IntentBuilder("").require("Scan_on"))
    def handle_scan_on_intent(self,message):
        self.speak("Starting scan ...")
    @intent_handler(IntentBuilder("").require("Scan_off"))
    def handle_scan_off_intent(self,message):
        self.speak("Stoping scan...")

    #connecting to device
    @intent_handler(IntentBuilder("").require("List_devices"))
    def handle_list_devices(self,message):
        #TODO:store available devices 

        self.speak("Listing the devices available for BLE connection")

    @intent_handler(IntentBuilder("").require("Connect_device"))
    def handle_connect_device(self,message):
        #TODO:Connect_device.voc should be able to recognise the device name to be connected. This cannot be hardcoded.
        #TODO:name contains the device found during scan which user wants to connect to.
        name = "se"
        self.speak("Connecting to {}".format(name))

    #switch control 
    @intent_handler(IntentBuilder("").optionally("Switch").require("Control"))
    def handle_switch_control(self,message):
        if message.data["Control"] == "on":
            self.speak_dialog("switch.on")
        else:
            self.speak_dialog("switch.off")

    
    
    # The "stop" method defines what Mycroft does when told to stop during
    # the skill's execution. In this case, since the skill's functionality
    # is extremely simple, there is no need to override it.  If you DO
    # need to implement stop, you should return True to indicate you handled
    # it.
    #
    # def stop(self):
    #    return False

# The "create_skill()" method is used to create an instance of the skill.
# Note that it's outside the class itself.
def create_skill():
    return TemplateSkill()
