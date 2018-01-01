from sublime import DRAW_NO_OUTLINE
from sublime import Region
import sublime_plugin


# TODO Optimise to hell. This is just an initial proof of concept. Updating all
# lines of a views after every keystroke is very inefficient.

# TODO Report ST issue suggesting to improve style of the adding regions,
# because rounded regions, looks crap.


class RulerColumnEvents(sublime_plugin.EventListener):

    def _update_ruler_columns(self, view):
        settings = view.settings()
        if settings.get('word_wrap'):
            return

        ruler = settings.get('ruler_column')

        regions = []
        for line in view.lines(Region(0, view.size())):
            if line.size() > ruler:
                a = line.begin() + ruler
                regions.append(Region(a, a + 1))

        if regions:
            view.add_regions(
                'ruler_columns',
                regions,
                'ruler.column',
                '',
                DRAW_NO_OUTLINE)

    def on_activated_async(self, view):
        self._update_ruler_columns(view)

    def on_modified_async(self, view):
        self._update_ruler_columns(view)

    def on_post_save_async(self, view):
        self._update_ruler_columns(view)
