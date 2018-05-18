'''
Below are functions that will be loaded when calling: import ship_mapper as sm
'''
from .converters import convert_to_nc, bulk_convert_to_nc

from .utils import (distance, estimate_velocity, elapsed_days,
                    align_with_grid, interp2d, spatial_filter,
                    checkDir, make_mydirs, get_all_files,
                    get_filename_from_fullpath, get_path_from_fullpath,
                    degrees_to_meters,write_info2data, stop)

from .gridder import gridder, grid_merger, mergedgrid_to_shp

from .mapper import map_density, map_dots, make_basemap, map_dots_one_ship, save_basemap

from .info_object import info, load_info, grid_to_info, data_to_info, info_to_attrs, attrs_to_info



def load_settings(path_to_settings=None):
    import imp
    from pathlib import Path
    
    if path_to_settings == None:
        path2settings = Path('../')
    else:
        path2settings=path_to_settings
    
    print('Loading settings file...')
    file, pathname, description = imp.find_module('settings',[path2settings])   
    settings = imp.load_module('settings', file, pathname, description)
    return settings

