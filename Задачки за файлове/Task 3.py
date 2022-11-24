import os

class mspotify_api:

    def __init__(self) -> None:
        self.COMMAND_ARGSEPERATOR = "|"
        self.COMMAND_SET = "SET"
        self.COMMAND_LIST = "LIST"
        self.COMMAND_FIND_ARTIST = "FIND ARTIST"
        self.COMMAND_FIND_SONG = "FIND SONG"
        self.COMMAND_EXIT = "EXIT"
        self.COMMANDS = [self.COMMAND_SET, self.COMMAND_LIST, self.COMMAND_FIND_ARTIST, self.COMMAND_FIND_SONG, self.COMMAND_EXIT]

        self.music_dir = None

    def start_program(self):      
        while True:
            userInput = input("Input Command (command|arguments): ")
            splitInput = userInput.split(self.COMMAND_ARGSEPERATOR) 
            curCommand = splitInput[0]
            arguments = []

            if len(splitInput) >= 2:
                arguments = [argument for argument in splitInput[1:]]

            if curCommand.lower() in [command.lower() for command in self.COMMANDS]:
                if curCommand.lower() == self.COMMAND_EXIT.lower():
                    break
                elif curCommand.lower() == self.COMMAND_SET.lower():
                    self.set_command(*arguments)
                elif curCommand.lower() == self.COMMAND_LIST.lower():
                    print(self.list_command(*arguments))
                elif curCommand.lower() == self.COMMAND_FIND_ARTIST.lower():
                    print(self.find_artist_command(*arguments))
                elif curCommand.lower() == self.COMMAND_FIND_SONG.lower():
                    print(self.find_song_command(*arguments))
            else:
                print("Nevalidna komanda")

    def command_execute(command):       
        def command_execution(*args, **kwargs):
            command_value, command_success = command(*args, **kwargs)

            if command_success:
                print("Command successful!")
            else:
                print("Command unsuccessful!")

            return command_value

        return command_execution

    @command_execute
    def set_command(self, new_music_dir):
        self.music_dir = os.path.join(new_music_dir)    

        return None, True  

    def music_from_dir(self, music_dir):
        music_files_root = [mfile for mfile in os.listdir(music_dir) if os.path.isfile(os.path.join(music_dir, mfile))]

        root_subdirs = [subdir for subdir in os.listdir(music_dir) if os.path.isdir(os.path.join(music_dir, subdir))]

        # if len(root_subdirs) == 0:
        #     music_files_root = map(lambda file: self.strip_song_extension(file), music_files_root)
        #     return music_files_root, True

        music_files_from_subdirs = []

        for root_subdir in root_subdirs:
            music_files_subdir, success = self.music_from_dir(os.path.join(music_dir, root_subdir))

            music_files_from_subdirs.extend(music_files_subdir)

        music_files_root.extend(music_files_from_subdirs)

        music_files_root = map(lambda file: self.strip_song_extension(file), music_files_root)
        # 
        return list(music_files_root), True

    @command_execute
    def list_command(self):
        return self.music_from_dir(self.music_dir)

    @command_execute
    def find_artist_command(self, artist_name):
        music_files = self.music_from_dir(self.music_dir)[0]

        music_files_from_artist = [music_file.split('-')[1] for music_file in music_files if 
            music_file.split('-')[0] == artist_name]

        return music_files_from_artist, True

    def strip_song_extension(self, song_full_name):
        return song_full_name.split('.mp3')[0]

    @command_execute
    def find_song_command(self, song_name):
        music_files = self.music_from_dir(self.music_dir)[0]

        music_song = [music_file.split('-')[1] for music_file in music_files if 
            music_file.split('-')[1] == song_name]

        return music_song, True


spotify_api = mspotify_api()

spotify_api.start_program()


    