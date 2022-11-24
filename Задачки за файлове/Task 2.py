import os

#Test the function

example_root_dir = os.path.join('SomeDirectory')
os.makedirs(example_root_dir, exist_ok=True)

nested_dir1 = os.path.join(example_root_dir, 'SomeNestedDirectory')
os.makedirs(nested_dir1, exist_ok=True)

nested_dir2 = os.path.join(example_root_dir, 'AnotherNestedDirectory')
os.makedirs(nested_dir2, exist_ok=True)

with open(os.path.join(nested_dir1, "SomeNestedFile.txt"), 'w') as nested_dir1_file:
    nested_dir1_file.writelines(["Huq\n", "mi\n", "Stan4o\n"])

with open(os.path.join(nested_dir2, "AnotherNestedFile.txt"), 'w') as nested_dir2_file:
    nested_dir2_file.writelines(["Kura\n", "mi\n", "Qnko\n"])

with open(os.path.join(example_root_dir, "SomeFile.txt"), 'w') as example_root_dir_file:
    example_root_dir_file.writelines(["Madoto\n", "mi\n", "Go6o\n"])
    
def rm_rf(dir):

    for dirname, subdirs, files in os.walk(dir):      
        for subdir in subdirs:
            rm_rf(os.path.join(dir, subdir))

        for file in files:
            os.remove(os.path.join(dir, file))

        os.rmdir(dir)

rm_rf(os.path.join(example_root_dir))



    