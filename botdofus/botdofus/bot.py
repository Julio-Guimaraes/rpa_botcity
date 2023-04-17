"""
WARNING:

Please make sure you install the bot with `pip install -e .` in order to get all the dependencies
on your Python environment.

Also, if you are using PyCharm or another IDE, make sure that you use the SAME Python interpreter
as your IDE.

If you get an error like:
```
ModuleNotFoundError: No module named 'botcity'
```

This means that you are likely using a different Python interpreter than the one used to install the bot.
To fix this, you can either:
- Use the same interpreter as your IDE and install your bot with `pip install -e .`
- Use the same interpreter as the one used to install the bot (`pip install -e .`)

Please refer to the documentation for more information at https://documentation.botcity.dev/
"""

from botcity.core import DesktopBot
# Uncomment the line below for integrations with BotMaestro
# Using the Maestro SDK
# from botcity.maestro import *


class Bot(DesktopBot):
    def action(self, execution=None):

        if not self.find("u1", matching=0.97, waiting_time=500000):
            self.not_found("u1")
        self.click()
        if not self.find("tol", matching=0.97, waiting_time=500000):
            self.not_found("tol")
        self.click()
        if not self.find("u2", matching=0.97, waiting_time=500000):
            self.not_found("u2")
        self.click()
        if not self.find("ton1", matching=0.97, waiting_time=500000):
            self.not_found("ton1")
        self.click()
        if not self.find("u3", matching=0.97, waiting_time=500000):
            self.not_found("u3")
        self.click()
        if not self.find("u4", matching=0.97, waiting_time=500000):
            self.not_found("u4")
        self.click()
        if not self.find("tr1", matching=0.97, waiting_time=500000):
            self.not_found("tr1")
        self.click()
        if not self.find("tn2", matching=0.97, waiting_time=500000):
            self.not_found("tn2")
        self.click()
    
    
    
           

    def not_found(self, label):
        print(f"Element not found: {label}")



if __name__ == '__main__':
    Bot.main()
