from sublime import DRAW_EMPTY
from sublime import DRAW_NO_OUTLINE
from sublime import Region
import sublime_plugin


# TODO Optimise to hell. Perhaps you know how to optimise some of the code?


def _update(view):
    get = view.settings().get

    # Work around issues where build panels and other related views
    # shouldn't have the column ruler drawn. This is a heuristic, I don't
    # know of any canonical way to solve this issue.
    if get('is_widget') or view.is_scratch() or get('word_wrap') or get('result_file_regex'):
        return

    regions = []
    column = get('ruler_column')
    width = get('ruler_column_width', 0)
    if column:
        append = regions.append
        for line in view.lines(Region(0, view.size())):
            if line.size() > column:
                a = line.begin() + column
                append(Region(a, min(a + width, line.end())))

    # We also need to add the regions, even if the regions list created
    # above is empty, because any stray column regions need to be cleared
    # e.g. if the user split a long line that have a column ruler then it
    # needs to cleared.
    view.add_regions(
        'ruler_columns',
        regions,
        'region.redish ruler.column',
        '',
        # We're stuck using "no outline" regions for regions > 0, because
        # Sublime Text can't draw block-like (non-rounded) regions.
        # See https://github.com/SublimeTextIssues/Core/issues/2134.
        DRAW_NO_OUTLINE if width else DRAW_EMPTY)


class RulerColumn(sublime_plugin.EventListener):

    def on_activated_async(self, view):
        _update(view)

    def on_modified_async(self, view):
        _update(view)

    def on_post_save_async(self, view):
        _update(view)
