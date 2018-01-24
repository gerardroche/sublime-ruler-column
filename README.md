# RULER COLUMN

A Sublime Text plugin that shows ruler columns only on lines where the text overflows.

`Menu > Preferences > Settings`:

```json
{
    "ruler_column": 120
}
```

You can also set the width (defaults to `0`):

```json
{
    "ruler_column_width": 0
}
```

## Customising the color

In newer versions of Sublime Text (`~= 3154`) customising the color is straight forward enough.

Create a *color scheme override* in your Sublime Text User directory (find the User directory via `Menu > Preferences > Browse Packages...`). The override file must be the same name as the color scheme you want to override e.g. if you wanted to override the [MonokaiFree](https://github.com/gerardroche/sublime-monokai-free) color scheme then you would create a color scheme override file named `MonokaiFree.sublime-color-scheme` in your Sublime Text User directory. Here is an example:

```
{
    "rules":
    [
        {
            "scope": "ruler.column",
            "foreground": "#f92672",
            "background": "#f926729d"
        }
    ]
}
```

<!--
TODO Add link to documentation. The documentation for the new color scheme
format is not publicly available yet.
https://www.sublimetext.com/docs/3/color_schemes.html
-->
