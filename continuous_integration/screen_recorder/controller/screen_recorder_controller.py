import os
from continuous_integration.screen_recorder.core.base import (
    Base,
)
from continuous_integration.screen_recorder.config.screen_recorder_config import (
    ScreenRecorderConfig,
)
from continuous_integration.screen_recorder.screen_recoder import ScreenRecoder
from services.disk.json.json_manager import JSONManager
import ffmpeg


# --
# ...
# --
class ScreenRecoderController(Base):
    def __init__(self) -> None:
        self.recorded_video_file_name = self.instance.config_dictionary["recorded_video_file_name"]
        self.recorded_video_directory = self.instance.config_dictionary[
            "recorded_video_directory"
        ]
        self.temp_recorded_video_file_name = self.instance.config_dictionary[
            "temp_recorded_video_file_name"
        ]
        self.control_file_address = self.instance.config_dictionary[
            "control_file_address"
        ]

        self.json = JSONManager().instance

        self.screen_recorder = ScreenRecoder()
        self.stop = False

    # --
    # ...
    # --

    @classmethod
    def get_config_dictionary(cls):
        return ScreenRecorderConfig().instance.dictionary

    # --
    # ... methods
    # --

    def start_recording(self):

        try:

            self.delete_old_file()

            context = """{"screen_recorder":{"is_record": true}}"""
            self.json.operation(address=self.control_file_address, context=context)

            self.screen_recorder.recording()

        except Exception as exp:
            print(repr(exp))
            return False

    # --
    # ...
    # --pip install pyscreeze

    def stop_recording(self):

        try:

            print("stop screen recording...")

            context = """{"screen_recorder":{"is_record": false}}"""
            self.json.operation(address=self.control_file_address, context=context)

            self.delay(5000)

            self.compress_video( f"{self.recorded_video_directory}{self.temp_recorded_video_file_name}", self.recorded_video_file_name, 10 * 1000)

            self.delete_old_file()

        except Exception as exp:
            print(repr(exp))
            return False

    # --
    # ...
    # --

    def delete_old_file(self):

        try:

            files = os.listdir(self.recorded_video_directory)
            for filename in files:
                if f"/{filename}".upper() == self.temp_recorded_video_file_name.upper():
                    os.remove(
                        f"{self.recorded_video_directory}{self.temp_recorded_video_file_name}"
                    )
                    break

        except Exception as exp:
            print(repr(exp))
            return False

    # --
    # ...
    # --

    def compress_video(self, video_full_path, output_file_name, target_size):

        print("video compressing...")

        probe = ffmpeg.probe(video_full_path)
        duration = float(probe['format']['duration'])

        target_total_bitrate = (target_size * 1024 * 8) / (1.073741824 * duration)

        video_bitrate = target_total_bitrate

        i = ffmpeg.input(video_full_path)
        
        ffmpeg.output(i, os.devnull,
                    **{'c:v': 'libx264', 'b:v': video_bitrate, 'pass': 1, 'f': 'mp4'}
                    ).overwrite_output().run()
        
        ffmpeg.output(i, output_file_name,
                    **{'c:v': 'libx264', 'b:v': video_bitrate, 'pass': 2, 'c:a': 'aac', 'b:a': 1}
                    ).overwrite_output().run()

