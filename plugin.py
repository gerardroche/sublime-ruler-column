from sublime import DRAW_NO_OUTLINE
from sublime import Region
import sublime_plugin


# TODO Optimise to hell. This is just an initial proof of concept. Updating all
# lines of a views after every keystroke is very inefficient.


class RulerColumnEvents(sublime_plugin.EventListener):

    def _update_ruler_columns(self, view):
        settings = view.settings()
        if settings.get('word_wrap'):
            return

        # Work around issues where build panels and other related views
        # shouldn't have the column ruler drawn. This is a heuristic, I don't
        # know of any canonical way to solve this issue.
        if settings.get('is_widget') or view.is_scratch() or settings.get('result_file_regex'):
            return

        regions = []
        ruler = settings.get('ruler_column')
        if ruler:
            for line in view.lines(Region(0, view.size())):
                if line.size() > ruler:
                    a = line.begin() + ruler
                    regions.append(Region(a, a + 1))

        # We're stuck using "no outline" regions, because Sublime Text can't
        # draw block-like (non-rounded) regions.
        # See https://github.com/SublimeTextIssues/Core/issues/2134.

        # We also need to add the regions, even if the regions list created
        # above is empty, because any stray column regions need to be cleared
        # e.g. if the user split a long line that have a column ruler then it
        # needs to cleared.

        view.add_regions(
            'ruler_columns',
            regions,
            'region.yellowish ruler.column',
            '',
            DRAW_NO_OUTLINE)

    def on_activated_async(self, view):
        self._update_ruler_columns(view)

    def on_modified_async(self, view):
        self._update_ruler_columns(view)

    def on_post_save_async(self, view):
        self._update_ruler_columns(view)
