
class DictMixin:
    def to_dict(self):
        return self._traverse_dict(self.__dict__)

    def _traverse_dict(self, attributes: dict) -> dict:
        result = {}
        for key, value in attributes.items():
            result[key] = self._traverse(key, value)

        return result

    def _traverse(self, key, value):
        if isinstance(value, DictMixin):
            return value.to_dict()
        elif isinstance(value, dict):
            return self._traverse_dict(value)
        elif isinstance(value, list):
            return [self._traverse(key, v) for v in value]
        elif hasattr(value, '__dict__'):
            return self._traverse_dict(value.__dict__)
        else:
            return value


class CameraMixin:
    def photo(self):
        print("Take a photo")

    def record_video(self):
        print("Start recording")

    def portrait_mode(self):
        print("Take a nice photo of you")


class SoundPlayerMixin:
    def play_music(self):
        print("Song ...")

    def pause_music(self):
        print("Pause")

    def continue_music(self):
        print("Continue")

    def stop_music(self):
        print("Stop")


class AppLauncherMixin:
    def start_app(self, app):
        print(f"Start APP {app}")

    def close_app(self, app):
        print(f"Close APP {app}")


class SmartPhone(CameraMixin, SoundPlayerMixin, AppLauncherMixin, DictMixin):
    def __init__(self, model, series, color):
        self.model = model
        self.series = series
        self.color = color

    def call(self):
        print("Call")

    def answer(self):
        print("Call")

    def go_to_web(self):
        print("WWW")


class MusicPlayer(SoundPlayerMixin):
    ...

class Tablet(CameraMixin, AppLauncherMixin, SoundPlayerMixin):
    ...


class ContainsFileMixin:
    url: str
    file_path: str


class BaseModel:
    id: int
    name: str


class VideoContent(BaseModel, ContainsFileMixin):
    duration: int



class AudioContent(BaseModel, ContainsFileMixin):
    url: str
    file_path: str






x =DictMixin()

s = SmartPhone("Iphone", "20", "white")
print(x.to_dict())
print(s.to_dict())
