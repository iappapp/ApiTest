from robotide.preferences import RideSettings, Preferences
from robotide import main
import os

if __name__ == '__main__':
    current_dir = os.path.dirname(os.path.abspath(__file__))
    settings = RideSettings()
    dir_list = []
    dir_list.append(os.path.join(current_dir, 'ApiTestLib'))
    dir_list.append(os.path.join(current_dir, 'ApiTestLib', 'scripts'))
    dir_list.append(os.path.join(current_dir, 'TEST'))
    settings.set('auto imports', dir_list)
    settings.set('pythonpath', dir_list)
    # preference = Preferences(settings)

    main()