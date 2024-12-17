import cv2
import numpy
import pyautogui
from continuous_integration.screen_recorder.core.base import (
    Base,
)
from continuous_integration.screen_recorder.config.screen_recorder_config import (
    ScreenRecorderConfig,
)
import asyncio
from services.disk.json.json_manager import JSONManager

# --
# ...
# --


class ScreenRecoder(Base):
    def __init__(self) -> None:
        self.recorded_video_directory = self.instance.config_dictionary[
            "recorded_video_directory"
        ]
        self.temp_recorded_video_file_name = self.instance.config_dictionary[
            "temp_recorded_video_file_name"
        ]
        self.control_file_address = self.instance.config_dictionary[
            "control_file_address"
        ]

        self.codec = self.instance.config_dictionary["codec"]
        self.fps = self.instance.config_dictionary["fps"]
        self.fps_writer = self.instance.config_dictionary["fps_writer"]

        self.json = JSONManager().instance

        self.is_record = True

    # --
    # ...
    # --

    @classmethod
    def get_config_dictionary(cls):
        return ScreenRecorderConfig().instance.dictionary

    # --
    # ...
    # --

    def recording(self):
        screen_size = pyautogui.size()
        codec = cv2.VideoWriter.fourcc(*f"{self.codec}")
        output = cv2.VideoWriter(
            f"{self.recorded_video_directory}{self.temp_recorded_video_file_name}",
            codec,
            self.fps_writer,
            (screen_size),
        )

        print_counter = 0
        read_operation_counter = 0
        pre_frame = numpy.array([[0, 0, 0]])

        while self.get_is_record(read_operation_counter):
            if (read_operation_counter % self.fps_writer) == 0:
                print_counter += 1
                if print_counter % 10 == 0:
                    print(
                        f"screen recording {read_operation_counter/self.fps_writer} sec..."
                    )

            img = pyautogui.screenshot()
            frame = numpy.array(img)

            if not numpy.array_equal(frame, pre_frame):
                pre_frame = frame
                frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
                output.write(frame)

            read_operation_counter += 1

        output.release()
        cv2.destroyAllWindows()

    # --
    # ...
    # --

    def get_is_record(self, read_operation_counter):
        if read_operation_counter % 100 == 0:
            self.is_record = self.json.operation(address=self.control_file_address)[
                "screen_recorder"
            ]["is_record"]
        return self.is_record
