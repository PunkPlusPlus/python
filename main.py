from l14.l14_code import tasks
from pathlib import Path

folder_path = '.'
extension = 'py'

#files = tasks.find_files_by_extension(folder_path, extension)

tasks.remove_empty_directories(Path('.'))


