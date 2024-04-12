import os
import subprocess
import sys

def resource_path(relative_path):
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)

ffmpeg_executable_path = resource_path('ffmpeg/ffmpeg.exe')

def set_mp4_titles():
    os.system('cls')
    try:
        input_folder_path = input('Enter the folder path containing MP4 files (...\Show_name\Season): ')
        # Get a list of all MP4 files in the specified input folder
        mp4_files = [file for file in os.listdir(input_folder_path) if file.lower().endswith(".mp4")]

        print(f'Path : {input_folder_path}')
        print(f'Episode : {len(mp4_files)}')
        print('')
        for mp4_file in mp4_files:
            print(f"{os.path.splitext(mp4_file)[0]} -> #{os.path.splitext(mp4_file)[0]}" )
        print('')
        confirm = input('Are you sure? (y/n)')
        if (confirm in ['y','Y']):
            for mp4_file in mp4_files:
                # Extract the file name (without extension) from the full path
                file_name = os.path.splitext(mp4_file)[0]
                
                # Add '#' to the file name
                new_file_name = f"#{file_name}.mp4"
                
                # Set the title metadata using FFmpeg
                input_file_path = os.path.join(input_folder_path, mp4_file)
                output_file_path = os.path.join(input_folder_path, new_file_name)
                cmd = f'"{ffmpeg_executable_path}" -i "{input_file_path}" -metadata title="{file_name}" -c copy "{output_file_path}"'
                subprocess.run(cmd, shell=True)

                # Delete the old MP4 file
                os.remove(input_file_path)
                print(f"Title set for {mp4_file}: {file_name}. Old file removed.")
    except:
        print('Fail - Press Enter to Continue')
        input()

def set_mp4_filename():
    os.system('cls')
    input_folder_path = input('Enter the folder path containing MP4 files (...\Show_name\Season): ')
    try:
        # Get the show name and season number from the folder path
        folder_name = os.path.basename(input_folder_path)
        show_name = os.path.basename(os.path.dirname(input_folder_path))
        season_number = folder_name.split()[-1].zfill(2)

        # List all MP4 files in the folder
        mp4_files = [file for file in os.listdir(input_folder_path) if file.lower().endswith(".mp4")]

        # Sort the files by filename
        mp4_files.sort()

        print(f'Path : {input_folder_path}')
        print(f'Show : {show_name}')
        print(f'Season : {season_number}')
        print(f'Episode : {len(mp4_files)}')
        print('')
        i = 0
        for mp4_file in mp4_files:
            i = i+1
            print(f"{os.path.splitext(mp4_file)[0]} -> {show_name} - s{season_number}e{i:02d} " )
        confirm = input('Are you sure? (y/n)')
        if (confirm in ['y','Y']):
            # Rename each file with episode information
            for idx, mp4_file in enumerate(mp4_files, start=1):
                episode_number = f"s{season_number}e{idx:02d}"
                new_filename = f"{show_name} - {episode_number}.mp4"
                os.rename(os.path.join(input_folder_path, mp4_file), os.path.join(input_folder_path, new_filename))
                print(f"Renamed {mp4_file} to {new_filename}")
    except:
        print('Fail - Press Enter to Continue')
        input()





running = True
while (running):
    os.system('cls')
    print('1 ) Set the title metadata using file name ')
    print('2 ) Set the file name to S##E##')
    print('3 ) Exit')
    print()
    programNumber = input('Choose the program (1-3): ')
    if (programNumber == '1'):
        set_mp4_titles()
    elif (programNumber == '2'):
        set_mp4_filename()
    elif (programNumber == '3'):
        running = False
        os.system('cls')
        
