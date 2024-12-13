from datetime import datetime
from pygame import Surface
from surface_generator import SurfaceGenerator
from text.alignment import Alignment
from typing import List


class TimeContent:
    """Class for displaying time information on screen"""

    @staticmethod
    def get_time_string() -> str:
        """Get the string representation for the current time"""
        return datetime.now().time().strftime("%H:%M")

    @staticmethod
    def get_time_surface() -> List[Surface]:
        """Gets the current time as a surface to display"""
        return [
            SurfaceGenerator.text_surface(TimeContent.get_time_string(), alignment=Alignment.CENTER, is_big=True),
            SurfaceGenerator.vertical_spacer(20)
        ]
