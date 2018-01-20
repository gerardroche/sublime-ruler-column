from sublime import DRAW_EMPTY
from sublime import DRAW_NO_OUTLINE
from sublime import Region
import sublime_plugin


# TODO Optimise to hell. This is just an initial proof of concept. Updating all
# lines of a views after every keystroke is very inefficient.


class RulerColumnEvents(sublime_plugin.EventListener):

    def _update(self, view):
        settings = view.settings()
        if settings.get('word_wrap'):
            return

        # Work around issues where build panels and other related views
        # shouldn't have the column ruler drawn. This is a heuristic, I don't
        # know of any canonical way to solve this issue.
        if settings.get('is_widget') or view.is_scratch() or settings.get('result_file_regex'):
            return

        regions = []

        column = settings.get('ruler_column')
        width = settings.get('ruler_column_width', 0)
        if column:
            for line in view.lines(Region(0, view.size())):
                if line.size() > column:
                    a = line.begin() + column
                    regions.append(Region(a, min(a + width, line.end())))

        # We also need to add the regions, even if the regions list created
        # above is empty, because any stray column regions need to be cleared
        # e.g. if the user split a long line that have a column ruler then it
        # needs to cleared.
        view.add_regions(
            'ruler_columns',
            regions,
            'region.yellowish ruler.column',
            '',
            # We're stuck using "no outline" regions for regions > 0, because
            # Sublime Text can't draw block-like (non-rounded) regions.
            # See https://github.com/SublimeTextIssues/Core/issues/2134.
            DRAW_NO_OUTLINE if width > 0 else DRAW_EMPTY)

    def on_activated_async(self, view):
        self._update(view)

    def on_modified_async(self, view):
        self._update(view)

    def on_post_save_async(self, view):
        self._update(view)
