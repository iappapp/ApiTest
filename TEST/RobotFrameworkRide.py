from robotide.preferences import RideSettings
from robotide import main
import os

if __name__ == '__main__':
    current_dir = os.path.dirname(__file__)
    dir_list = list()
    dir_list.append(os.path.join(current_dir, '/ApiTestLib'))
    dir_list.append(os.path.join(current_dir, '/ApiTestLib/scripts'))
    settings = RideSettings()

    settings.set('auto imports', dir_list)
    main()