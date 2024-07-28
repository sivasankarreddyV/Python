#reloading a module
print("This is from module")

import module
import module
from imp import reload
reload(module)
reload(module)
reload(module)
print("This is test module")

